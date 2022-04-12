'''
Student Info Search Using Dictionary

Write a program to store students info like admission number, role number, name and marks in a dictionary, admission numbers should be used as dictionary
keys. Display info on the basis of admission number obtained as user input.
'''

n = int(input("Enter number of students: "))
d = {}
for i in range(n):
    adm = int(input("Enter admission number: "))
    role = input("Enter role number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    d[adm] = [role, name, marks]



print()

adm = int(input("Enter admission number of student: "))

print("Role number: " + d[adm][0] + "\nName: " + d[adm][1] + "\nMarks: " + d[adm][2])
    
