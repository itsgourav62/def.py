#Write a Python class named Student with two instances student1,student2 and assign given values to the said instances attributes. Print
#all the attributes of student1, student2 instances with their values in the given format.

class Student:
    school = 'School of Life'
    address = '22/B Baker street, MANHATTAN' 
student1 = Student()
student2 = Student() 
student1.student_name = "John Wick"
student1.student_id = "19"
student1.English = 88
student1.Math = 90

student2.student_name = "Tony Montana"
student2.student_id = "22"
student2.English = 99
student2.Math = 90
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
