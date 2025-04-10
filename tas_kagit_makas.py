
class TasKagitMakas():
    import random

    secenekler = ['tas', 'kagit', 'makas']
    bilgisayar_secimi = random.choice(secenekler)
    print("Bilgisayarın seçimi:", bilgisayar_secimi)

    def __init__(self,tas,kagit,makas):
        self.tas=tas
        self.kagit=kagit
        self.makas=makas

    def tas_kag_mak(self,secim,bilgisayar_secimi= random.choice(secenekler)):
        if secim==self.tas and bilgisayar_secimi==self.tas:
          return 'Oyun Berabere Seçiminiz {} Bilgisayarın seçimi {} '.format(self.tas,self.tas)
        if secim==self.kagit and bilgisayar_secimi==self.kagit:
            return 'Oyun Berabere Seçiminiz {} Bilgisayarın seçimi {} '.format(self.kagit,self.kagit)
        if secim==self.makas and bilgisayar_secimi==self.makas:
            return 'Oyun Berabere Seçiminiz {} Bilgisayarın seçimi {} '.format(self.makas,self.makas)

        if secim==self.tas and bilgisayar_secimi==self.makas:
            return 'Oyunu kazandınız Seçiminiz {} Bilgisayarın seçimi {} '.format(self.tas,self.makas)
        if secim==self.kagit and bilgisayar_secimi==self.tas:
            return 'Oyunu kazandınız Seçiminiz {} Bilgisayarın seçimi {} '.format(self.kagit,self.tas)
        if secim== self.makas and bilgisayar_secimi==self.kagit:
            return 'Oyunu kazandınız Seçiminiz {} Bilgisayarın seçimi {} '.format(self.makas,self.kagit)

        if secim==self.tas and bilgisayar_secimi==self.kagit:
            return 'Oyunu kaybettiniz Seçiminiz {} Bilgisayarın seçimi {} '.format(self.tas,self.kagit)
        if secim==self.kagit and bilgisayar_secimi==self.makas:
            return 'Oyunu kaybettiniz Seçiminiz {} Bilgisayarın seçimi {} '.format(self.kagit,self.makas)
        if secim==self.makas and bilgisayar_secimi==self.kagit:
            return 'Oyunu kaybettiniz Seçiminiz {} Bilgisayarın seçimi {} '.format(self.makas,self.kagit)

tas_kagit_makas=TasKagitMakas('tas','kagit','makas')

print(tas_kagit_makas.tas_kag_mak('tas'))