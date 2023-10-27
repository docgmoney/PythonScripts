print("Interest Loan Calculator")

# Variables
name = input("What is your name?: \n")
loan_amount = float(input("How much is the loan for?: \n"))
apr = float(input("What is the APR % on the loan?: \n"))
months = int(input("How many months is the loan for?: \n"))

# Calculations
interest_rate = apr / 100 / 12  # Monthly interest rate

# Monthly payment formula
monthly_payment = (loan_amount * interest_rate * (1 + interest_rate)**months) / ((1 + interest_rate)**months - 1)

# Output
print(name, "for a loan amount of $", "%.2f" % loan_amount, "with an APR of", "%.2f" % apr, "% over", months, "months. Your monthly payment will be approximately: $", "%.2f" % monthly_payment, "\n")

# Paying it Down
outstanding_balance = loan_amount
for month in range(1, months + 1):
    if outstanding_balance < monthly_payment:
        print("Month", month, "Payment required: $", "%.2f" % outstanding_balance, "This is the final payment.👑👑👑")
        outstanding_balance = 0
    else:
        print("Month", month, "Payment required: $", "%.2f" % monthly_payment)
        outstanding_balance -= monthly_payment
    if outstanding_balance == 0:
        break
