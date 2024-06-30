line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ['a','b','c']

# To find index 
letter_index = abc.index(letter)       # here, whatever letter user enter, we will use that letter and will finds its index in list abc and will store it in variable
number_index = int(position[1])- 1  # bcz indexing starts from 0 so, here if user enter 3 as number we will minus it from 1 and result is 2
map[number_index][letter_index] = 'X'   # here we first write number(e.g; 3) and then we write letter(e.g; B)


# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"


print(f"{line1}\n{line2}\n{line3}")