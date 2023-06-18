#Luan Nguyen

#June 17th 2023

#  Write a function that takes a list and prints if the value 5 is in that list

import random
def randomlist(lst):
    if 5 in lst:
        print("The value 5 is present in the list.")
    else:
        print("The value 5 is not present in the list.")

#random list of numbers from 1 to 10
random_list = random.sample(range(1, 11), 6)
print(random_list)

randomlist(random_list)
