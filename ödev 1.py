class memur:
    def __init__(self, vatandaslik, yas, egitim, puan):
        self.vatandaslik = vatandaslik
        self.yas = yas
        self.egitim = egitim
        self.puan = puan

    def uygunluk_kontrol(self):
        if not self.vatandaslik:
            return "Türkiye vatandaşı olmalısınız."
        if not (18 <= self.yas <= 35):
            return "18-35 yaş aralığında olmalısınız."
        if self.egitim not in ["lise", "önlisans", "lisans"]:
            return "En az lise, önlisans veya lisans mezunu olmalısınız."
        if self.puan < 70:
            return "KPSS'den en az 70 puan almanız gerekmektedir."
        return "Devlet memuru olmak için tüm şartları sağlıyorsunuz!"


vatandaslik = input("Türkiye vatandaşı mısınız? (evet/hayır): ").lower() == "evet"
yas = int(input("Yaşınızı girin: "))
egitim = input("Eğitim durumunuz (lise/önlisans/lisans): ").lower()
puan = int(input("KPSS puanınızı girin: "))

aday = memur(vatandaslik, yas, egitim, puan)
sonuc = aday.uygunluk_kontrol()

print(sonuc)
