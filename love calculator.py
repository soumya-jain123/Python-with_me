def calculate_love_percentage(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    common_letters = set(name1) & set(name2)
    common_count = len(common_letters)

    total_length = len(name1) + len(name2)
    love_percentage = (common_count/total_length) * 100

    return love_percentage

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = calculate_love_percentage(name1,name2)
print(f"The love percentage between {name1} and {name2} is {result}%.")