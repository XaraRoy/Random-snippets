
laptop_price = 2400
balance = laptop_price
months_to_repay = 6
interest = 0
monthly_payment = laptop_price / months_to_repay
while months_to_repay >= 1:
    balance = balance - monthly_payment + balance * interest / 100
    monthly_payment = balance / months_to_repay
    months_to_repay = months_to_repay - 1
    print("there are " + str(months_to_repay) +"monthly payments remaining, and a balance of " + str(balance) + "remaining. The monthly payment is " + str(monthly_payment) )
