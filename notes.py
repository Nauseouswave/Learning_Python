# Python notes

# Numbers can have underscores and still be readable by python

# Example:

# Number has underscores and can still be used in math
SOL_Balance = 1_250_000

SOL_Price = 0.0547

SOL_Value = SOL_Balance * SOL_Price

print("SOL Value = $" + str(SOL_Value))

# The same but with BTC
BTC_Balance = 0.00567

BTC_Price = 45_500

BTC_Value = BTC_Balance * BTC_Price
print("BTC Value = $" + str(BTC_Value))

net_worth = SOL_Value + BTC_Value

print("Net worth = $" + str(net_worth))
