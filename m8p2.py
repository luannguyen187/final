
#Luan Nguyen

#June 17th 2023

# Write a function that takes two inputs from a user and prints whether the sum is
# greater than 10, less than 10, or equal to 10.
def compare():
    number_1 = float(input("Enter the number 1: "))
    number_2 = float(input("Enter the number 2: "))

    # Calculate the sum of the inputs
    sum = number_1 + number_2
    print("the sum is: ", sum)

    if sum > 10:
        print("The sum is greater than 10.")
    elif sum < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

compare()
