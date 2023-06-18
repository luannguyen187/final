#Luan Nguyen

#June 17th 2023

#Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens. Confirm the list results using a print statement.

i = 0

divide_by_ten = []

while i <= 50:
    if i % 10 == 0:
        divide_by_ten.append(i)
    i += 1

print("Number divide by 10", divide_by_ten)