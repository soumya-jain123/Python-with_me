'''Write the code to give the BMI of the indvidual person
BMI = weight(kg)/(height(m))**2(m^2)
'''

weight = float(input("Enter the weight of the person in (kg): "))
height = float(input("Enter the height of indvidual in (cm): "))

if height == 0 or height < 0:
    print("Enter height greater than 0 !!!. ")
else:
    #to change the height into (m) from (cm)

    height = height / 100

    print(f"Height in (m): {height}(m)")

    bmi = weight / (height)**2

    print(f"BMI of individual: {bmi}")