def class_demo():
    print("\n---- CLASS & INHERITANCE ----")

    class Animal:
        def speak(self):
            print("Animal speaks")

    class Dog(Animal):  # Inheritance
        def speak(self):
            print("Dog barks")

    class Cat(Animal):
        def speak(self):
            print("Cat meows")

    a = Animal()
    d = Dog()
    c = Cat()

    a.speak()
    d.speak()
    c.speak()

class_demo()