class Food:
    def __init__(self,name,carbs,fat,protein,quantity,measure):
        self.name=name
        self.carbs=carbs
        self.fat=fat
        self.protein=protein
        self.quantity=quantity
        self.measure=measure
    
    def info(self):
        print(f"Food name: {self.name}, protein: {self.protein}")

    def get_weight(self):
        c=0
        if self.measure=="cup":
            c=200
        elif self.measure=="tsp":
            c=6
        return self.quantity*c

    def get_calorie(self,gram=1):
        weight=self.get_weight()
        carbs1gr=self.carbs/weight
        fat1gr=self.fat/weight
        protein1gr=self.protein/weight
        return (carbs1gr*4+fat1gr*9+protein1gr*4)*gram

    def compare(self,food):
        cal1=self.get_calorie()
        cal2=food.get_calorie()
        if cal1>cal2:
            print(f"Calorie of {self.name} is greater than {food.name}")
        else:
            print(f"Calorie of {food.name} is greater than {self.name}")


f1=Food("Corn flakes",24.2,0.2,1.8,1,"cup")
f2=Food("Butter",0,3.8,0,1,"tsp")
f3=Food("Mango",7,0.1,0.2,0.25,"cup")
f2.info()
f1.info()
print(f1.get_weight())
print(f"{f3.name} : {f3.get_calorie(200)}")
f1.compare(f2)