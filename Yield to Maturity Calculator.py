print('''
Yield to Maturity Calculator
============================
''')
restart = "y"
def yield_maturity():
    face_value = input("Enter the face value of the bond: ")
    face_value = float(face_value)
    market_value = input("Enter the current market value: ")
    market_value = float(market_value)
    term_left = input ("enter the years left: ")
    term_left = float(term_left)
    coupon_interest = input("enter the coupon interest(% amount out of the face value): ")
    coupon_interest = float(coupon_interest)
    
    print('''
    This is your yield to maturity, move the decimal point two places to the right for the %:
    ''')
    print(((face_value - market_value)/term_left + coupon_interest)/((face_value + market_value)/2))
while restart == "y":
    yield_maturity()
    continue_question = input('''
    Do you want to continue? Y/N: ''').lower()
    restart = continue_question
    if restart == "y":
     continue
else:
    print('''
            Goodbye!''')