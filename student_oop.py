class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum / len(self.students)

s1 = Student("Burak", 25, 89)
s2 = Student("Ozge", 26, 90)
s3 = Student("Hamza", 30, 70)

course = Course("Physics", 3)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

for student in course.students:
    print(f'student:{student.name}, grade:{student.grade}')


print(f'average: {course.get_average_grade()}')