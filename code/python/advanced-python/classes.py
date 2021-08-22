def function_name(var1, var2):
    pass

class FooClass:
    pass

# To instantiate
foo = FooClass()

# class Animal:
#     property_1 = { #property
#         'key_1': 'Value 1'
#     }
#     property_2 = ['a', 'b', 'c']

#     def method_1(self): #self gives access to properties and methods of class
#         print(self.property_1)

#     @property #decorator, treat it like a property
#     def method_2(self):
#         self.property_2.append('d')
#         return self.property_2[2]


# animal_1 = Animal()
# animal_1.method_1()
# print("this is a decorator property:", animal_1.method_2)

class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Raawwwrr")

    def eat(self):
        pass

    def chase(self):
        pass

    def sleep(self):
        raise NotImplementedError

class Tiger(Animal): #inherit
    def speak(self): #overwrite parent
        print("meow")
    def talk(self):
        super().speak()
        print("-y")

class HouseCat(Animal):
    def speak(self):
        print("Roar!!!")
    def sleep(self):
        print("zzzzz")

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
tiger.talk()
