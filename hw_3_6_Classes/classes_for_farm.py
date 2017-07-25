# coding=utf-8


class Animal:
    tail = True
    nose = True
    diet = ['grass', 'water', 'wheat', 'corn']
    status = 'domesticated'
    location = 'farm'

    def wake_up(self):
        print('Awoke!')

    def sleep(self):
        print('Fell asleep')

class Mammal(Animal):
    pass

class Bird(Animal):
    pass




