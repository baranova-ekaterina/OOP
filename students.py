class Student:
    student_ch = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_ch.append(self)
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
  
    def score_hw(self, lecturer, course, score):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.scores:
                lecturer.scores[course] += [score]
            else:
                lecturer.scores[course] = [score]
        else:
            return 'Ошибка'

    def av_grade(some_student, some_course):
        if isinstance(student, Student) and course in self.grades:
            for key, value in self.grades:
                av_gr = sum(value) / len(value)
            return av_gr
                

    def __str__(self):
        return  f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: () \nКурсы в процессе: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}\n'       

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lectors = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.scores = {}
        Lecturer.lectors.append(self)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: ()\n'
            

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
            
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n' 
        #res3 = (
            #f'Имя: {self.name} \n' 
             #'Фамилия: {self.surname}'
            #)
        #return res3
    
def av_grade(some_student, some_course):
    if isinstance(student_1, Student) and course in self.grades:
        for key, value in self.grades:
            av_gr = sum(value) / len(value)
        return av_gr
      
    #for key, value in Lecturer.scores.values():
        #av_gr = sum(value) / len(value)
    #return av_gr


student_1 = Student('Иван', 'Иванов', 'мужской')
student_1.courses_in_progress += ['Python', 'English']
student_1.finished_courses += ['Git']

student_2 = Student('Николай', 'Николаев', 'мужской')
student_2.courses_in_progress += ['Git', 'Python']
student_2.finished_courses += ['English']

mentor_1 = Reviewer('Пётр', 'Петров')
mentor_1.courses_attached += ['Python', 'Git']
mentor_2 = Reviewer('Анна', 'Мороз')
mentor_2.courses_attached += ['English']

mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Git', 10)
mentor_2.rate_hw(student_1, 'English', 7)

mentor_1.rate_hw(student_2, 'Python', 10)
mentor_1.rate_hw(student_2, 'Git', 8)
mentor_2.rate_hw(student_2, 'English', 5)

lector_1 = Lecturer('Игнат','Игнатов')
lector_1.courses_attached += ['Python', 'Git']
lector_2 = Lecturer('Василий', 'Васильев')
lector_2.courses_attached += ['English']

student_1.score_hw(lector_1, 'Python', 9)
student_1.score_hw(lector_1, 'Git', 10)
student_1.score_hw(lector_2, 'English', 10)
student_2.score_hw(lector_1, 'Python', 10)
student_2.score_hw(lector_1, 'Git', 8)
student_2.score_hw(lector_2, 'English', 5)

print(student_1.grades)
print(student_2.grades)

print(student_1)
print(student_2)

print(mentor_1)
print(mentor_2)

print(lector_1.scores)
print(lector_2.scores)

print(lector_1)
print(lector_2)

tap = av_grade(student_1, "Python")
print(tap)

#old_student = Student('Ruoy', 'Eman', 'male')
#old_student.courses_in_progress += ['Python']

#new_student = Student('Pam', 'Newman', 'female')
#new_student.courses_in_progress += ['English']
#new_student.finished_courses += ['Python']
 
#cool_mentor = Reviewer('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']
 
#cool_mentor.rate_hw(old_student, 'Python', 10)
#cool_mentor.rate_hw(old_student, 'Python', 10)
#cool_mentor.rate_hw(new_student, 'English', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#lector_1 = Lecture


#print(old_student.grades)
#print(new_student.grades)
#print(cool_mentor)
