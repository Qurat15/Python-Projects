print("The Love Calculator is calculating your score...")
name1 = input('Enter name1: ') # What is your name?
name2 = input('Enter name2: ') # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e1 = lower_names.count('e')
first_digit = t + r + u + e1
# print(first_digit)

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e2 = lower_names.count('e')
second_digit = l + o + v + e2
# print(second_digit)

whole_digit = str(first_digit) + str(second_digit)
whole = int(whole_digit)

if whole < 10 or whole > 90:
  print(f'Your score is {whole}, you go together like coke and mentos.')
elif whole >= 40 and whole <=50:
  print(f'Your score is {whole}, you are alright together.')
else:
  print(f'Your score is {whole}.')