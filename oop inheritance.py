# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


# Child Class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # calling parent constructor
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

    # Method Overriding
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old and I teach {self.subject}")


# Child Class: Student
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)   # calling parent constructor
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying in grade {self.grade}")

    # Method Overriding
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old and I study in grade {self.grade}")


# -------------------------
# Creating Objects
# -------------------------

t1 = Teacher("Ali", 35, "Mathematics")
s1 = Student("Sara", 16, "10th")

# Teacher actions
t1.introduce()
t1.teach()

print("-----")

# Student actions
s1.introduce()
s1.study()