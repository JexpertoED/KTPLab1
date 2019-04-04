# coding:utf-8
groupmates = [
    {
        "name": u"Евгений Жмакин",
        "group": u"БВТ1702",
        "age": 18,
        "marks": [5, 4, 4, 5, 5]
    },
    {
        "name": u"Андрей Тимчкук",
        "group": u"БВТ1702",
        "age": 20,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": u"Зверь",
        "group": u"БВТ1702",
        "age": 19,
        "marks": [3, 3, 3, 3, 3]
    },
    {
        "name": u"Даниил Вершинин",
        "group": u"БВТ1701",
        "age": 18,
        "marks": [3, 4, 4, 5, 4]
    }
]


def print_students(students):
    print u"Имя студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20)
    for student in students:
        print \
            student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20)
    print "\n"


def student_avg(avgMark, students):
    matchingstudents = []
    for student in students:
        count = 0
        for mark in student["marks"]:
            count += mark
        if count / len(student["marks"]) >= avgMark:
            matchingstudents.append(student)
    return matchingstudents


print_students(student_avg(4, groupmates))
