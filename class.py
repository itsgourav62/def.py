#Write a Python class named Student with two attributes name,marks.
# Modify the attribute values of the said class and print the said attributes.

class Student:
    student_name = 'Bully Maguire'
    marks = 99  
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Bruce Wayne')
setattr(Student, 'marks', 100) 
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
