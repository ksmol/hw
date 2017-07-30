# coding=utf-8


class Animal:
    tail = True
    general_diet = ['grass', 'water']
    status = 'domesticated'
    location = 'farm'
    number_of_legs = 4
    awakening_time = 4  # am
    sleep_time = 22  # pm

    def __init__(self, animals_name=None, sex='Women'):
        self.animals_name = animals_name
        self.sex = sex

    def wake_up(self, current_time):
        if 4 <= current_time <= 21:
            print('Не спит')

    def go_for_a_walk(self, current_position):
        if current_position == self.initial_location:
            print('В стойле')
        elif current_position != self.initial_location:
            print('Гуляет по ферме')

    def fall_sleep(self, current_time):
        if 0 <= current_time < 4 and current_time > 21:
            self.status
        return self.status


class Mammal(Animal):
    mammals_diet = ['milk', 'wheat']
    birth_method = 'Live birth'
    age = 0

    def __init__(self, animals_name=None, age=None, sex='Women'):
        super().__init__(animals_name, sex)
        self.age = age


class Cow(Mammal):
    russian_designation = 'Корова'
    initial_location = (2, 3)
    benefit = ['Give milk', 'Give meat']
    sound = 'Muuuu'
    default_sex = 'Cow'


class Goat(Mammal):
    russian_designation = 'Козел'
    initial_location = (5, 1)
    benefit = ['Give milk', 'Give wool']
    sound = 'Meeee'


class Sheep(Mammal):
    russian_designation = 'Овца'
    initial_location = (3, 1)
    benefit = ['Give wool', 'Give meat']
    sound = 'Beeee'


class Pig(Mammal):
    russian_designation = 'Свинья'
    initial_location = (6, 0)
    benefit = 'Give meat'
    sound = 'Oink-Oink'


class DomesticBird(Animal):
    birds_diet = ['corn', 'wheat', 'seashells']
    birth_method = 'Laying eggs'
    number_of_legs = 2
    benefit = ['Give meat', 'Give eggs']


class Duck(DomesticBird):
    russian_designation = 'Утка'
    benefit = ['Give feathers', 'Give meat', 'Give eggs']
    initial_location = (4, 4)
    sound = 'Kra-Kra'


class Chicken(DomesticBird):
    russian_designation = 'Курица'
    initial_location = (2, 4)
    benefit = ['Give feathers', 'Give meat', 'Give eggs']
    sound = 'Co-Co-Co'

    def __init__(self, animals_name=None, sex='hen'):
        super().__init__(animals_name)
        self.sex = sex


class Goose(DomesticBird):
    russian_designation = 'Гусь'
    initial_location = (3, 4)
    benefit = ['Give feathers', 'Give meat', 'Give eggs']
    sound = 'Ga-Ga'


goose = Goose('Ашот')
cow = Cow('Буренка', 9)
hen = Chicken('Ряба')
print(goose.initial_location)
print(goose.wake_up(5))
print(goose.go_for_a_walk((4, 6)))
print(goose.benefit)
print('Корове {} уже {} лет'.format(cow.animals_name, cow.age))
print('Того странного гуся зовут {}'.format(goose.animals_name))
print('Это {} {}'.format(hen.russian_designation, hen.animals_name))
