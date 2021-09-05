# -*- coding: utf-8 -*-
# @Time: 2021/9/4 15:26
# @Author: yuyinghao
# @FileName: 03_class.py
# @Software: PyCharm

class Person(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        print('eat...')


class Student(Person):
    def __init__(self, name, gender, age, school, score):
        super(Student,self).__init__(name,gender,age)
        self.name = name.upper()
        self.gender = gender.upper()
        self.school = school
        self.score = score


s = Student('Alice', 'female', 18, 'Middle school', 87)
s.eat()
s.age