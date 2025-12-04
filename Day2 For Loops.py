# Day 2: For Loops

# Example 1: Loop through investment years
print("Year-by-year corpus projection @ 15% CAGR:")
monthly_investment = 65000
annual_return = 0.15

for year in range(1, 6):  # 1 to 5
    months = year * 12
    monthly_return = annual_return / 12
    corpus = monthly_investment * (((1 + monthly_return)**months - 1) / monthly_return) * (1 + monthly_return)
    print(f"Year {year}: ₹{corpus:,.0f}")

# Example 2: Loop through mutual fund portfolio
print("\nTop 5 Nifty 50 companies:")
nifty50_top5 = ["Reliance", "TCS", "HDFC Bank", "ICICI Bank", "Infosys"]

for company in nifty50_top5:
    print(f"- {company}")

# Example 3: Loop with index (enumerate)
print("\nCompany rankings:")
for index, company in enumerate(nifty50_top5, 1):
    print(f"{index}. {company}")

# Exercise 2: Calculate SIP for different amounts
# Create a list: sip_amounts = [50000, 60000, 70000, 80000]
# Loop through each amount and calculate 5-year corpus @ 15%
# Print: "SIP of ₹X/month grows to ₹Y in 5 years"

# YOUR CODE HERE:

sip_amounts = [50000, 60000, 70000, 80000]
print("\nSIP corpus projections for different amounts @ 15% CAGR:")
annual_return = 0.15
for sip in sip_amounts:
    months = 5 * 12
    monthly_return = annual_return / 12
    corpus = sip * (((1 + monthly_return)**months - 1) / monthly_return) * (1 + monthly_return)
    print(f"SIP of ₹{sip}/month grows to ₹{corpus:,.0f} in 5 years")


# Example 4: Nested loops (investment + inflation)
print("\nCorpus with 6% inflation adjustment:")
inflation_rate = 0.06
for year in range(1, 6):
    months = year * 12
    corpus = monthly_investment * (((1 + monthly_return)**months - 1) / monthly_return) * (1 + monthly_return)
    inflation_factor = (1 - inflation_rate)**year
    real_value = corpus * inflation_factor
    print(f"Year {year}: Nominal ₹{corpus:,.0f} | Real value ₹{real_value:,.0f}")
