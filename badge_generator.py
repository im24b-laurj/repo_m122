import sys
import os
import datetime

import csv


def parse_arguments():
    if len(sys.argv) < 2:
        exit(1)
    if os.path.exists(sys.argv[1]) == False:
        exit(1)

    return sys.argv[1]



def read_participants(path_to_csv):

    participants = []
    with open(path_to_csv, 'r') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)
        return data_list


def read_template(template_path):
    with open(template_path, 'r', encoding="utf-8") as file:
        data = file.read()
        return data


def generate_badge_id(name, index):
    if len(str(index)) > 1 and len(str(index)) < 3:
        index = f'0{str(index)}'
    else:
        index = f'00{str(index)}'
    name_split = name.split()
    last_name = name_split[-1]
    first_3_letter = last_name[:3]
    first_3_letter_upper = first_3_letter.upper()

    badge_id = f'{first_3_letter_upper}-{index}'
    return badge_id


def create_badge(template, participant, badge_id):
    print(participant)
    name = participant["name"]
    firma = participant["firma"]
    rolle = participant["rolle"]



    template = template.replace("<<NAME>>", name)
    template = template.replace("<<FIRMA>>", firma)
    template = template.replace("<<ROLLE>>", rolle)
    template = template.replace("<<BADGE_ID>>", badge_id)
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%d.%m.%Y")
    template = template.replace("<<DATE>>", formatted)
    return template



def save_badge(badge_content, output_path):
    with open(output_path, 'w', encoding="utf-8") as file:
        file.write(badge_content)

def write_log(message, log_path):
    with open(log_path, 'a', encoding="utf-8") as file:
        file.write(message)

def main():
    path_to_directory = parse_arguments()
    path_to_csv = os.path.join(path_to_directory, "teilnehmer.csv")
    participants = read_participants(path_to_csv)
    path_txt = path_to_directory + "/vorlage.txt"
    template = read_template(path_txt)
    index = 0
    path_to_csv = os.path.join(path_to_directory, "teilnehmer.csv")
    os.makedirs(path_to_directory + '/badges', exist_ok=True)
    log_path = os.path.join(path_to_directory, "badge_log.txt")

    for i in participants:
        index += 1
        name = i["name"]
        badge_id = generate_badge_id(name, index)
        badge_done = create_badge(template, i, badge_id)
        save_badge(badge_done, os.path.join(path_to_directory, "badges", f"{badge_id}.txt"))
        write_log(name, path_to_directory + "/badge_log")

    print("Insgesamt" + str(index) + " Badges erstellt")



















if __name__ == "__main__":
    main()
