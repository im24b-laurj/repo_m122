import os
from datetime import date
import datetime
import argparse
from time import strptime
from datetime import datetime
import sys

created = {
    "message.log" : date(2025, 1, 10),
    "message20240210.log": date(2024, 12,15),
    "message20230520.log": date(2024,12,20),
    "message20240404.log": date(2024,12,8),
    "message20240605.log": date(2024,8,8)}

def main():

    days = sys.argv[1]
    saved = sys.argv[2]

    check_date(days)
    check_saved(saved, "C:\logs")
    print(created)






def check_date(days):
    log_date = created["message.log"]
    curent_days = date.today() - log_date
    if curent_days.days > int(days):
        log_date_string = log_date.strftime("%Y%m%d")
        created.update({
            "message" + log_date_string + ".log" : log_date
        })
        created["message.log"] = date.today()







list_values = []

def check_saved(saved, log_dir):
    # Exclude 'message.log' from sorting, because it's always kept
    historical_logs = {k: v for k, v in created.items() if k != "message.log"}

    # Sort historical logs by date descending
    sorted_keys = sorted(historical_logs, key=lambda k: historical_logs[k], reverse=True)


    keys_to_keep = set(sorted_keys[:int(saved)])


    keys_to_keep.add("message.log")


    for k in list(created):
        if k not in keys_to_keep:
            log_file_path = os.path.join(log_dir, k)
            if os.path.exists(log_file_path):
                try:
                    os.remove(log_file_path)
                    print(f"Deleted file: {log_file_path}")
                except PermissionError:
                    print(f"Cannot delete file (in use?): {log_file_path}")
            created.pop(k)



if __name__ == "__main__":
    main()
