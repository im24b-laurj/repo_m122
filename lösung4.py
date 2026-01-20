import argparse
import shutil
from pathlib import Path


def update_master_file(master_path: Path, old_str: str, new_str: str):
    """
    Liest die Masterdatei, ersetzt alte Strings durch neue Strings
    und speichert das Ergebnis in einer neuen Masterdatei.
    """
    new_master_path = master_path.parent / master_path.name.replace(old_str, new_str)
    with open(master_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = content.replace(old_str, new_str)

    with open(new_master_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    return new_master_path


def rename_files(folder: Path, old_str: str, new_names: list):
    """
    Sucht alle Dateien im Ordner, die old_str enthalten,
    und erstellt Kopien/Umbenennungen für jeden Eintrag in new_names.
    """
    for new_str in new_names:
        for file in folder.iterdir():
            if old_str in file.name:
                # Neuen Dateinamen erstellen
                new_file_name = file.name.replace(old_str, new_str)
                new_file_path = folder / new_file_name

                # Datei kopieren/umbenennen
                if file.name != new_file_name:
                    shutil.copy2(file, new_file_path)
                    print(f"{file.name} -> {new_file_name}")

                # Masterdatei aktualisieren, falls es eine Masterdatei ist
                if "master" in file.name:
                    update_master_file(file, old_str, new_str)


def main():
    parser = argparse.ArgumentParser(description="Dateien umbenennen und Masterdateien aktualisieren.")
    parser.add_argument("--folder", "-f", required=True, help="Pfad zum Ordner mit den Dateien")
    parser.add_argument("--old", "-o", required=True, help="Zu ersetzende Zeichenfolge im Dateinamen")
    parser.add_argument("--new", "-n", required=True, action="append",
                        help="Neue Zeichenfolge im Dateinamen (mehrfach erlaubt)")

    args = parser.parse_args()

    folder_path = Path(args.folder)
    if not folder_path.is_dir():
        print(f"Fehler: Ordner {folder_path} existiert nicht.")
        return

    rename_files(folder_path, args.old, args.new)


if __name__ == "__main__":
    main()
