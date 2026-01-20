#!/usr/bin/env python3

import argparse
from datetime import date, datetime, timedelta
import sys
from pathlib import Path

def parse_arguments() -> str:
    if len(sys.argv[1]) < 2:
        sys.exit(1)

    workdirectory = Path(sys.argv[1])

    if not workdirectory.exists() or not workdirectory.is_dir():
        sys.exit(-1)

    print("test")
    return str(workdirectory)

def read_participants(csv_path) -> list:
    path = Path(csv_path)

    user = []

    lines = path.read_text().splitlines()

    for line in lines[1:]:
        name, firma, rolle = [x.strip() for x in line.split(",")]
        user.append({"name": name, "firma": firma, "rolle": rolle})

    return user

def read_template(template_path):
    path = Path(template_path)

    return path.read_text()

def generate_badge_id(name, index):
    nachname = name.strip().split(" ")[-1]
    return f"{(nachname[:3].upper())}-{index:03}"

def create_badge(template, participant, badge_id):
    return template.replace("<<NAME>>", participant["name"]).replace("<<FIRMA>>", participant["firma"]).replace("<<ROLLE>>", participant["rolle"]).replace("<<BADGE_ID>>", badge_id).replace("<<DATUM>>", datetime.today().strftime("%d.%m.%Y"))

def save_badge(badge_content, output_path):
    path = Path(output_path)
    path.write_text(badge_content)

def write_log(message, log_path):
    logpath = Path(log_path)
    logpath.parent.mkdir(parents=True, exist_ok=True)
    logpath.touch(exist_ok=True)

    print(message)

    with logpath.open("a") as f:
        f.write(f"{datetime.today()}: {message}\n")


def main():
    argument = parse_arguments()

    participants = read_participants(argument + "/teilnehmer.csv")

    template = read_template(argument + "/vorlage.txt")

    badgespath = argument + "/badges"
    Path(badgespath).mkdir(parents=True, exist_ok=True)

    i = 1

    for participant in participants:
        badge_id = generate_badge_id(participant["name"], i)
        i += 1
        badge = create_badge(template, participant, badge_id)
        save_badge(badge, badgespath + "/" + "badge_" + badge_id + ".txt")
        write_log((f'Badge erstellt: {badge_id} für {participant["name"]}'), argument + "/badge_log.txt")

    summary = f'Insgesamt {len(participants)} Badges erstellt.'
    print(summary)
    write_log(summary, argument + "/badge_log.txt")


help()
if __name__ == "__main__":
    main()