class Student:
    def __init__(self,rno,name,course,assignment,exam):
        self.rno=rno
        self.name=name
        self.course=course
        self.assignment=assignment
        self.exam=exam
        self.result=""

    def CalculatePassOrFail(self):
        if self.assignment+self.exam>=50:
            self.result="pass"
        else:
            self.result="Fail"

    def show_info(self):
        print(f"{self.rno} is {self.name} and {self.result}")
