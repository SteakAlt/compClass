'''
Student Info Search Using Dictionary

Write a program to store students info like admission number, role number, name and marks in a dictionary, admission numbers should be used as dictionary
keys. Display info on the basis of admission number obtained as user input.
'''

d = {1 : ['01', 'Jay', '90'], 2 : ['02', 'Jaeden', '95']}

adm = int(input("Enter admission number: "))
l = d[adm]

print("Role number: " + l[0] + "\nName: " + l[1] + "\nMarks: " + l[2])
