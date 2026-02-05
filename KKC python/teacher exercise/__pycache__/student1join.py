from student1 import Student
rno=int(input("Enter your rno"))
name=input("Enter your name")
course=input("Enter your course")
assignment=int(input("Enter ur ass"))
exam=int(input("enter your exam"))
S2=Student(rno,name,course,assignment,exam)
S2.CalculatePassOrFail()
S2.show_info()
