# ------- Exercise: Who is going to pay for meal today? ------------------
import random
names = ['Tooba','Aini','Noor','Mashal']
# print(names)

numbers = len(names)
random_choice = random.randint(0, numbers-1)

print(f'{names[random_choice]} is going to buy the meal today!')