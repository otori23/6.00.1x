balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = (annualInterestRate) / 12.0
lo = balance / 12.0
hi = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = (hi + lo) / 2.0
epsilon = 0.01

def TestMinPayment(balance, guess):
    for month in range(1, 13):
        monthlyUnpaidBalance = balance - guess
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return balance
    
while(True):
    balanceLeft = TestMinPayment(balance, guess)
    if(abs(balanceLeft) < epsilon):
        break
    elif(balanceLeft > 0):
        lo = guess
    else:
        hi = guess
    guess = (hi + lo) / 2.0
    
print("Lowest Payment: " + str(round(guess, 2)))