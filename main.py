class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached =[]

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

#возможность выставлять лекторам оценки за курс
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегрузите магический метод __str__ у всех классов.
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average_in_course} \nЗавершенные курсы: {self.finished_courses} "


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.courses_in_progress =[]

    def __str__(self):
        return self.__name

# Перегрузите магический метод __str__ у всех классов.
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

#наследование классов Reviewer (эксперты, проверяющие домашние задания).
class Reviewer(Mentor):

    # возможность выставлять оценки студентам за курс
    def rate_hw(self, student, courses, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#наследование классов Lecturer (лекторы)
class Lecturer(Mentor):
    finished_courses = []
    courses_in_progress = []
    grades = {}
    courses_attached = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

#Перегрузите магический метод __str__ у всех классов.
def __str__(self):
    result = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lecturer}"
    return result

#олевые испытания
#экземпляр класса student и вызов функции оценки лекторов и средней оценки за дз

Ruoy_Eman = Student('name', 'surname','gender')
Ruoy_Eman.rate_lecturer('lecturer', 'course','grade')
Ruoy_Eman.average_in_course()


# средняя оценка лекторов
def average_lecturer(self):
    list_average_lecturer = []
    for grade in self.average_lecturer.values():
        for x in grade:
            list_average_lecturer.append(x)
    average_lecturer = round(sum(list_average_lecturer) / len(list_average_lecturer, 2))
    return average_lecturer
print(f'Средняя оценка {list_average_lecturer } за курс {course_id}: {average_lecturer}')

#экземпляр класса лектор

some_lecturer = Lecturer()
some_lecturer.average_lecturer()

#экземпляр класса проверяющий и вызов функции оценки студентов

some_reviewer = Reviewer()
def average_in_course(course_id, student_in_course):
    student_in_course = []
    all_rates_in_course = []
    for student in student_in_course:
        if course_id in student.courses_in_progress + student.finished_courses:
            student_in_course.append(student)
            all_rates_in_course += student.grades[course_id]
    if student_in_course == []:
        print(f'Студенты {student_list} не проходили курс {course_id}')
    elif len(all_rates_in_course) != 0:
        res = sum(all_rates_in_course) / len(all_rates_in_course)
    else:
        res = 0
    return res
    print(f'Средняя оценка студентов {student_in_course} за курс {course_id}: {res}')



some_reviewer.rate_hw()

course = ['Python', 'Git']
grades ={}
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']

best_lecturer = Lecturer('Some', 'Buddy')

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_reviewer = Reviewer

cool_reviewer.rate_hw(best_student,course,grades)
cool_reviewer.rate_hw(best_student,course,grades)
cool_reviewer.rate_hw(best_student,course,grades)

print(best_student.grades)
#возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

def __lt__(self, other):
  if not isinstance(other, Lecturer):
    print('Not a Lecturer')
  return
return self.lecturer < other.lecturer

def __str__(self):
    res = f'Средняя оценка  = {average_lecturer}'

def __lt__(self, other):
  if not isinstance(other, Student):
    print('Not a Student')
  return
    return self.student < other.student

# def __str__(self):
#     res = f'Средняя оценка  = {average_in_course}'
#     return res

best_student = Student ()
average_in_course = Student()
best_lecturer = Lecturer()
average_lecturer = Lecturer

print(best_student > average_in_course)
print(best_lecturer > average_lecturer)
print()
