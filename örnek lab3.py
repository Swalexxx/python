class Kisi:
    def __init__(self, isim , yas):
        self.isim = isim
        self.yas = yas 
    def __str__(self):
        return f"{self.isim} , {self.yas} yasındadır."
    def __eq__(self,other):
        return self.isim == other.isim and self.yas == other.yas
kisi1 = Kisi("ahmet",21)
kisi2 = Kisi("ahmet",25)
print (kisi1)
print(kisi1==kisi2)