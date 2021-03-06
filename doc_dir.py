documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],

        '3': []
      }

documents_use = documents.copy()      
directories_use = directories.copy()

def input_command():
    comm = input('\nВведите команду из списка:\n\
 p - people (вывод хозяина документа)\n\
 l - list (вывод списка всех документов)\n\
 s - shell (вывод номера полки, где находится документ)\n\
 a - add (добавление нового документа в каталог)\n\
 d - delete (удалить документ из хранилища)\n\
 m - move (переместить документ на другую полку)\n\
 as - add shelf (добавить новую полку в хранилище документов)\n\
 e - exit (закрыть программу)\n')
    return comm

def input_doc_number():
    doc_number = input('Введите номер документа:\n')
    return doc_number

def input_doc_type():
    doc_type = input('Укажите тип документа:\n')
    return doc_type
    
def input_owner_name():
    owner_name = input('Укажите имя владельца документа в формате "ФИ":\n')
    return owner_name    
    
def input_shelf_num():
    shelf_num = input('Введите номер полки:\n')
    return shelf_num  

def confirm(conf ='нет'):
    conf = input()
    return conf

def find_people():
    num = input_doc_number()
    for i, doc in enumerate(documents_use):
        if documents_use[i]['number'] == num:
            print('\nХозяином документа № {} является {}\n'.format(documents_use[i]['number'], documents_use[i]['name']))

def doclist_output():
    for document in documents_use:
        print('{} "{}" "{}"'.format(document['type'],\
                                    document['number'],\
                                    document['name']))

def shelf_number():
    num = input_doc_number()
    for shelf in directories_use:
        if num in directories_use[shelf]:
            print('\n Этот документ находится на полке № {}'.format(shelf))
            
def add_doc_info():
    doc_type = input_doc_type()
    num = input_doc_number()
    name = input_owner_name()
    shelf = input_shelf_num()
    l_dir = len(directories) 
    documents_use.append({"type": doc_type, "number": num, "name": name})
    while shelf not in directories_use:
      print('\nВы указали несуществующую полку, пожалуйста, укажите номер в интервале от 1 до 3\n')
      shelf = input_shelf_num()
    else:
      for i, sh in enumerate(directories_use):
        if shelf == sh:
          directories_use[shelf].append(num)
    print('Обновленный список документов:\n {}\n Новый документ теперь лежит на полке №{} {}'.format(documents_use, shelf, directories_use))
    return documents_use, directories_use

def del_doc():
    num = input_doc_number()
    for i, n in enumerate(documents_use):
      for j, sh in directories_use.items():
        if documents_use[i]['number'] == num and num in directories_use[j]:
          ind = directories_use[j].index(num) #при условии, что все номера документов уникальны
          print('Вы действительно хотите удалить документ с номером {} ? (да/нет)'.format(documents_use[i]['number']))
          conf = confirm()
          if conf == 'да':
            documents_use.pop(i)
            directories_use[j].pop(ind)
            print('Документ с номером {} был удален.\n Список документов теперь выглядит так:\n\n{}\n\n\
            На полках лежат следующие документы: \n\n{}\n'.format(num, documents_use, directories_use))
          else:
            print('Документ не был удален.')

def move_doc():
    num = input_doc_number()
    shelf = input_shelf_num()
    prev_sh = ''
    for i, sh in directories_use.items():
        if num in directories_use[i]:
            ind = directories_use[i].index(num)
            prev_sh = i
            directories_use[i].pop(ind)
        if shelf == i:
            directories_use[shelf].append(num)
            print('\nДокумент с номером {} перемещен с полки {} на полку {}\n\nДокументы на полке теперь\
    расположены следующим образом:\n{} '.format(num, prev_sh, shelf, directories_use))  
    
def add_shelf():
    id = False
    while id == False:
      shelf = input_shelf_num()
      if shelf in directories_use:
        print('\nТакая полка уже существует, попробуйте еще раз\n')
      else:
        id = True  
        for nu, sh in directories.items():
          directories_use[shelf] = []
        print('Полка с номером {} добавлена, хранилище документов теперь выглядит так:\n{}\n'.format(shelf, directories_use))
        
def output_by_command():
    while True:
        ic = input_command()
        if ic == 'p':
            find_people()
        elif ic == 'l':
            doclist_output()
        elif ic == 's':
            shelf_number()
        elif ic == 'a':
            add_doc_info()
        elif ic == 'd':
            del_doc()
        elif ic == 'm':
            move_doc()
        elif ic == 'as':
            add_shelf()
        elif ic == 'e':
            exit()
        else:
            print('Вы ввели неверную команду')
    return directories_use
  
output_by_command()
