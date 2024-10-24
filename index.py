class Person:
    #constructor
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
        self.created="14.10.2024"
    
    def info(self):
        status=self.get_status()
        print(f"{self.name} has {status}")

    def get_proper_weight(self):
        return (self.height**2)*23
    
    def get_status(self):
        proper_weight=self.get_proper_weight()
        max_proper_weight=proper_weight+(proper_weight*0.1)
        min_proper_weight=proper_weight-(proper_weight*0.1)
        if self.weight>max_proper_weight:
            return "over weight"
        elif self.weight>min_proper_weight:
            return "normal"
        return "under weight"

p1=Person("ahmet",95,1.82)
p2=Person("ali",75,1.73)
p3=Person("Yunus Emre",78,1.98)
p1.info()
p2.info()
p3.info()

