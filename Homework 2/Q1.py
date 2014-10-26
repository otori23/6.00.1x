# Write a program to calculate the credit card balance after one year if a 
# person only pays the minimum monthly payment required by the credit card 
# company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining 
# balance, and print to screen something of the format:

# Month: 1
# Minimum monthly payment: 96.0
# Remaining balance: 4784.0

# Math is:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + 
# (Monthly interest rate x Monthly unpaid balance)

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0;
monthlyInterestRate= annualInterestRate / 12.0

for i in range(1, 13):
    print("Month: " + str(i))
    
    minMonthlyPayment = monthlyPaymentRate*balance
    totalPaid += minMonthlyPayment
    print("Minimum monthly payment: " + str(round(balance*monthlyPaymentRate, 2)))
    
    monthlyUnpaidBalance = balance-minMonthlyPayment
    balance = monthlyUnpaidBalance  + (monthlyInterestRate*monthlyUnpaidBalance)
    print("Remaining balance: " + str(round(balance, 2)))
    
print("Total paid: " + str(round(totalPaid, 2)))
print("Remaining balance: " + str(round(balance, 2)))