# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def prn(self, name, age):
#         print(self.name, self.age)
#
# dog1 = Dog("Rex", 3)
# #dog1.prn

# class Company:
#     department = 15
#
#     def __init__(self, surname, age, department = 15):
#         self.surname = surname
#         self.age = age
#         self.department = department
#
# s1 = Company("������", 23, 14)
# s2 = Company("�������", 24, 16)
# s3 = Company("������", 30, 4)

class School:
    def __init__(self, id, age, population):
        self.id = id
        self.age = age
        self.population = population

one = School(13, 25,1500)

print("������ id:  ", one.id)
print("�������� age (��������� ��������):  ", one.age)
print("�������� population (��������� ��������):  ", one.population)

one.age = 27
one.population = 1650

print("�������� age (��������� ��������):  ", one.age)
print("�������� population (��������� ��������):  ", one.population)


