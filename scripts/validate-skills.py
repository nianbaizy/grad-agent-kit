#!/usr/bin/env python3
"""
Validate GradAgentKit skills structure.

This script checks if each skill directory contains the required files.

Usage:
    python scripts/validate-skills.py

Expected output:
    ✅ paper-writer passed
    ✅ experiment-analyzer passed
    ❌ reviewer-simulator missing checklist.md
"""

import os
import sys
from pathlib import Path

# Required files for each skill
REQUIRED_FILES = [
    'SKILL.md',
    'input-template.md',
    'output-format.md',
    'checklist.md',
]

# Optional directories
OPTIONAL_DIRS = [
    'examples',
]


def get_skills_directory():
    """Get the skills directory path."""
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    skills_dir = project_dir / 'skills'
    return skills_dir


def validate_skill(skill_dir):
    """
    Validate a single skill directory.

    Args:
        skill_dir: Path to the skill directory

    Returns:
        tuple: (is_valid, missing_files, missing_dirs)
    """
    missing_files = []
    missing_dirs = []

    # Check required files
    for file_name in REQUIRED_FILES:
        file_path = skill_dir / file_name
        if not file_path.exists():
            missing_files.append(file_name)

    # Check optional directories (warning only)
    for dir_name in OPTIONAL_DIRS:
        dir_path = skill_dir / dir_name
        if not dir_path.exists():
            missing_dirs.append(dir_name)

    is_valid = len(missing_files) == 0
    return is_valid, missing_files, missing_dirs


def main():
    """Main validation function."""
    skills_dir = get_skills_directory()

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        sys.exit(1)

    # Get all skill directories
    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]

    if not skill_dirs:
        print("⚠️  No skills found in skills directory")
        sys.exit(0)

    # Validate each skill
    passed = 0
    failed = 0
    warnings = 0

    print("[VALIDATE] Validating GradAgentKit skills...\n")

    for skill_dir in sorted(skill_dirs):
        skill_name = skill_dir.name

        # Skip hidden directories
        if skill_name.startswith('.'):
            continue

        is_valid, missing_files, missing_dirs = validate_skill(skill_dir)

        if is_valid:
            print(f"[PASS] {skill_name} passed")
            passed += 1

            # Show warnings for missing optional directories
            if missing_dirs:
                for dir_name in missing_dirs:
                    print(f"   [WARN] Missing optional directory: {dir_name}")
                warnings += len(missing_dirs)
        else:
            print(f"[FAIL] {skill_name} failed")
            for file_name in missing_files:
                print(f"   Missing: {file_name}")
            failed += 1

    # Summary
    print(f"\n[SUMMARY]")
    print(f"   [PASS] Passed: {passed}")
    print(f"   [FAIL] Failed: {failed}")
    print(f"   [WARN] Warnings: {warnings}")
    print(f"   [TOTAL] Total: {passed + failed}")

    # Exit with error if any skill failed
    if failed > 0:
        print(f"\n[ERROR] Validation failed! {failed} skill(s) have issues.")
        sys.exit(1)
    else:
        print(f"\n[SUCCESS] All skills passed validation!")
        sys.exit(0)


if __name__ == '__main__':
    main()