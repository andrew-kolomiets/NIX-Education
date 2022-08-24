# Создайте несколько классов: Animal (абстрактный класс), Cat, Dog
# Создайте абстрактные методы say, run и jump в классе Animal (abc.abstractmethod)
# Реализуйте полиморфизм поведения животных для методов: say, run, jump

import abc
from abc import ABC, abstractmethod
 
 
class Animal(ABC):
    
    # abstract method
    @abstractmethod
    def say():
        pass
    # abstract method
    @abstractmethod
    def run():
        pass
    # abstract method
    @abstractmethod
    def jump():
        pass
        
        
class Cat(Animal):
    # overriding abstract method
    def say(self):
        return 'Gau, gau, gau!'
    # overriding abstract method
    def run(self):
        return 'The cat is run!'
    # overriding abstract method
    def jump(self):
        return 'The cat is jump!'
    
    
class Dog(Animal):
    # overriding abstract method
    def say(self):
        return 'Niau, niau, niau!'
    # overriding abstract method
    def run(self):
        return 'The dog is run!'
    # overriding abstract method
    def jump(self):
        return 'The dog is jump!'
    

obj1=Dog()
print(obj1.run())

obj2=Cat()
print(obj2.run())

