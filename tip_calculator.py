'''WAP to form the tip calculator'''

def calculate_tip (bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage/100)
    total_amount = bill_amount + tip
    return tip, total_amount

def main():
    try:
        bill_amount = float(input("Enter the bill amount: Rs."))
        tip_percentage = float(input("Enter the tip percentage you want to give: "))

        tip, total_amount = calculate_tip(bill_amount, tip_percentage)

        print(f"Tip amount: Rs.{tip}")
        print(f"Total Amount (including tip): Rs.{total_amount}")

    except ValueError:
        print("Invalid input. Please enter valid numerical values only.")

main()