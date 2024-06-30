import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.'))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
else:
    print(scissors)

computer_input = random.randint(0,2)
print(computer_input)
if computer_input == 0:
    print(rock)
elif computer_input == 1:
    print(paper)
else:
    print(scissors)

# options: 0,0 1,1 2,2 --- 0,1 0,2 0,3 1,2 1,3 --- 2,3 --- 1,0 2,0 3,0 --- 1,2 1,3 --- 3,2 
if user_input == 0 and computer_input == 0:
    print('Game Draw!')
elif user_input == 1 and computer_input == 0:
    print('Rock has rapped by paper. You lose!')
elif user_input == 2 and computer_input == 0:
    print('Rock has broken the scissor. You lose!')
# elif user_input == 1 and computer_input ==