import os
import sys
from pathlib import Path

def usage():
    print("Usage: python compare_folders.py <folder1> <folder2>")
    sys.exit(1)

# Argumentprüfung
if len(sys.argv) != 3:
    usage()

folder1 = Path(sys.argv[1])
folder2 = Path(sys.argv[2])

# Existenzprüfung der Ordner
if not folder1.is_dir():
    print(f"Error: Folder {folder1} does not exist.")
    sys.exit(1)
if not folder2.is_dir():
    print(f"Error: Folder {folder2} does not exist.")
    sys.exit(1)

files1 = {f.name: f for f in folder1.iterdir() if f.is_file()}
files2 = {f.name: f for f in folder2.iterdir() if f.is_file()}

all_files = set(files1.keys()) | set(files2.keys())

for filename in sorted(all_files):
    f1 = files1.get(filename)
    f2 = files2.get(filename)

    if f1 and not f2:
        print(f"Datei {filename} nur in {folder1}")
    elif f2 and not f1:
        print(f"Datei {filename} nur in {folder2}")
    else:
        size1 = f1.stat().st_size
        size2 = f2.stat().st_size
        mtime1 = f1.stat().st_mtime
        mtime2 = f2.stat().st_mtime

        if size1 == size2 and mtime1 == mtime2:
            print(f"Datei {filename} ist in beiden Ordnern identisch")
        else:
            if size1 != size2:
                bigger = folder1 if size1 > size2 else folder2
                print(f"Datei {filename} in {bigger} ist grösser")
            if mtime1 != mtime2:
                newer = folder1 if mtime1 > mtime2 else folder2
                print(f"Datei {filename} in {newer} ist neuer")
