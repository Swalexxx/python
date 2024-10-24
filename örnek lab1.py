class Phone:
    def __init__(self,marka,model,renk,yıl):
        self.marka = marka
        self.model = model 
        self.renk = renk 
        self.yıl = yıl 
    def baslat(self):
        print(f"{self.marka} {self.model} telefonunuz baslatılıyor...")
    def ozellikler(self):
        print(f" marka = {self.marka} model = {self.model} renk = {self.renk} yıl = {self.yıl}")
    def ara(self, numara):
        print (f"{self.marka} {self.model} cihaziniz {numara} numarasını ariyor ...")
    def kapat(self):
        print(f"{self.marka} {self.model} cihaziniz kapatılıyor ...")
                    
ph1=Phone("iphone", 11, "siyah", 2021)
ph1.baslat()
ph1.ozellikler()

aranacak = input("aranacak numarayı girin : ")

ph1.ara(aranacak)
ph1.kapat()
    
                