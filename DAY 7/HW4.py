import string

# QUESTION 1:
with open("my_id.txt", "w") as file:
    file.write("name: Matan Atedgi\nage: 30\nphone_number: 0525758426")


# QUESTION 2:
def word_frequency_dict(file_path):
    with open(file_path, "r") as file:
        word_list = file.read().split()
    dict = {}
    for word in word_list:
        word = word.strip()
        word = word.strip(string.punctuation)
        dict[word] = dict.get(word, 0) + 1
    return dict


# 1)
def read_lines(n, file_path):
    with open(file_path, "r") as file:
        result = ""
        for i in range(n):
            result += file.readline()
        return result


# 2)
def find_longest_word(file_path):
    with open(file_path) as file:
        word_list = file.read().split()
    result = ""
    for word in word_list:
        word = word.strip()
        word = word.strip(string.punctuation)
        if len(result) < len(word):
            result = word
    return result


# 3)
def reverse_word(input_string: str):
    word_list = input_string.split()
    return " ".join(word_list[::-1])


# 4)
class Upper_string:
    def __init__(self):
        self.string = None

    def get_string(self, input_sting):
        self.string = input_sting

    def print_string(self):
        print(self.string.upper())


# 5)
class Rectangle:
    def __init__(self):
        self.width = 2
        self.hight = 3

    def get_area(self):
        return self.width * self.hight


# 6)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")


class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying!")


class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming!")


# forel = Fish("forel")
# forel.swim()
# forel.eat()
# forel.sleep()

# hummingbird = Bird("hummingbird")
# hummingbird.eat()
# hummingbird.sleep()
# hummingbird.fly()


# 7)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start():
        pass

    def stop():
        pass


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        Vehicle.__init__(self, make, model, year)
        self.number_of_doors = number_of_doors


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        Vehicle.__init__(self, make, model, year)
        self.has_sidecar = has_sidecar


# car = Car("mazda", "2", 2015, 5)
# print(f"{car.make} {car.model} {car.year} has {car.number_of_doors} doors")
# motorcycle = Motorcycle("kawasaki", "Z400", 2020, False)
# print(f"{motorcycle.make} {motorcycle.model} {motorcycle.year} {'has' if motorcycle.has_sidecar else 'doesn\'t have'} a side car")


# 8)
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Student(Person):
    def __init__(self, name, address, student_id, enrolled_courses=None):
        Person.__init__(self, name, address)
        self.student_id = student_id
        self.enrolled_courses = enrolled_courses

    def enroll_course(self, course):
        if not self.enrolled_courses:
            self.enrolled_courses = [course]
        elif course in self.enrolled_courses:
            print(f"{self.name} is already enrolled to {course} course")
        else:
            self.enrolled_courses.append(course)
            print(f"{self.name} is now enrolled to {course} course")


class Instructor(Person):
    def __init__(self, name, address, employee_id, teaching_courses=None):
        Person.__init__(self, name, address)
        self.employee_id = employee_id
        self.teaching_courses = teaching_courses

    def assign_teaching(self, course):
        if not self.teaching_courses:
            self.teaching_courses = [course]
        elif course in self.teaching_courses:
            print(f"{self.name} is already assigned to teach {course} course")
        else:
            self.teaching_courses.append(course)
            print(f"{self.name} is now assigned to teach {course} course")


# student = Student("david", "herzl 5, herzliya", "551516", ["Chemistry", "Physics"])
# student.enroll_course("Thermodynamics")
# student.enroll_course("Thermodynamics")
# print(student.enrolled_courses)

# instructor = Instructor("shlomo", "herzl 4, herzliya", "451586", ["Chemistry"])
# instructor.assign_teaching("Physics")
# print(instructor.teaching_courses)
