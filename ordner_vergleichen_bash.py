import sys
import subprocess
from pathlib import Path

def usage():
    print("Usage: python compare_folders.py <folder1> <folder2>")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

folder1 = Path(sys.argv[1])
folder2 = Path(sys.argv[2])

if not folder1.is_dir():
    print(f"Error: Folder {folder1} does not exist.")
    sys.exit(1)
if not folder2.is_dir():
    print(f"Error: Folder {folder2} does not exist.")
    sys.exit(1)

def list_files(folder):
    result = subprocess.run(["ls", str(folder)], capture_output=True, text=True)
    return set(result.stdout.split())

files1 = list_files(folder1)
files2 = list_files(folder2)

all_files = files1 | files2

for filename in sorted(all_files):
    f1_path = folder1 / filename
    f2_path = folder2 / filename

    if filename in files1 and filename not in files2:
        print(f"Datei {filename} nur in {folder1}")
    elif filename in files2 and filename not in files1:
        print(f"Datei {filename} nur in {folder2}")
    else:
        # Dateigröße
        size1 = int(subprocess.run(["stat", "-c", "%s", str(f1_path)], capture_output=True, text=True).stdout.strip())
        size2 = int(subprocess.run(["stat", "-c", "%s", str(f2_path)], capture_output=True, text=True).stdout.strip())
        # Änderungsdatum
        mtime1 = float(subprocess.run(["stat", "-c", "%Y", str(f1_path)], capture_output=True, text=True).stdout.strip())
        mtime2 = float(subprocess.run(["stat", "-c", "%Y", str(f2_path)], capture_output=True, text=True).stdout.strip())

        if size1 == size2 and mtime1 == mtime2:
            print(f"Datei {filename} ist in beiden Ordnern identisch")
        else:
            if size1 != size2:
                bigger = folder1 if size1 > size2 else folder2
                print(f"Datei {filename} in {bigger} ist grösser")
            if mtime1 != mtime2:
                newer = folder1 if mtime1 > mtime2 else folder2
                print(f"Datei {filename} in {newer} ist neuer")
