class Animal:
    sound = ''
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}.".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = 'Oink!'

Piglet('Mark').speak()

class Cow(Animal):
    sound = 'Mooooo'

Cow('JJ').speak()