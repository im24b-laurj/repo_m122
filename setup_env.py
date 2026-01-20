#!/usr/bin/env python3
"""
Setup script for LB2 Trial - Badge-Generator
Creates a test environment with a participant list and badge template.

Usage: python setup_env.py [DIRECTORY_NAME]
Example: python setup_env.py konferenz
"""

import os
import sys


def create_directory(path):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Verzeichnis erstellt: {path}")


def create_file(path, content):
    """Create a file with the given content."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Datei erstellt: {path}")


def setup_environment(base_dir):
    """Set up the complete test environment."""

    # Remove existing directory if it exists (clean slate)
    if os.path.exists(base_dir):
        import shutil
        shutil.rmtree(base_dir)
        print(f"Bestehendes Verzeichnis gelöscht: {base_dir}")

    # Create base directory
    create_directory(base_dir)

    # Create teilnehmer.csv
    teilnehmer_csv = """name,firma,rolle
Maria Huber,TechCorp AG,Speaker
Jonas Keller,DataFlow GmbH,Teilnehmer
Sophie Braun,CodeLab Inc,Workshop-Leiter
Lukas Fischer,NetSystems,Teilnehmer
Emma Wagner,AI Solutions,Speaker"""

    create_file(os.path.join(base_dir, "teilnehmer.csv"), teilnehmer_csv)

    # Create vorlage.txt (badge template)
    vorlage_txt = """╔══════════════════════════════════════╗
║         TECH KONFERENZ 2026          ║
╠══════════════════════════════════════╣
║                                      ║
║  Name:  <<NAME>>                     ║
║  Firma: <<FIRMA>>                    ║
║  Rolle: <<ROLLE>>                    ║
║                                      ║
║  Badge-ID: <<BADGE_ID>>              ║
║  Erstellt: <<DATUM>>                 ║
║                                      ║
╚══════════════════════════════════════╝
"""

    create_file(os.path.join(base_dir, "vorlage.txt"), vorlage_txt)

    print(f"\n✓ Umgebung erfolgreich erstellt in: {base_dir}/")
    print(f"  ├── teilnehmer.csv")
    print(f"  └── vorlage.txt")


def main():
    if len(sys.argv) != 2:
        print("Fehler: Bitte geben Sie einen Verzeichnisnamen an.")
        print("Verwendung: python setup_env.py [VERZEICHNISNAME]")
        print("Beispiel: python setup_env.py konferenz")
        sys.exit(1)

    base_dir = sys.argv[1]
    setup_environment(base_dir)


if __name__ == "__main__":
    main()
