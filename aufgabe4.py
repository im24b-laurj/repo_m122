import argparse
import os
import sys


def parse_old(args):
    path = args.folder
    old_name = args.old
    new_name = args.new
    paths = []
    for file in os.listdir(path):
        if "master" in file:

            with open( path+ "/"+file, "r", encoding="utf-8") as f:
                for line in f:
                    print("checked_master")
                    line = line.strip()

                    if not line or line.startswith("#"):
                        continue

                    if "=" not in line:
                        continue
                    _, value = line.split("=", 1)
                    if value.startswith("/"):
                        paths.append(value)

            os.rename(os.path.join(path, old_name), os.path.join(new_name, file))

        else:
            if len(new_name) > 1:
                already_renamed = False
                for i in new_name:
                    if already_renamed == False:
                        os.rename(os.path.join(path, old_name), os.path.join(path, i))
                        already_renamed = True
                        print("renamed" + i)
                    else:
                        open("/data/" + i, "w").close()
                        print("renamed" + i)





            else:
                new_file = file.replace(old_name, new_name[0])
                os.rename(os.path.join(path, file), os.path.join(path, new_file))













def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', required=True, type=str)
    parser.add_argument('-o', '--old', required=True, type=str)
    parser.add_argument('-n', '--new', required=True, type=str, nargs='+')
    args = parser.parse_args()

    parse_old(args)



if __name__ == '__main__':
    main()