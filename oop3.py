#Multiple inheritances
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal')

#Mammal inherits Animal
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a mammal.')
    super().__init__(mammalName)

#CannotFly inherits Mammal
class CannotFly(Mammal):
  def __init__(self, mammalThatCantFly):
    print(mammalThatCantFly, 'cannot fly.')
    super().__init__(mammalThatCantFly)

#CannotSwim inherits Mammal
class CannotSwim(Mammal):
  def __init__(self, mammalThatCantSwim):
    print(mammalThatCantSwim, "cannot swim.")
    super().__init__(mammalThatCantSwim)

#Cat inherits CannotSwim and CannotFly
class Cat(CannotSwim, CannotFly):
  def __init__(self):
    print('I am a cat.')
    super().__init__('Cat')

#Drive code
cat = Cat()
print('')
bat = CannotSwim('Bat')

#Cat class's instaniation order of events
#1. Cat class is called first.
#2 CannotSwim parent class is called, appears before CannotFly
#in the order of inheritance. Follows Python's Method Resolution Order
#MRO outlines order in which methods inherited
#3. CannotFly class is called
#4. Mammal class is called
#5. Finally, Animal class is called.

#Bat object, bats are flying mammals, cannot swim.
#Bat object instantiated with the CannotSwim class.
#The super function in CannotSwim class invokes Mammal
#class constructor after it. Mammal class then invokes
#Animal class constructor
