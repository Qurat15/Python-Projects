import random

random_int = random.randint(0,10)
# print(random_int)

random_float = random.random()
# print(random_float)

r = float(random.randint(0,5))
print(r)

# ------------ Exercise -------------------------

import random
num = random.randint(0,1)
# print(num)
if num == 1:
  print('Heads')
else:
  print('Tails')