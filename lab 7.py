


from abc import ABC, abstractmethod

class Animal (ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def sleep(self):
        print("animal is sleeping ...")
class dog(Animal):
    def make_sound(self):
        print(" barks : woof woof ...!")
  
kupek = dog()
kupek.make_sound() 
kupek.sleep()       
        
        