
#Luan Nguyen

#June 17th 2023

# Using a while loop, create a list called L that contains the numbers 0 to 10. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.
L = []

i = 0

while i <=10:
    L.append(i)
    i += 1
print(L)