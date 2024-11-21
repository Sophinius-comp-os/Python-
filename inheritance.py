#Prent class
class Animal:
    def move(self):

        print("Animal is Walking")

#Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


a = Animal()
d = Dog()

d.bark()
d.move()