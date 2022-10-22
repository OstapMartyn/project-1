class Student:
    def __init__(self, name, surname, age, group):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.marks = marks
        self.money = money
    def info(self):
        print(f"Student {self.name} {self.surname}")

    def average(self):
        result = sum(self.marks) / len(self.marks)

    def info(self):
        print(f"Student {self.name} {self.surname}")

    def to_chill(self):
        pass

student1 = Student(
    "Oleg",
    "Bobko",
    24,
    "F18",
    [9, 7, 2, 7, 12]

)
student2 = Student(
    "Igor",
    "Vovk",
    28,
    "F13",
    [9, 12, 7, 12, 12, 5]
)
student1.info()
student2.info()
print(student1.average())
print(student2.average())