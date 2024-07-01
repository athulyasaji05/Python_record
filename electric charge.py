def calculate_electricity_bill(units):
    if units <= 200:
        amount = units * 0.50
    elif units <= 400:
        amount = 100 + (units - 200) * 0.65
    elif units <= 600:
        amount = 230 + (units - 400) * 0.80
    else:
        amount = 390 + (units - 600)
        
    if amount > 400:
        surcharge = 0.15 * amount
        amount += surcharge
        
    amount = max(amount, 100)
    return amount

def main():
    try:
        units_consumed = float(input("Enter the consumption units: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    total_bill = calculate_electricity_bill(units_consumed)
    print(f"Electricity Bill: Rs. {total_bill:.2f}")

if __name__ == "__main__":
    main()
