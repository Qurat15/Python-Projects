print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip_amount = int(input("How much tip would you like to give? 10,12 or 15%: "))
tip_total = (tip_amount/100)*total_bill

num_of_people = int(input("How many people to split the bill?"))
amount_by_each_person = ((total_bill + tip_total)/num_of_people)

amount = "{:.2f}".format(amount_by_each_person)

print(f"Each person should pay: ${amount}")


