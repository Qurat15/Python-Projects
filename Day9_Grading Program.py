'''
--------------------------------- Question -------------------------------------
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.


This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail" 

'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.

student_grades = student_scores
for key in student_grades:
  if student_grades[key] <= 70:
    student_grades[key] = 'Fail'
  elif student_grades[key] > 70 and student_grades[key] <= 80:
    student_grades[key] = 'Acceptable'
  elif student_grades[key] > 80 and student_grades[key] <= 90:
    student_grades[key] = 'Exceeds Expectations'
  else:
    student_grades[key] = 'Outstanding'
    
print(student_grades)