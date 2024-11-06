from abc import ABC , abstractmethod
#interface olarak davranan bir abstract sınıf
class movable(ABC):
    @abstractmethod
    def move (self):
        pass
    @abstractmethod
    def stop (self):
        pass
class car (movable):
    def move (self):
        print ("car is moving ")
    def stop (self):
        print ("car has stopped")
        
car = car()
car.move()
car.stop()        