# Day 2: Lists (most important data structure)

# Example 1: Portfolio tracking
portfolio = ["Nifty 50", "Midcap", "Smallcap", "Emergency Fund", "Gold"]
print("My portfolio:", portfolio)

# Example 2: SIP amounts
sip_amounts = [30000, 20000, 10000, 5000]  # Matching portfolio
print("SIP amounts:", sip_amounts)

# Example 3: Accessing elements
print("Largest SIP:", sip_amounts[0])  # Index 0 = first element
print("Total SIP:", sum(sip_amounts))

# Example 4: Modifying list
sip_amounts.append(15000)  # Add new investment
print("After adding new SIP:", sip_amounts)

# Example 5: Loop through portfolio with amounts
print("\nComplete portfolio breakdown:")
for i in range(len(portfolio)):
    print(f"{portfolio[i]}: ₹{sip_amounts[i]:,}/month")

# Exercise 4: Returns calculation
# Create list: annual_returns = [12.5, 15.2, 18.7, 6.0]  # % returns
# Calculate weighted average return based on sip_amounts
# Hint: Weighted return = Σ(return * amount) / Σ(amount)

# YOUR CODE HERE:
annual_returns = [12.5, 15.2, 18.7, 6.0]  # % returns
total_investment = sum(sip_amounts)
weighted_return = sum((ret / 100) * amt for ret, amt in zip(annual_returns, sip_amounts)) / total_investment * 100
print(f"\nWeighted average return of portfolio: {weighted_return:.2f}%")

# Example 6: List comprehension (powerful Python feature)
print("\nProjected corpus for each fund in 5 years @ different returns:")
returns = [0.12, 0.15, 0.18, 0.06]  # Different returns for each fund
corpus_projection = [sip * 12 * 5 * (1 + ret)**5 for sip, ret in zip(sip_amounts, returns)]
for fund, corpus in zip(portfolio, corpus_projection):
    print(f"{fund}: ₹{corpus:,.0f}")
