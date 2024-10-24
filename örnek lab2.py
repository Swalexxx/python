class bilgisayar:
    
    def __init__(self, marka , model , ram , depolama):
        self.marka = marka 
        self.model = model 
        self.ram = ram
        self.depolama = depolama
   
    def baslat (self):
        print(f"{self.marka}{self.model} bilgisayarınız baslatılıyor... " )
   
         def ozellikler (self):
                print(f"marka = {self.marka} model = {self.model} ram = {self.ram} depolama = {self.depolama} " ) 
                      
 
                      def kapat (self):
                          print(f"{self.marka}{self.model} bilgisayarınız kapatılıyor...")


pc1= bilgisayar("monster", "tulpar", 16, 512)
pc1.baslat()
pc1.ozellikler()
pc1.kapat()
