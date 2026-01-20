import sys
import argparse
from datetime import datetime
from datetime import date

print("22")
ISO_FMT = "%Y-%m-%d"
SWISS_FMT = "%d.%m.%Y"


def get_quarter(month_value: int):
    if month_value in (1,2,3 ):
        return "Quarter 1"
    elif month_value in range(4, 6):
        return "Quarter 2"
    elif month_value in range(7, 9):
        return "Quarter 3"
    elif month_value in range(10, 12):
        return "Quarter 4"




def parse_datetime(value: str):
    if len(sys.argv) < 1:
        return date.today
    else:

        for fmt in (ISO_FMT, SWISS_FMT):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                print("Falsches Formats")




def process():
    date_value1 = parse_datetime(sys.argv[1])
    quarter = get_quarter(date_value1.month)
    print("This month is " + quarter)



if __name__ == "__main__":
    process()