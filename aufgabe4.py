import argparse
import os



def parse_old(args):
    path = args.folder
    old_name = args.old
    for file in os.listdir(path):
        if old_name in file:
            full_path_master = os.path.join(path, old_name + "_master.dat")
            with open(full_path_master, 'r', encoding="utf-8") as file_:
                data = file_.read()
                print(data)
                return data



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', required=True, type=str)
    parser.add_argument('-o', '--old', required=True, type=str)
    parser.add_argument('-n', '--new', required=True, type=str)
    args = parser.parse_args()

    parse_old(args)



if __name__ == '__main__':
    main()