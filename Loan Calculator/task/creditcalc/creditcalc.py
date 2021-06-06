import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="diff/annuity")
parser.add_argument("--principal", help="Loan principal amount")
parser.add_argument("--periods", help="number of periods")
parser.add_argument("--interest", help="loan interest")
parser.add_argument("--payment", help="monthly payment")
args = parser.parse_args()

if args.type and args.type in ["diff", "annuity"] and args.principal and args.periods and args.interest:
    if args.type == "diff":
        diff_payment_list = []
        P = float(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)
        for m in range(1, int(args.periods) + 1):
            diff_payment = math.ceil((P / n) + (i * (P - ((P * (m - 1))/n))))
            diff_payment_list.append(diff_payment)
            print("Month {}: payment is {}".format(m, diff_payment))
        print("")
        print("Overpayment = {}".format(sum(diff_payment_list) - P))
    else:
        P = float(args.principal)
        n = int(args.periods)
        i = float(args.interest) / (12 * 100)
        monthly_amount = math.ceil(P * ((i * math.pow(1 + i, n)) / ((math.pow(1 + i, n) - 1))))
        print("Your annuity payment = {}!".format(monthly_amount))
        print("Overpayment = {}".format((monthly_amount * n) - P))
elif args.type and args.type == "annuity" and args.payment and args.periods and args.interest:
    totals_no_of_months = float(args.periods)
    monthly_amount = int(args.payment)
    loan_interest = float(args.interest) / (12 * 100)
    loan_principal = math.floor(monthly_amount / ((loan_interest * math.pow(1 + loan_interest, totals_no_of_months)) / ((math.pow(1 + loan_interest, totals_no_of_months) - 1))))
    print("Your loan principal = {}!".format(loan_principal))
    print("Overpayment = {}".format((monthly_amount * totals_no_of_months) - loan_principal))
elif args.type and args.type == "annuity" and args.principal and args.payment and args.interest:
    loan_principal = float(args.principal)
    monthly_amount = float(args.payment)
    loan_interest = float(args.interest) / (12 * 100)
    totals_no_of_months = math.ceil(math.log((monthly_amount / (monthly_amount - (loan_interest * loan_principal))), 1 + loan_interest))
    no_of_years = int(totals_no_of_months // 12)
    no_of_months = totals_no_of_months % 12
    if no_of_years == 0:
        print("It will take {} months to repay this loan!".format(no_of_months))
    elif no_of_months == 0:
        print("It will take {} years to repay this loan!".format(no_of_years))
    else:
        print("It will take {} years and {} months to repay this loan!".format(no_of_years, math.ceil(no_of_months)))
    print("Overpayment = {}".format(int((totals_no_of_months * monthly_amount) - loan_principal)))
else:
    print("Incorrect parameters.")