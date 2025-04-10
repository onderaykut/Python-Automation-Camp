"""
class SayiTahmin():
    import random

    secenekler = range(1, 10+1)
    bilgisayar_secimi = random.choice(secenekler)
    print("Bilgisayarın seçimi:", bilgisayar_secimi)


    def __init__(self,tahmin,tahmin2):
        self.tahmin=tahmin
        self.tahmin2=tahmin2


    def sayi_tahmin(self,tahmin,tahmin2):
        if tahmin==self.bilgisayar_secimi or tahmin2==self.bilgisayar_secimi:
            return 'Doğru tahmin ettiniz Tahminleriniz: {} - {} Bilgisayarın Tahmini {}'.format(tahmin,tahmin2,self.bilgisayar_secimi)
        else:
            return 'Yanlış tahminde bulundunuz Tahminleriniz: {} - {}  Bilgisayarın Tahmini {}'.format(tahmin,tahmin2 ,self.bilgisayar_secimi)

sayi_tahmin=SayiTahmin(1,2)

print(sayi_tahmin.sayi_tahmin(4,5))
"""