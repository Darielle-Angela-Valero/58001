class Person:
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display(self):
        print(self.__name, self.__pre, self.__mid, self.__fin)
        print("Term Grade:", self.Grade())


class Student1(Person):
    pass


class Student2(Person):
    pass


class Student3(Person):
    pass


student1 = Student1("Student 1:", 90, 98, 96)
student1.display()
student2 = Student2("Student 2:", 80, 86, 89)
student2.display()
student3 = Student3("Student 3:", 70, 76, 78)
student3.display()