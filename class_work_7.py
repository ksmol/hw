# f = open('1.txt', encoding = 'utf-8')
# print(f.read())
# print(f.readline())
# print(f.readline())
#
# f.close()
#-----------------------------------------

# with open('1.txt', encoding='utf-8') as f:
#     # print(f.readlines())
#     for line in f:
#         print(line.strip())

grades = {}

with open('1.txt', encoding='utf-8') as f:
    for line in f:
        grade = line.strip()
        print(grade)
        marks = f.readline()
        marks_list = marks.split()
#         # marks_list = [int(x) for x in marks_list]
        marks_list = list(map(int, marks_list))
        print(marks_list)
#         avg = sum(marks_list) / len(marks_list)
#         grades[grade] =avg
#         print(grades)
        f.readline()
#
# print(grades)
#
# maxGrade = None
# maxMark = 0
# for grade, mark in grades.items():
#     if maxMark < mark:
#         maxGrade = grade
#         maxMark = mark
#
# print('Класс с наилучшей оценкой: {}, оценка {}'.format(\
#     maxGrade, maxMark))
# with open('result.txt', 'w', encoding='utf-8') as f:
#     for grade, mark in grades.items():
#         f.write('{} класс с оценкой {}\n'.format(grade, mark))