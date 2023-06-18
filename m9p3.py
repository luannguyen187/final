#Luan Nguyen

#June 17th 2023

# Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100

list_number = []
total = 0

while total <= 100:
    number = int(input("Enter the number: "))
    list_number.append(number)
    total = sum(list_number)
print("list of number:", number)
print("Sum is :", total)
