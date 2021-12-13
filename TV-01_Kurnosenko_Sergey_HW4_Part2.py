from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def office(self):
        pass


class IOffsiteCourse(ICourse, ABC):
    @property
    @abstractmethod
    def city(self):
        pass


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def createTeacher(teacher_name):
        pass

    @staticmethod
    @abstractmethod
    def createCourse(course_name, teacher, course_program, local_or_not, city_or_office):
        pass


class Teacher(ITeacher):
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    @property
    def name(self):
        return self.__name

    @property
    def courses(self):
        return self.__courses

    @name.setter
    def name(self, name):
        if not name or not isinstance(name, str):
            raise TypeError("wrong name")
        self.__name = name

    @courses.setter
    def courses(self, courses):
        if not isinstance(courses, list) or not all(isinstance(x, ICourse) for x in courses):
            raise TypeError("wrong courses")
        self.__courses = courses

    def __str__(self):
        s = "Name: " + self.__name + " ,Courses: "
        for i in self.__courses:
            s += i.__str__()
        return s


class LocalCourse(ILocalCourse):
    def __init__(self, name, teacher, course_program, office):
        self.name = name
        self.teacher = teacher
        self.course_program = course_program
        self.office = office

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def course_program(self):
        return self.__course_program

    @property
    def office(self):
        return self.__office

    @name.setter
    def name(self, name):
        if not name or not isinstance(name, str):
            raise TypeError
        self.__name = name

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError
        self.__teacher = teacher

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list) or not all(isinstance(x, str) for x in course_program):
            raise TypeError
        self.__course_program = course_program

    @office.setter
    def office(self, office):
        if not office or not isinstance(office, str):
            raise TypeError
        self.__office = office

    def __str__(self):
        return "Name: " + self.__name + " ,Type: Local ,Teacher: " + self.__teacher.name + " ,Program: " \
               + self.__course_program.__str__() + " ,Office: " + self.__office


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, teacher, course_program, city):
        self.name = name
        self.teacher = teacher
        self.course_program = course_program
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def course_program(self):
        return self.__course_program

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, name):
        if not name or not isinstance(name, str):
            raise TypeError
        self.__name = name

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError
        self.__teacher = teacher

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list) or not all(isinstance(x, str) for x in course_program):
            raise TypeError
        self.__course_program = course_program

    @city.setter
    def city(self, city):
        if not city or not isinstance(city, str):
            raise TypeError
        self.__city = city

    def __str__(self):
        return "Name: " + self.__name + " ,Type: Offsite ,Teacher: " + self.__teacher.name + " ,Program: " \
               + self.__course_program.__str__() + " ,City: " + self.__city


class CourseFactory(ICourseFactory):
    @staticmethod
    def createTeacher(teacher_name):
        return Teacher(teacher_name, [])

    @staticmethod
    def createCourse(course_name, teacher, course_program, local_or_not, city_or_office):
        if local_or_not:
            c = LocalCourse(course_name, teacher, course_program, city_or_office)
            teacher.courses.append(c)
            return c
        else:
            c = OffsiteCourse(course_name, teacher, course_program, city_or_office)
            teacher.courses.append(c)
            return c


t = CourseFactory.createTeacher("Sergey")
course = CourseFactory.createCourse("First", t, ["1", "2"], True, "office№2")
print(t)
