#Соколов Юрий муж. True 5 5 5 5 4 10
#Чернова Алла жен. False 4 4 3 5 5 9
#Миличкина Ирина жен. False 4 4 3 3 4 7
#Харитонов Игорь муж. True 4 5 4 3 4 8
#Измайлова Карина жен. True 5 4 4 5 5 10
#Соколов Юрий муж. False 4 3 3 3 4 7

student_directory = [
                      {'name' : 'соколов юрий', 'sex' : 'муж.', 'programming_exp' : True, 'hw_score' : [5, 5, 5, 5, 4], 'exam_score' : 10},
                      {'name' : 'чернова алла', 'sex' : 'жен.', 'programming_exp' : True, 'hw_score' : [4, 4, 3, 3, 3], 'exam_score' : 6},
                      {'name' : 'миличкина ирина', 'sex' : 'жен.', 'programming_exp' : False, 'hw_score' : [4, 4, 3, 3, 4], 'exam_score' : 7},
                      {'name' : 'харитонов игорь', 'sex' : 'муж.', 'programming_exp' : True, 'hw_score' : [4, 5, 4, 3, 4], 'exam_score' : 8},
                      {'name' : 'соколов юрий', 'sex' : 'муж.', 'programming_exp' : False, 'hw_score' : [5, 5, 4, 5, 5], 'exam_score' : 10},
                      {'name' : 'измайлова карина', 'sex' : 'жен.', 'programming_exp' : False, 'hw_score' : [5, 4, 5, 5, 5], 'exam_score' : 10}
                      
]
def input_attribute():
  attribute = input('Выберите и введите атрибут из списка (пол, опыт, чтобы вывести среднее по всей группе просто нажмите Enter, для выхода введите Q):').lower()
  return attribute

def add_avg_scores_for_student(input_directory):
  new_student_directory = []
  for student_info in input_directory:
    number_of_hw = len(student_info['hw_score'])
    summ_hw_score = sum(student_info['hw_score'])
    student_info['avg_hw_score'] = round(summ_hw_score / number_of_hw, 2)
    new_student_directory.append(student_info)
  return new_student_directory


def avg_scores_for_group(input_directory):
  summ_exam_score = 0
  summ_hw_score = 0
  student_directory_with_avg = add_avg_scores_for_student(input_directory)
  number_of_students = len(student_directory_with_avg)
  for student_info in student_directory_with_avg:
    summ_exam_score += student_info['exam_score']
    summ_hw_score += student_info['avg_hw_score']
  if number_of_students != 0:
    avg_hw_score = round(summ_hw_score /  number_of_students, 2)
    avg_exam_score = round(summ_exam_score / number_of_students, 2)
  avg_scores = [avg_hw_score, avg_exam_score]
  return avg_scores

def split_student_directory_by_attribut(attribute):
  men_student_list = []
  women_student_list = []
  student_with_exp_list = []
  student_without_exp_list = []
  dict_of_avg_by_attributes = {}
  if attribute == 'пол':
    for student_info in student_directory:
      if student_info['sex'] == 'муж.':
        men_student_list.append(student_info)
      elif student_info['sex'] == 'жен.':
        women_student_list.append(student_info)
    dict_of_avg_by_attributes['men'] = avg_scores_for_group(men_student_list)
    dict_of_avg_by_attributes['women'] = avg_scores_for_group(women_student_list)
  elif attribute == 'опыт':
    for student_info in student_directory:
      if student_info['programming_exp'] == True:
        student_with_exp_list.append(student_info)
      elif student_info['programming_exp'] == False:
        student_without_exp_list.append(student_info)
    dict_of_avg_by_attributes[True] = avg_scores_for_group(student_with_exp_list)
    dict_of_avg_by_attributes[False] = avg_scores_for_group(student_without_exp_list)
  return dict_of_avg_by_attributes

# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение

summ_of_hw_score = 0
dict_students_hw_avg_score = {}
dict_students_hw_avg_score = {}
for student_info in student_directory:
  number_of_hw = len(student_info['hw_score'])
  summ_of_hw_score = sum(student_info['hw_score']) / number_of_hw
  dict_students_hw_avg_score['name'] = student_info['name']
  dict_students_hw_avg_score['avg_score'] = summ_of_hw_score
print(dict_students_hw_avg_score)




def output_avg_results():
  while True:
    attribute = input_attribute()
    dict_of_avg_by_attributes = split_student_directory_by_attribut(attribute)
    if attribute == 'пол':
      print('Средняя оценка за домашние задания у мужчин: {}\n\
      Средняя оценка за экзамен у мужчин: {}\n\
      Средняя оценка за домашние задания у женщин: {}\n\
      Средняя оценка за экзамен у женщин: {}\n'.format(dict_of_avg_by_attributes['men'][0],\
                                                      dict_of_avg_by_attributes['men'][1],\
                                                      dict_of_avg_by_attributes['women'][0],\
                                                      dict_of_avg_by_attributes['women'][1]))
    elif attribute == 'опыт':
      print('Средняя оценка за домашние задания у студентов с опытом: {}\n\
      Средняя оценка за экзамен у студентов с опытом: {}\n\
      Средняя оценка за домашние задания у студентов без опыта: {}\n\
      Средняя оценка за экзамен у студентов без опыта: {}\n'.format(dict_of_avg_by_attributes[True][0],\
                                                                    dict_of_avg_by_attributes[True][1],\
                                                                    dict_of_avg_by_attributes[False][0],\
                                                                    dict_of_avg_by_attributes[False][1]))
    elif attribute == 'q':
      exit()
    else:
      print('Средняя оценка за домашние задания по группе:{}\n\
      Средняя оценка за экзамен:{}\n'.format(*avg_scores_for_group(student_directory)))

if __name__ == '__main__':
  output_avg_results()