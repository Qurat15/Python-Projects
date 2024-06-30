height = int(input("Enter your height: "))
age = int(input("Enter your age: "))

if height >= 120:
    print("You can take RollarCoaster ride.")
    if age < 12:
        bill = 5
        print("You have to pay $5.")

    elif age >= 12 and age < 18:
        bill = 7
        print("You have to pay $7.")
    
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can take free ride.")
        
    else:
        bill = 12
        print("You have to pay $12.")

    wantPhoto = input("Do you want photo while taking the ride? Type Y for Yes, N for No.")
    if wantPhoto == 'Y':
        bill = bill + 3
    print(f"You final bill is ${bill}")
    
else:
    print("You cannot take RollarCoaster. You have to grow taller.")