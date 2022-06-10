
class WrongGrade(BaseException) :
    pass


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __check_grades(self, marks) :
        self.marks = marks
        for grade in self.marks :
            if grade not in range(0, 11) or not isinstance(grade, int):
                raise WrongGrade("Grade must be in 1 - 10 range")
        return True
            
    def rate_lecturer(self, lector, course, *grade):
        if (self.__check_grades(grade) and isinstance(lector, Lecturer) and course in self.courses_in_progress 
            and course in lector.courses_attached):
            # print("OK")
            if course in lector.grades:
                lector.grades[course] += list(grade)
            else:
                lector.grades[course] = list(grade)
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        self.result = 0
        for key, value in self.grades.items() :
            if self.grades.get(key) != None:
                self.result += sum(self.grades.get(key)) / len(self.grades.get(key))
            else :
                self.result += "еще не было оценок"
        return self.result / len(self.grades.keys())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._get_average_grade()}\n"
                f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {" ".join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() == other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __ne__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() != other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __lt__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() < other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __gt__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() > other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __le__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() <= other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __ge__(self, other):
        if isinstance(other, Student) :
            return self._get_average_grade() >= other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"


class Mentor:
    """Parent class for Lecturer and Reviewer"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor) :
    """Someone who gives lecture"""
    def __init__(self, name, surname) :
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_grade(self):
        self.result = 0
        for key, value in self.grades.items() :
            if self.grades.get(key) != None:
                self.result += sum(self.grades.get(key)) / len(self.grades.get(key))
            else :
                self.result += "еще не было оценок"
        return self.result / len(self.grades.keys())

    def __str__(self):
        return(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_average_grade()}")

    def __eq__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() == other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __ne__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() != other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __lt__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() < other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __gt__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() > other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __le__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() <= other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"

    def __ge__(self, other):
        if isinstance(other, Lecturer) :
            return self._get_average_grade() >= other._get_average_grade()
        else :
            return "Нельзя сравнивать объекты разных классов!"


class Reviewer(Mentor) :
    """Someone who checks Homework"""
    def __check_grades(self, marks) :
        self.marks = marks
        for grade in self.marks :
            if grade not in range(0, 11) or not isinstance(grade, int):
                raise WrongGrade("Grade must be in 1 - 10 range")
        return True

    def rate_hw(self, student, course, *grade):
        if (self.__check_grades(grade) and isinstance(student, Student) 
            and course in self.courses_attached and course in student.courses_in_progress) :
            if course in student.grades:
                student.grades[course] += list(grade)
            else:
                student.grades[course] = list(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return(f"Имя: {self.name}\nФамилия: {self.surname}")




if __name__ == "__main__" :
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['Git']
 
    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.courses_attached += ['Python']
    cool_reviewer.courses_attached += ['Git']

    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.courses_attached += ['Python']
    cool_lecturer.courses_attached += ['Git']
    # print(cool_lecturer.grades)
 
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Git', 10)
    cool_reviewer.rate_hw(best_student, 'Git', 9)
    cool_reviewer.rate_hw(best_student, 'Git', 8)
 
    # print(best_student.name, best_student.grades)


    best_student.rate_lecturer(cool_lecturer, 'Python', 10, 10, 10)
    best_student.rate_lecturer(cool_lecturer, 'Git', 9, 9, 9)
    # print(cool_lecturer.name, cool_lecturer.grades)
    # print()
    # print(best_student)
    # print()
    # print(cool_lecturer)
    # print()
    # print(cool_reviewer)


    worst_student = Student('Ivan', 'Ivan', 'Man')
    worst_student.courses_in_progress += ['Python']
    worst_student.courses_in_progress += ['Git']

    worst_lecturer = Lecturer('Qwe', 'Rty')
    worst_lecturer.courses_attached += ['Python']
    worst_lecturer.courses_attached += ['Git']


    cool_reviewer.rate_hw(worst_student, 'Python', 5)
    cool_reviewer.rate_hw(worst_student, 'Python', 6)
    cool_reviewer.rate_hw(worst_student, 'Python', 7)
    cool_reviewer.rate_hw(worst_student, 'Git', 2)
    cool_reviewer.rate_hw(worst_student, 'Git', 3)
    cool_reviewer.rate_hw(worst_student, 'Git', 4)

    worst_student.rate_lecturer(worst_lecturer, 'Python', 5, 5, 5)
    worst_student.rate_lecturer(worst_lecturer, 'Git', 6, 6, 6)
    
    # print()
    # print(worst_student)
    # print()
    # print(worst_lecturer)
    # print()


    print(worst_student > best_student)
    print(worst_student != best_student)
    print(worst_student < best_student)
    print()
    print(worst_lecturer > cool_lecturer)
    print(worst_lecturer != cool_lecturer)
    print(worst_lecturer < cool_lecturer)
    print()
    print(worst_student == cool_lecturer)
    print(best_student > worst_lecturer)

