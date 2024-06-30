# Which year do you want to check?
year = int(input("Enter the year: "))


# check if it is leap year
# Note: leap year should be divisible by 0 and 400 with no remainder, and also its remainder should not equal to 0 if we divide it by 100
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("Leap year")
else:
  print("Not leap year")