class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = ['Python', 'Git']
        self.grades = {}
    
    def rate_lec(self, lectorer, course, grade):
        if isinstance(lectorer, Lectorer) and course in self.courses_in_progress and course in lectorer.courses_attached:
            if course in lectorer.grades:
                lectorer.grades[course] += [grade]
            else:
                lectorer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def rating(self):
        res = []
        for values in self.grades.values():
            res += values
        rating = sum(values) / len(res)
        return rating

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.rating()}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}
        """
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не Студент')
            return
        return self.rating() < other.rating()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python']
        

class Lectorer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {'Python': 10, 'Pytho': 9,'Pyth': 10}

    def rating(self):
        rating = sum(self.grades.values()) / len(self.grades.values())
        return rating
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating()}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lectorer):
            print('Это не Лектор')
            return
        return self.rating() < other.rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

some_lecturer = Lectorer('Some', 'Buddy')
print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 'something')
print(some_student)

daniil = Student("Daniil", "Any","something")
anna = Student("Anna", "Any","something")
jan = Reviewer("Jan", "Krd")
Reviewer.rate_hw(jan, daniil, 'Python', 6)
Reviewer.rate_hw(jan, anna, 'Python', 10)
print(daniil > anna)
print(daniil < anna)