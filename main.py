class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
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
        rating = sum(res) / len(res)
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
        self.courses_attached = []
        

class Lectorer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rating(self):
        values = []
        for value in self.grades.values():
            values += value
        rating = sum(values) / len(values)
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

daniil = Student("Daniil", "Any","something")
anna = Student("Anna", "Any","something")
djan = Reviewer("Djan", "Krd")
jan_darm = Reviewer("Jan", "Darm")
maga_lector = Lectorer("Maga", "Lector")
mega_lodon = Lectorer("Mega", "Lodon")

maga_lector.courses_attached.append('Git')
mega_lodon.courses_attached.append('Java')
daniil.finished_courses.append('Python')
daniil.courses_in_progress = ['Введение в программирование', 'Git', 'Java']
djan.courses_attached.append('Git')
jan_darm.courses_attached.append('Git')
anna.finished_courses.append('Введение в программирование')
anna.courses_in_progress = ['Python', 'Git', 'Java']

daniil.rate_lec(maga_lector, 'Git', 8)
daniil.rate_lec(mega_lodon, 'Java', 10)
anna.rate_lec(maga_lector, 'Git', 4)
anna.rate_lec(mega_lodon, 'Java', 7)

djan.rate_hw(daniil, 'Git', 10)
djan.rate_hw(anna, 'Git', 8)

maga_lector.rating()
mega_lodon.rating()
print(maga_lector > mega_lodon)
print(mega_lodon > maga_lector)
print(daniil > anna)
print(daniil < anna)
print(daniil)
print(anna)
print(djan)
print(jan_darm)
print(maga_lector)
print(mega_lodon)