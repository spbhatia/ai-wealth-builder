"""
Personal Investment Calculator
Calculates corpus, real returns, time to goal
"""

def calculate_sip_corpus(monthly_investment, years, annual_return):
    """Calculate SIP corpus using compound interest formula"""
    months = years * 12
    monthly_return = annual_return / 12
    corpus = monthly_investment * (((1 + monthly_return)**months - 1) / monthly_return) * (1 + monthly_return)
    return corpus

def calculate_time_to_goal(target, monthly_investment, annual_return):
    """Calculate months needed to reach target corpus"""
    monthly_return = annual_return / 12
    corpus = 0
    months = 0
    
    while corpus < target:
        corpus = (corpus + monthly_investment) * (1 + monthly_return)
        months += 1
    
    return months

def main():
    print("="*50)
    print("PERSONAL INVESTMENT CALCULATOR")
    print("="*50)
    
    # User inputs
    monthly_sip = 65000
    target_amount = 50000000  # 5 crore
    expected_return = 0.15  # 15%
    inflation_rate = 0.06  # 6%
    
    print(f"Monthly SIP: ₹{monthly_sip:,}")
    print(f"Target: ₹{target_amount:,}")
    print(f"Expected Return: {expected_return*100}%")
    print(f"Inflation: {inflation_rate*100}%")
    print("-"*50)
    
    # Calculate 5-year corpus
    corpus_5y = calculate_sip_corpus(monthly_sip, 5, expected_return)
    real_value_5y = corpus_5y * (1 - inflation_rate)**5
    
    print(f"5-Year Corpus (Nominal): ₹{corpus_5y:,.0f}")
    print(f"5-Year Corpus (Real value): ₹{real_value_5y:,.0f}")
    print(f"Shortfall from ₹5 crore: ₹{target_amount - corpus_5y:,.0f}")
    
    # Calculate time to reach 5 crore
    months_needed = calculate_time_to_goal(target_amount, monthly_sip, expected_return)
    years_needed = months_needed / 12
    
    print(f"\nTime to reach ₹5 crore: {months_needed} months ({years_needed:.1f} years)")
    
    # Sensitivity analysis
    print("\nSensitivity Analysis (different returns):")
    returns = [0.12, 0.15, 0.18, 0.20]
    for ret in returns:
        corpus = calculate_sip_corpus(monthly_sip, 5, ret)
        print(f"@{ret*100}%: ₹{corpus:,.0f}")

if __name__ == "__main__":
    main()
