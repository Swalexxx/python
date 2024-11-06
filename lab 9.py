from abc import ABC, abstractmethod

class telefonfabrikasi(ABC):
    def __init__(self, model , uretici, batarya_kapasitesi):
        self.model = model
        self.uretici = uretici
        self.batarya_kapasitesi = batarya_kapasitesi
    def sarj_durumu(self):
        print(f"{self.model} cihazınızın batarya kapasitesi = {self.batarya_kapasitesi} mAh")
        
    @abstractmethod
    def arama_yap(self,numara):
        pass
    @abstractmethod    
    def mesaj_gonder(self, numara, mesaj):
        pass
    @abstractmethod
    def ozellikleri_goster(self):
        pass


class iphone(telefonfabrikasi):
    def __init__(self, model, batarya_kapasitesi, kamera_megapiksel):
        super().__init__ (model, "apple", batarya_kapasitesi)
        self.isletim_sistemi = "ios"
        self.kamera_megapiksel = kamera_megapiksel
        
    def arama_yap(self, numara):
        print(f"{self.model}(apple) numarayı arıyor: {numara}")
    def mesaj_gonder(self, numara, mesaj):
        print(f"{self.model}(apple) mesaj  gönderiyor: {numara}- '{mesaj}'")
    def ozellikleri_goster(self):
        print(f"model: {self.model}")
        print(f"uretici: {self.uretici}")
        print(f"batarya kapasitesi: {self.batarya_kapasitesi} mAh")
        print(f"işletim sistemi: {self.isletim_sistemi}")
        print(f"kamera : {self.kamera_megapiksel} mp")
        
        
class samsung(telefonfabrikasi):
    def __init__(self, model, batarya_kapasitesi, suya_dayaniklilik):
        super().__init__ (model, "samsung", batarya_kapasitesi)
        self.isletim_sistemi = "android"
        self.suya_dayaniklilik=suya_dayaniklilik
        
        
    def arama_yap(self, numara):
        print(f"{self.model}(samsung) numarayı arıyor: {numara}")
    def mesaj_gonder(self, numara, mesaj):
        print(f"{self.model}(samsung) mesaj  gönderiyor: {numara}- '{mesaj}'")
    def ozellikleri_goster(self):
        print(f"model: {self.model}")
        print(f"uretici: {self.uretici}")
        print(f"batarya kapasitesi: {self.batarya_kapasitesi} mAh")
        print(f"işletim sistemi: {self.isletim_sistemi}")
        print(f"suya dayanıklılık : {self.suya_dayaniklilik}")
        
def telefon_olustur():
    while True:
        uretici = input("telefon üreticisini seciniz: (apple ve samsung)").strip().lower()
        
        if uretici in ["apple","samsung"]:
            model = input("telefon modelini giriniz: ")
            batarya_kapasitesi = int(input("batarya kapasitesi kaç mAh"))
            if uretici == "apple":
                kamera_megapiksel = int(input("Kamera megapikselini giriniz: "))
                return iphone(model, batarya_kapasitesi, kamera_megapiksel)
            
            elif uretici == "samsung":
                suya_dayaniklilik = input("suya dayanıklılık derecesini giriniz (örn IP85)")
                return samsung(model, batarya_kapasitesi, suya_dayaniklilik)
        else:
            print("gecersiz bir uretici frima sectiniz . adam gibi seçiniz")
            
telefon= telefon_olustur()
telefon.sarj_durumu()

numara = int(input("\n aramak istediğiniz numarayı giriniz: "))

telefon.arama_yap(numara)
mesaj_numara = input("\n mesaj atmak istediğiniz numarayı giriniz: ")
mesaj = input("göndermek istediğiniz mesaj içeriğini giriniz")
telefon.mesaj_gonder(numara, mesaj)

print("\n telefon özellikleri")
telefon.ozellikleri_goster()        
        
    


