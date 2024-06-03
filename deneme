liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

tekrarlar = {}
for eleman in liste:
    if eleman in tekrarlar:
        tekrarlar[eleman] += 1
    else:
        tekrarlar[eleman] = 1

print("Listedeki tekrar eden elemanlar:")
for eleman, adet in tekrarlar.items():
    if adet > 1:
        print(str(eleman) + ": " + str(adet) + " kez tekrar ediyor.")
