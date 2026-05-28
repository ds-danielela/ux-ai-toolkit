#!/usr/bin/env python3
"""
rebuild_guidelines.py
---------------------
Rebuilds knowledge_base/guidelines/ files from source data.

Run this script whenever you:
  - Add a new component .md doc
  - Add a new component .json record
  - Update a foundation doc (border.md, spacing.md, etc.)
  - Change a usage rule in any component record

Usage:
  python rebuild_guidelines.py

Output files (written to ./guidelines/):
  - component-status.json   (registry of all 59 components + coverage)
  - token-usage-rules.json  (token pairing rules from foundation docs)
  - do-dont-rules.json      (all usage rules extracted from component records)

Requirements:
  pip install rich   # optional, for pretty output
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

# ── CONFIG ────────────────────────────────────────────────────────────────────

KNOWLEDGE_BASE = Path(__file__).parent.parent  # adjust if script is in a subfolder
COMPONENTS_DIR = KNOWLEDGE_BASE / "components"
GUIDELINES_DIR = KNOWLEDGE_BASE / "guidelines"
TOKENS_FILE    = KNOWLEDGE_BASE / "tokens" / "design-tokens.json"

GUIDELINES_DIR.mkdir(parents=True, exist_ok=True)

VERSION = "0.33.0"

# ── HELPERS ───────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def write_json(path: Path, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Written: {path.relative_to(KNOWLEDGE_BASE)}")

def load_all_component_records() -> list[dict]:
    """Load every *.component.json from the components/ directory."""
    records = []
    for p in sorted(COMPONENTS_DIR.glob("*.component.json")):
        try:
            records.append(load_json(p))
        except Exception as e:
            print(f"  ⚠ Could not load {p.name}: {e}")
    return records

# ── 1. COMPONENT STATUS ───────────────────────────────────────────────────────

def rebuild_component_status(records: list[dict]):
    """
    Rebuilds component-status.json from:
    - The existing component-status.json (as the source of truth for all 59 components)
    - The component record files (to update record_file and coverage)
    """
    existing_path = GUIDELINES_DIR / "component-status.json"
    if not existing_path.exists():
        print("  ⚠ component-status.json not found — skipping rebuild. Seed it manually first.")
        return

    status = load_json(existing_path)

    # Build a lookup of which records exist
    record_files = {p.name for p in COMPONENTS_DIR.glob("*.component.json")}
    record_by_id = {}
    for r in records:
        record_by_id[r["id"]] = r

    # Update record_file pointers and coverage
    for comp in status["components"]:
        cid = comp["id"]
        # Find matching record file
        expected_filename = cid.replace("component-", "") + ".component.json"
        if expected_filename in record_files:
            comp["record_file"] = expected_filename
        else:
            comp["record_file"] = None

    # Update coverage stats
    total = len(status["components"])
    fully_ready = sum(
        1 for c in status["components"]
        if c.get("figma_ready") and c.get("doc_ready") and c.get("storybook_ready")
    )
    gaps = sum(
        1 for c in status["components"]
        if not c.get("doc_ready") or not c.get("storybook_ready")
    )
    records_generated = sum(1 for c in status["components"] if c.get("record_file"))

    status["meta"]["total_components"] = total
    status["meta"]["fully_ready"] = fully_ready
    status["meta"]["gaps"] = gaps
    status["meta"]["last_rebuilt"] = datetime.utcnow().isoformat() + "Z"
    status["record_coverage"]["total_records_generated"] = records_generated
    status["record_coverage"]["records"] = sorted(
        [c["record_file"] for c in status["components"] if c.get("record_file")]
    )
    status["record_coverage"]["remaining"] = fully_ready - records_generated

    write_json(existing_path, status)

# ── 2. DO-DONT RULES ─────────────────────────────────────────────────────────

def rebuild_do_dont_rules(records: list[dict]):
    """
    Rebuilds do-dont-rules.json by:
    - Keeping the global rules (hand-authored, scope=global)
    - Re-extracting usage_rules from every component record
    - Deduplicating by rule text
    """
    existing_path = GUIDELINES_DIR / "do-dont-rules.json"
    if not existing_path.exists():
        print("  ⚠ do-dont-rules.json not found — skipping rebuild.")
        return

    existing = load_json(existing_path)

    # Keep global rules as-is (they are hand-authored)
    global_rules = [r for r in existing["rules"] if r.get("scope") == "global"]

    # Extract component-scoped rules from all records
    component_rules = []
    seen_rules = set()

    for record in records:
        component_name = record.get("name", "Unknown")
        for rule in record.get("usage_rules", []):
            key = rule.get("rule", "")
            if key in seen_rules:
                continue
            seen_rules.add(key)

            # Determine component_scope
            existing_scope = rule.get("component_scope")
            if not existing_scope:
                existing_scope = [component_name]

            component_rules.append({
                "id": f"rule-extracted-{len(component_rules)+1:03d}",
                "component_scope": existing_scope if isinstance(existing_scope, list) else [existing_scope],
                "severity": rule.get("severity", "warning"),
                "rule": key,
                "detail": rule.get("detail", ""),
                "source_record": record.get("id")
            })

    # Merge: global first, then component-extracted
    # Re-number ids for global rules to keep them stable
    all_rules = global_rules + component_rules

    existing["rules"] = all_rules
    existing["meta"]["last_rebuilt"] = datetime.utcnow().isoformat() + "Z"
    existing["meta"]["total_rules"] = len(all_rules)
    existing["meta"]["sources"] = sorted([p.name for p in COMPONENTS_DIR.glob("*.component.json")])

    write_json(existing_path, existing)

# ── 3. TOKEN USAGE RULES ─────────────────────────────────────────────────────

def rebuild_token_usage_rules():
    """
    token-usage-rules.json is derived from foundation docs only.
    It is stable — only changes when foundation docs change.
    This function just updates the last_rebuilt timestamp.
    To fully regenerate, re-run the initial generation with Claude.
    """
    path = GUIDELINES_DIR / "token-usage-rules.json"
    if not path.exists():
        print("  ⚠ token-usage-rules.json not found — skipping.")
        return

    data = load_json(path)
    data["meta"]["last_rebuilt"] = datetime.utcnow().isoformat() + "Z"
    write_json(path, data)
    print("  ℹ  token-usage-rules.json: foundation-derived, timestamp updated.")
    print("     To fully regenerate (e.g. after changing border.md/spacing.md),")
    print("     paste the updated .md files to Claude and request regeneration.")

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print(f"\n🔄  Rebuilding knowledge_base/guidelines/")
    print(f"    Source: {KNOWLEDGE_BASE}\n")

    if not COMPONENTS_DIR.exists():
        print(f"  ✗ components/ directory not found at {COMPONENTS_DIR}")
        sys.exit(1)

    records = load_all_component_records()
    print(f"  ✓ Loaded {len(records)} component records\n")

    print("  → Rebuilding component-status.json ...")
    rebuild_component_status(records)

    print("\n  → Rebuilding do-dont-rules.json ...")
    rebuild_do_dont_rules(records)

    print("\n  → Updating token-usage-rules.json ...")
    rebuild_token_usage_rules()

    print(f"\n✅  Done. {len(records)} records processed.\n")

if __name__ == "__main__":
    main()
