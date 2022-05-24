def affordability(total_money,price):
    affordability=total_money//price
    change=total_money%price
    return "number of bars that can be bought: %f, change left over: %f."%(affordability,change)

#Test the function
total_money=100000
price=5.99
print(affordability(total_money, price))

#Outcome: number of bars that can be bought: 16694.000000, change left over: 2.940000.