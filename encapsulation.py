class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def setMarks(self, marks):
        self.__marks += marks

    def result(self):
        if self.__marks >= 40:
            return "pass"
        else:
            return "fail"

    def getMarks(self):
        return self.__marks


s1 = Student("Usman", 80)
s2 = Student("Zain", 40)

s1.setMarks(10)
s2.setMarks(5)

print(s1.getMarks())
print(s1.result())

print("___________________")

print(s2.getMarks())
print(s2.result())