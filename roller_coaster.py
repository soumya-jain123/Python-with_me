def calculate_ride_cost(height, age):
    base_cost = 10

    if height >= 150:
        base_cost += 20
    
    if age<=12:
        base_cost -= 5
    elif 45<=age<=55:
        base_cost *= 0.8

    return base_cost

height = float(input("Enter the height of the person (in cm): "))
age = int(input("Enter the age of the person: "))

ride_cost = calculate_ride_cost(height,age)
print(f"the total cost for your ride is: {ride_cost}")