# Input a Python list of student heights
student_heights = input('Enter height of students by single space: ').split()
# print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height= 0
number_of_students = 0
average_height = 0

for i in range(0, len(student_heights)):
  total_height = total_height + student_heights[i]
print(f'total height = {total_height}')

for i in student_heights:
  number_of_students = number_of_students + 1
print(f'number of students = {number_of_students}')

average_height = total_height / number_of_students
print(f'average height = {round(average_height)}')
