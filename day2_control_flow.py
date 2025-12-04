# Day 2: Control Flow - If/Else Statements

# Example 1: Basic if/else
age = 25
if age >= 18:
    print("You are eligible to invest in mutual funds")
else:
    print("You need to be 18+ to invest")

# Example 2: Investment decision based on risk
risk_appetite = "high"  # Change this to "medium" or "low"

if risk_appetite == "high":
    equity_allocation = 80
    debt_allocation = 20
elif risk_appetite == "medium":
    equity_allocation = 60
    debt_allocation = 40
else:  # low risk
    equity_allocation = 30
    debt_allocation = 70

print(f"Equity: {equity_allocation}%, Debt: {debt_allocation}%")

# Exercise 1: SIP amount checker
monthly_sip = 65000

# Write code to check:
# If monthly_sip >= 50000, print "Great! You're on track"
# If 30000 <= monthly_sip < 50000, print "Good start, try to increase"
# If monthly_sip < 30000, print "Consider increasing your SIP"

# YOUR CODE HERE:

if monthly_sip >= 50000:
    print("Great! You're on track")
elif monthly_sip >= 30000 and monthly_sip < 50000:
    print("Good start, try to increase")
elif monthly_sip < 30000:
    print("Consider increasing your SIP")

# Example 3: Fund selection based on amount
investment_amount = 10000

if investment_amount >= 5000:
    print("Eligible for Nifty 50 Index Fund")
    if investment_amount >= 10000:
        print("Also eligible for Midcap Fund")
else:
    print("Minimum SIP amount is ₹5000")
