def is_number_between_1_and_10(number):
    if number >= 1 and number <= 10:
        return True
    else:
        return False
number_1 = int(input("Enter the number 1: "))
number_2 = int(input("Enter the number 2: "))

result = is_number_between_1_and_10(number_1)
print(result)  # Output: True

result = is_number_between_1_and_10(number_2)
print(result)  # Output: False
