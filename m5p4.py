#Luan Nguyen

#May 11th 2023

#Modulus (%)
for i in range(1, 51):

    if  i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 5 == 0:
        print("Divisible by 5" )
    elif i % 3 == 0:
        print("Divisible by 3")
    else:
        print(i)

