import subprocess
from pathlib import Path

# Pfad für das neue Verzeichnis
dir_path = Path("/tmp/python_bash_test")

# 1. Verzeichnis erstellen
subprocess.run(["mkdir", "-p", str(dir_path)], check=True)
print(f"Verzeichnis erstellt: {dir_path}")

# 2. Überprüfen, ob das Verzeichnis existiert (ls -l /tmp)
print("Inhalt von /tmp:")
subprocess.run(["ls", "-l", "/tmp"])

# 3. Dateien erstellen
files = ["file1.txt", "file2.txt", "file3.txt"]
for file in files:
    file_path = dir_path / file
    subprocess.run(["touch", str(file_path)], check=True)
print(f"Dateien erstellt: {', '.join(files)}")

# 4. Inhalt des Verzeichnisses auflisten (ls)
print(f"Inhalt von {dir_path}:")
subprocess.run(["ls", str(dir_path)])

# 5. Dateigrößen anzeigen (du -h)
print(f"Größe der Dateien in {dir_path}:")
subprocess.run(["du", "-h", str(dir_path) + "/*"])

# 6. Zusatz: Eine Datei löschen (file3.txt)
file_to_delete = dir_path / "file3.txt"
subprocess.run(["rm", str(file_to_delete)], check=True)
print(f"{file_to_delete} wurde gelöscht.")

# Aktualisierte Liste der Dateien
print(f"Aktueller Inhalt von {dir_path}:")
subprocess.run(["ls", str(dir_path)])
