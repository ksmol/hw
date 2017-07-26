# coding=utf-8


class Animal:
    type = 'Animal'

    def __init__(self):
        self.tail = True
        self.nose = True
        self.general_diet = ['grass', 'water']
        self.status = 'domesticated'
        self.location = 'farm'
        self.number_of_legs = 4
        self.awakening_time = 4
        self.sleep_time = 21
        self.initial_location = (0, 0)

    def wakeUp(self, current_time):
        if 4 <= current_time <= 21:
            print('Не спит')

    def goForAWalk(self, current_position):
        if current_position == self.initial_location:
            print('Не двигается')
        elif current_position != self.initial_location:
            print('Гуляет')

    def fallAsleep(self, current_time):
        if 0 <= current_time < 4 and current_time > 21:
            print('Спит')


class Mammal(Animal):
    type = 'Mammal'

    def __init__(self):
        Animal.__init__(self)
        self.mammals_diet = ['milk', 'wheat']
        self.birth_method = 'Live birth'


class Cow(Mammal):
    type = 'Cow'

    def __init__(self):
        Mammal.__init__(self)
        self.initial_location = (2, 3)
        self.benefit = ['Give milk', 'Give meat']


class Goat(Mammal):
    type = 'Goat'

    def __init__(self):
        Mammal.__init__(self)
        self.initial_location = (5, 1)
        self.benefit = ['Give milk', 'Give wool']


class Sheep(Mammal):
    type = 'Sheep'

    def __init__(self):
        Mammal.__init__(self)
        self.initial_location = (3, 1)
        self.benefit = ['Give wool', 'Give meat']


class Pig(Mammal):
    type = 'Pig'

    def __init__(self):
        Mammal.__init__(self)
        self.initial_location = (6, 0)
        self.benefit = 'Give meat'


class DomesticBird(Animal):
    type = 'DomesticBird'

    def __init__(self):
        Animal.__init__(self)
        self.birds_diet = ['corn', 'wheat', 'seashells']
        self.birth_method = 'Laying eggs'
        self.number_of_legs = 2
        self.benefit = ['Give meat', 'Give eggs']


class Duck(DomesticBird):
    type = 'Duck'

    def __init__(self):
        DomesticBird.__init__(self)
        self.initial_location = (4, 4)


class Chicken(DomesticBird):
    type = 'Chicken'

    def __init__(self):
        DomesticBird.__init__(self)
        self.initial_location = (2, 4)


class Goose(DomesticBird):
    type = 'Goose'

    def __init__(self):
        DomesticBird.__init__(self)
        self.initial_location = (3, 4)
        self.benefit = ['Give feathers', 'Give meat', 'Give eggs']


goose = Goose()
cow = Cow()
print(goose.initial_location)
print(goose.wakeUp(5))
print(cow.goForAWalk((0, 0)))
print(goose.benefit)
