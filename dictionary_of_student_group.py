#Соколов Юрий муж. True 5 5 5 5 4 10
#Чернова Алла жен. False 4 4 3 5 5 9
#Миличкина Ирина жен. False 4 4 3 3 4 7
#Харитонов Игорь муж. True 4 5 4 3 4 8
#Измайлова Карина жен. True 5 4 4 5 5 10
#Соколов Юрий муж. False 4 3 3 3 4 7

student_directory = [
                      {'name' : 'соколов юрий', 'sex' : 'муж.', 'programming_exp' : True, 'hw_score' : [5, 5, 5, 5, 4], 'exam_score' : 10},
                      {'name' : 'чернова алла', 'sex' : 'жен.', 'programming_exp' : False, 'hw_score' : [4, 4, 3, 5, 5], 'exam_score' : 9},
                      {'name' : 'миличкина ирина', 'sex' : 'жен.', 'programming_exp' : False, 'hw_score' : [4, 4, 3, 3, 4], 'exam_score' : 7},
                      {'name' : 'харитонов игорь', 'sex' : 'муж.', 'programming_exp' : True, 'hw_score' : [4, 5, 4, 3, 4], 'exam_score' : 8},
                      {'name' : 'соколов юрий', 'sex' : 'муж.', 'programming_exp' : False, 'hw_score' : [4, 3, 3, 3, 4], 'exam_score' : 7},
                      {'name' : 'измайлова карина', 'sex' : 'жен.', 'programming_exp' : True, 'hw_score' : [5, 4, 4, 5, 5], 'exam_score' : 10}
                      
]

def avg_scores_for_group(input_directory):
  number_of_students = len(input_directory)
  summ_exam_score = 0
  for student_info in input_directory:
    number_of_hw = len(student_info['hw_score'])
    summ_exam_score += student_info['exam_score']
    summ_hw_score = sum(student_info['hw_score'])
  if number_of_students != 0:
    avg_hw_score = round(summ_hw_score / number_of_hw / number_of_students, 1)
    avg_exam_score = round(summ_exam_score / number_of_students, 1)
  avg_scores = [avg_hw_score, avg_exam_score]
  return avg_scores

def avg_scores_by_attributes():
  men_student_list = []
  women_student_list = []
  student_with_exp_list = []
  student_without_exp_list = []
  dict_of_avg_by_gender = {}
  dict_of_avg_by_exp = {}
  for student_info in student_directory:
    if student_info['sex'] == 'муж.':
      men_student_list.append(student_info)
    elif student_info['sex'] == 'жен.':
      women_student_list.append(student_info)
      
    if student_info['programming_exp'] == True:
      student_with_exp_list.append(student_info)
    elif student_info['programming_exp'] == False:
      student_without_exp_list.append(student_info)  
      
  dict_of_avg_by_gender['men'] =  avg_scores_for_group(men_student_list)  
  dict_of_avg_by_gender['women'] = avg_scores_for_group(women_student_list)
 
  dict_of_avg_by_exp[True] =  avg_scores_for_group(student_with_exp_list)  
  dict_of_avg_by_exp[False] = avg_scores_for_group(student_without_exp_list)
  
  return dict_of_avg_by_gender, dict_of_avg_by_exp

# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение

summ_hw_score = 0

for student_info in student_directory:
  number_of_hw = len(student_info['hw_score'])
  summ_of_hw_score = sum(student_info['hw_score'])
  print(summ_of_hw_score)


print()

print('Средняя оценка за домашние задания по группе:{}\n\
Средняя оценка за экзамен:{}\n'.format(*avg_scores_for_group(student_directory)))

dict_of_avg_by_attributes = avg_scores_by_attributes()

print('Средняя оценка за домашние задания у мужчин: {}\n\
Средняя оценка за экзамен у мужчин: {}\n\
Средняя оценка за домашние задания у женщин: {}\n\
Средняя оценка за экзамен у женщин: {}\n'.format(dict_of_avg_by_attributes[0]['men'][0],\
dict_of_avg_by_attributes[0]['men'][1], dict_of_avg_by_attributes[0]['women'][0], dict_of_avg_by_attributes[0]['women'][1]))

print('Средняя оценка за домашние задания у студентов с опытом: {}\n\
Средняя оценка за экзамен у студентов с опытом: {}\n\
Средняя оценка за домашние задания у студентов без опыта: {}\n\
Средняя оценка за экзамен у студентов без опыта: {}\n'.format(dict_of_avg_by_attributes[1][True][0],\
dict_of_avg_by_attributes[1][True][1], dict_of_avg_by_attributes[1][False][0], dict_of_avg_by_attributes[1][False][1]))