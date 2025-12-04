# Day 2: While Loops

# Example 1: Reach corpus goal
print("\nHow many months to reach ₹1 crore?")
target = 10000000  # 1 crore
monthly_investment = 65000
annual_return = 0.15
monthly_return = annual_return / 12

corpus = 0
months = 0
while corpus < target:
    corpus = (corpus + monthly_investment) * (1 + monthly_return)
    months += 1

years = months / 12
print(f"Will take {months} months ({years:.1f} years) to reach ₹1 crore")

# Example 2: Emergency fund builder
print("\nBuilding ₹5 lakh emergency fund:")
emergency_fund = 0
target_emergency = 500000
monthly_savings = 20000  # separate from SIP
months_count = 0

while emergency_fund < target_emergency:
    emergency_fund += monthly_savings
    months_count += 1
    if months_count <= 12:  # Print first 12 months only
        print(f"Month {months_count}: ₹{emergency_fund:,.0f}")

print(f"\nEmergency fund complete in {months_count} months")

# Exercise 3: Risk management
# Create a variable: portfolio_value = 1000000
# Create a variable: risk_per_trade = 0.02 (2%)
# Calculate max loss per trade
# Use while loop to show how many trades you can lose before hitting 50% capital

# YOUR CODE HERE:
print("\nRisk management - max losing trades before 50% capital:")
portfolio_value = 1000000
risk_per_trade = 0.02  # 2%

max_loss_per_trade = portfolio_value * risk_per_trade
print(f"Max loss per trade: ₹{max_loss_per_trade:,.0f}")