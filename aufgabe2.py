import argparse

unit = {'CHF' : 1,
        'EUR' : 0.89}
def calculate(args):
    start_curency = args.from_unit
    if  start_curency not in unit:
        print("ERROR false unit")
    elif args.to_unit not in unit:
        print("ERROR true unit")
    else:
        curency_amount = args.amount / unit[start_curency]
        result = curency_amount * unit[args.to_unit]
        print(args.amount)
        print(result)






def main():
    parser = argparse.ArgumentParser(description='Simple Example')

    parser.add_argument('-a' , '--amount', type = float, default = 1, help = 'Amount')
    parser.add_argument('-f', '--from_unit', type = str , help='Second argument')
    parser.add_argument('-t', '--to_unit', type = str , help='Third argument')
    args = parser.parse_args()
    calculate(args)










if __name__ == '__main__':
    main()