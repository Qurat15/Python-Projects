print('''              ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    ****************************************************************
''')

print("Welcome to the Treasure House.")
print('Your goal is to find the treasure.')

print('You are at the door of this house.Where do you want to go? Type "left" or "right": ')
home_entry = input().lower()

if home_entry == 'left':
    print('You come to a room. There are two boxes. Which box do you want to open? "box1", "box2", "box3": ')
    leftentery = input().lower()
    
    if leftentery == 'box1':
        print('Snake has come out of the box.It has bitten you. Game Over.')
    elif leftentery == 'box2':
        print('This box is full of jewels and diamonds. You Win!')
    elif leftentery == 'box3':
        print('This box is empty. Game Over.')

else:
    print('You have fill in a pit.Game Over. ')