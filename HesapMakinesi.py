'''
class HesapMakinesi():

    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2

    def toplama(self,sayi1,sayi2):
        return sayi1 + sayi2

    def cikarma(self, sayi1, sayi2):
        return sayi1 - sayi2

    def carpma(self, sayi1, sayi2):
        return sayi1 * sayi2

    def bolme(self, sayi1, sayi2):
        return sayi1 / sayi2

hesapMakinesi=HesapMakinesi(20,10)

print(hesapMakinesi.toplama(5,10))
print(hesapMakinesi.cikarma(5,10))
print(hesapMakinesi.carpma(5,10))
print(hesapMakinesi.bolme(5,10))
'''