print("Welcome to my PIZZA HUB!!!!")
def your_pizza_order():
    choice = input("Are you veg(V) or non-veg(NV): ")
    if choice == 'v' or choice == 'V':
        print("\nMENU\n")
        print('''1. MARGHERITA PIZZA
            Small = 159/-
            Medium = 259/-
            Large = 369/-
      
        2. VEG DELIGHT PIZZA
            Small = 199/-
            Medium = 368/-
            Large = 518/-
            
        3. VEGGIES FEAST PIZZA
            Small = 199/-
            Medium = 368/-
            Large = 518/-
        
        4. SPICY PANEER PIZZA
            Small = 299/-
            Medium = 518/-
            Large = 718/-
      ''' )
        pizza = input("Your order please(pizza): ")
        size = input("Enter the desired size accordingly('S','M','L'): ")
    else:
        print("/nMenu/n")
        print('''
                1. BULLS EYE(Egg, corn with pepper and jalapenos)
                    Small = 239/-
                    Large = 449/-
                2. PEPPER CHICKEN(Chicken marinated in pepper and garlic)
                    Small = 239/-
                    Large = 449/-
                3. THE SAILOR MAN(Mixed seafood(Prawn and Fish))
                    Small = 239/-
                    Large = 449/-''') 
        pizza = input("Your order please(pizza): ")
        size = input("Enter the desired size accordingly('S','M','L'): ")
    print("""Do you want any additional toppings:
            1. Extra cheese = 49/-
            2. Extra meat = 79/-
            3. Spicy = 99/-
            4. extra oregano = 39/-""")
    toppings = input("What's your option for additional toppings: ")
    total_prize = total_bill_amount(pizza, size, toppings)

    return print(f"Your total is: {total_prize}")

def total_bill_amount(pizza, size, topping):
    bill = 0
    if pizza == "MARGHERITA PIZZA":
        if size == 'S':
            bill = 159
        elif size == 'M':
            bill = 259
        elif size == 'L':
            bill = 369
    elif pizza == "VEG DELIGHT PIZZA":
        if size == 'S':
            bill = 199
        elif size == 'M':
            bill = 368
        elif size == 'L':
            bill = 518
    elif pizza == 'VEGGIES FEAST PIZZA':
        if size == 'S':
            bill = 199
        elif size == 'M':
            bill = 368
        elif size == 'L':
            bill = 518
    elif pizza == 'SPICY PANEER PIZZA':
        if size == 'S':
            bill = 299
        elif size == 'M':
            bill = 518
        elif size == 'L':
            bill = 718
    elif pizza == 'BULLS EYE':
        if size == 'S':
            bill == 239
        elif size == 'L':
            bill == 449
    elif pizza == 'PEPPER CHICKEN':
        if size == 'S':
            bill = 239
        elif size == 'L':
            bill = 449
    elif pizza == 'THE SAILOR MAN':
        if size == 'S':
            bill = 239
        elif size == 'L':
            bill = 449
    
    #FOR my toppings 
    if topping == 'Extra cheese':
        bill += 49
    elif topping == 'Extra meat':
        bill += 79
    elif topping == 'Spicy':
        bill += 99
    elif topping == 'Extra oregano':
        bill += 39
    else:
        bill += 0
    
    print("Do you have any referal code or and discount coupon ")
    if_coupon= input("Yes or No: ")
    if if_coupon == 'Yes':
        coupon = input ("Enter the coupon code: ")
        print("Coupon successuly applied!!!\n")
        bill *= 0.8 # fixing discount of 20%
        return bill
    else:
        return bill

    
your_pizza_order()