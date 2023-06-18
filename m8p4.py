#Luan Nguyen

#June 17th 2023

#
def leap_year(year):
    if (year % 4 == 0 and  year % 100 == 0) or( year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
leapyear = leap_year(year)
print(leapyear)


