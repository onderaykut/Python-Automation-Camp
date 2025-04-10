#import os
#print(os.getcwd())  #Şu anda çalıştığım ortamın adresi
#print(os.listdir()) #listele
#print(os.chdir())
#print(os.mkdir('C:\\Users\\ondre\\PycharmProjects\\starting\\deneme_klasoru2'))  #klasor olustur
#print(os.rmdir('C:\\Users\\ondre\\PycharmProjects\\starting\\deneme_klasoru')) #klasor silme
#yeni_dosya=os.open('yeni_dosya.txt',os.O_RDWR|os.O_CREAT)
#os.write(yeni_dosya,"Onder Aykut".encode())
#os.close(yeni_dosya)

## os.O_RDONLY - Read OnLy Sadece Oku

## os.O_WRONLY - Write OnLy - Sadece Yaz

## os.O_RDWR - Read and Write - Oku ve Yaz
## os.O_CREAT - Create - Olustur


#print("Hello \nWorld") #\n newline
#print("My name is \tÖnder")      # \t 1 tab bosluk
#print("My name is {} my age is {}".format("Önder",22))
#print("My name is {1}, my age is {0}".format("Önder",22))
#print("My name is {ad}, my age is {yas}".format(ad="Önder",yas=22))
#print(type(5))
#print(type(1.5))
#strvar="Python"
#print(strvar)
#print(strvar[0])
#print(strvar[2:])  [start:end]
#print(strvar[:2])
#print(strvar[2:4])
#print(strvar[2:6:2])  2 den altıya adar tara 2 atlayarak
#print(strvar[::2])
#print(len(strvar))
#strvar = strvar+" "+"oğren"
#print(strvar.lower())
#print(strvar.upper())
#print(strvar.find())

#liste=["a","b","c","d","e"]
#print(liste)
#liste=liste+["f"]
#print(liste)
#liste.append("g")
#print(liste)

#sayilar=[123,1,1,45,89,8999,6633,7755,45,123]
#sayilar.sort()
#print(sayilar)
#sayilar.reverse()
#print(sayilar)
#print(set(sayilar))

#liste=["a","b","c","d","e"]
#tup=("a","b","c","d","e")  #tuple object sabit
#liste[0]=22
#print(liste)
#print(tup.count('a'))

#dictionary1 = {
#   'isim':"Önder",
#   'Soyisim':'Aykut',
#   'Yas':22,
#  'lokasyon':{
#        "memleket":'Karabük',
#        'Yasadıgı Sehir':'İstanbul'
#           }
#}
#print(dictionary1["lokasyon"]["memleket"])
#print(dictionary1.get('Yas'))

#  hava_durumu="yagmurlu"
#  if hava_durumu=="yagmurlu" \
 #       :print("Şemsiyeni al")
#  elif hava_durumu=="karlı" :
#    print("dışarı çıkma")
#  else : print("Şemsiye alma")

#liste=["a","b","c","d"]
#hedef_harf="o"

#if hedef_harf in liste :
#   print("hedef harf bulundu")
#else: liste.append(hedef_harf)
#print("hedef harf eklendi")
#print(liste)

#toot=["önder aykut","ouz çelik","dodo ekinci","ahmet toktas","eto şahin"]
#for uye in toot:
#   print(uye)

"""
mod="önder aykut"
uye_sayisi=0
mod_sayisi=0

for uye in toot:
    ad, soyad =uye.split()[0],uye.split()[1]
    if (uye==mod):
        mod_sayisi+=1
        print('{0}. modun adı {1} ve soyadı {2}'.format(mod_sayisi,ad,soyad))
    else:
        uye_sayisi+=1
        print('{0}. uyenin adı {1} ve soyadı {2}'.format(uye_sayisi,ad,soyad))  """

"""
tup1=(1,3,5,7)

for sayi in tup1:
    print(sayi)

liste=[[1,2],[3,4]]
for x,y in liste:
    print(x)
"""

"""
kullanici1={
    "ad":"Ömder",
    "soyad":"Aykut"
    }

for k,v in kullanici1.items():
    print("Key: {}\t Value:{}".format(k,v))
"""
"""
x=0
while x<10:
    print("{} değeri 10dan kucuk ".format(x))
    x += 1
else: print("{} değeri 10a eşit".format(x))
"""
"""
sayi=5
sonuc=1

while sayi>0:
    sonuc = sayi*sonuc
    sayi-=1
    print(sonuc)
"""
"""
#print(list(range(10))) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for sayi in range(10):
    print(sayi)
"""
"""
harfler=["a","b","c","d","e"]
for harf in enumerate(harfler): #indexleriyle beraber
    print(harf)
"""
"""
ulkeler=["TR","ENG","USA"]
siralamalar=range(1,4)
for ulke,sira in zip (ulkeler,siralamalar):
    print(sira,ulke )
    """
"""
harfler=["a","b","c","d","e"]
for index,harf in enumerate(harfler):
    print(index+1,harf)
    if harf=="c" or index==4:
        print("{} harfi ya da {}. index bulundu".format(harf,index))
        break;
"""
"""
#tek sayıları yazdırıyo
for sayi in range(9):
    if sayi%2 !==0:
        continue
    print(sayi)
"""
"""
for sayi in range(9):
    if sayi%2 !=0:
        pass
    else:
        print(sayi)
"""
"""
kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}

kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün' ,
    'uzmanlik': ['Front-End']
}
"""
"""
#print(kullanici1.get("uzmanlik"))
kullanici_listesi=[kullanici1,kullanici2,kullanici3]
kullanici_yaslari_listesi=[22,35,40]
"""
"""
for kullanici in kullanici_listesi:
    if 'Front-End' in   kullanici.get('uzmanlik'):
        print(kullanici.get('ad'))"""
"""
kullanici3['uzmanlik'].append('Yazilim')
print(kullanici3)
"""
"""
for yas,kullanici in zip (kullanici_yaslari_listesi,kullanici_listesi):
    if yas<30:
        print(kullanici)
"""

"""
deger=7
x=deger-1
while x>1:
    if deger%2==0:
        print("{} asal degil".format(deger))
        break
    else:
        x=x-1
else:
    print("{} asal sayidir".format(deger))
"""
"""
def bes_bastir():
    print(5)
def bes_dondur():
    return 5
bes_bastir()
print(bes_dondur())
"""
"""
def buyuk_sayi_dondur(sayi1,sayi2):
     if sayi1 >sayi2:
         return sayi1
     else: return sayi2

def metin_yaz(a,b):
   buyuk_sayi=buyuk_sayi_dondur(a,b)
   metin=" {} daha buyuktur".format(buyuk_sayi)
   print(metin)

metin_yaz(5,55)
buyuk_sayi_dondur(5,15)
"""
"""
def carpma(sayi1,sayi2):
    return sayi1*sayi2
print(carpma(20,5))
"""
"""
def isim_soyisim_ayirma(isim_soyisim):
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
    print(isim,soyisim)
    return isim,soyisim
isim_soyisim_ayirma("Önder Aykut")
"""
"""
#    MAP
def kare(x):
    return x ** 2  # Sayının karesini alır

sayilar = list(range(1, 6))  # [1, 2, 3, 4, 5]
sonuc = list(map(kare, sayilar))  # [1, 4, 9, 16, 25]
print(sonuc)
"""
"""
def cift_sayi_fitrele(x):
    if x%2==0:
        return x
    else:
        return None

print(cift_sayi_fitrele(4))

#filter
sayilar = list(range(1, 6))
sonucc=list(filter(cift_sayi_fitrele,sayilar))
print(sonucc)
"""
"""
sayilar= list(range(1,6))
sonuc=list(filter(lambda x: x if x%2==0 else None,sayilar))
print(sonuc)
"""
"""
def uygulama():
    girdi=input('Bir sayi girin :')
    islem=input('girilen sayinin çift mi tek mi olduğunu sorgula :')

    if islem=='çift':
        if int(girdi) % 2 == 0:
            return 'Girilen sayi çift'
        else:
            return 'Girdi Çift sayı değil'
    elif str(islem)=='tek':
        if int(girdi) % 2 != 0:
            return 'Girilen sayi tek'
        else:
            return 'girilen sayi tek degil'
print(uygulama())
"""
"""
def sayi_girdisi_kontrol():
    if input().isdigit():
        return 'Geçerli girdi'
    else:
        return 'Geçersiz girdi'

print(sayi_girdisi_kontrol())
"""
"""
def sayi_girdi_kontrol_dongu():
    girdi= input('Bir sayi girin: ')
    while not girdi.isdigit():
        print('Geçersiz girdi')
        girdi = input('Bir sayi girin')
    else:
        print('Geçerli girdi')
print(sayi_girdi_kontrol_dongu())
"""
"""
def e_posta_kontrol():
    eposta=input('Bir e posta adresi giriniz: ')
    while not(('@' in eposta) and ('.' in eposta)):
        print('Geçersiz bir e posta girdiniz')
        eposta = input('Bir e posta adresi giriniz: ')
    else:
        print('Geçerli e posta girdiniz')
print(e_posta_kontrol())
"""
#print(round(1.6))  #yuvarlama
"""
def tam_sayiya_cevir():
    girdi=input('Bir ondalik sayi girin: ')
    status=''
    try:
        girdi=round(float(girdi))
        print('Yuvarlama islemi sonucu {}'.format(girdi))
        status='basarili'
    except:
        print('Girdi ({}) Tam sayiya cevrilemiyor'.format(girdi))
        status = 'basarisiz'
    finally:
        print('Yuvarlama islemi sonucu {}'.format(status))
    return girdi
print(tam_sayiya_cevir())
"""
"""
def tam_sayiya_cevir_dongu():

    while True:
        girdi = input('Ondalikli bir sayi giriniz: ')
        try:
            girdi=round(float(girdi))
            print('Yuvarlama islemi sonucu {}'.format(girdi))
            break
        except:
            print('Girilen değer({}) tam sayıya cevrilemiyor'.format(girdi))
            pass
    return girdi
print(tam_sayiya_cevir_dongu())
"""
"""
def ustel_sayi(x,y):
    return x**y
print(ustel_sayi(47,5))
"""
"""
def ustel_sayi(x,y):
    sonuc =1
    for kuvvet in range(1,y+1):
        sonuc = sonuc * x
    return sonuc

print(ustel_sayi(5,3))
"""
"""
for kullanici in kullanici_listesi:
    if 'Front-End' in   kullanici.get('uzmanlik'):
        print(kullanici.get('ad'))
"""
"""
liste=[1,4,9,15,99,3]
def liste_dondur(liste):

    liste.sort()
    return liste[-1],liste[-2]
print(liste_dondur(liste))
"""
"""
list=['a','onder','b',22,775]
def str_filtrele(list):

    strlist=[]
    for x in list:
        if type(x)== str:
            strlist.append(x)
        else:
            pass
    return strlist
print(str_filtrele(list))
"""
"""
liste=[90000000,150000000,250000000]
def alti_sifir_at(liste):
    sonuc=[]
    for x in liste:
        sonuc.append(int(x/1000000))

    return sonuc
print(alti_sifir_at(liste))
"""
"""
def saat_dakika():
    saat=input('Saat girin: ')

    if saat>'23' and saat<'00':
        saat = input(int('Geçerli bir saat girin'))
    else:
        dakika=input('dakika girin')
        if dakika>'59' and dakika<'00':
                dakika=input('Geçerli bir dakika girin: ')
        else:
            pass
        return 'Girdiğiniz saat: '+saat+':'+ dakika
print(saat_dakika())
"""
"""
def saat_dakika2():
    saat=input("Saat Girin: ")
    if saat.isdigit():
        saat=int(saat)
        if ((saat>=0) and (saat<24)):
            dakika=input("Dakika Girin: ")
            if dakika.isdigit():
                dakika=int(dakika)
                if dakika>=0 and dakika<60:
                    return 'Girilen saat {}:{}'.format(saat,dakika)
print(saat_dakika2())
"""

#Class
class Ucus():
    havayolu='THY'
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons_yap(self):
        return "{} sefer sayılı {} - {} ucusumuz {} dakika sürecektir".format(self.kod,self.kalkis,self.varis,self.sure)
    def koltuk_sayi_guncelle(self):
        return self.kapasite-self.yolcu
    def bilet_satis(self,bilet_adedi=1):
        if self.yolcu+ bilet_adedi <=self.kapasite:
            self.yolcu+=bilet_adedi
            self.koltuk_sayi_guncelle()
            return '{} adet bilet satıldı kalan koltuk {} '.format(bilet_adedi,self.koltuk_sayi_guncelle())
        else:
            print('İşlem gerçekleştirilemedi.Yeteri kadar koltuk yok.  ')
    def bilet_iptal(self,bilet_adedi=1):
        if self.yolcu>=bilet_adedi:
            self.yolcu -= bilet_adedi
            self.koltuk_sayi_guncelle()
            return '{} adet bilet iptal edildi.Kalan boşta koltuk sayisi {}'.format(bilet_adedi ,self.koltuk_sayi_guncelle())
        else:
            print('İşlem gerçekleştirilemedi. ')
#ucus1=Ucus()
#print(ucus1.havayolu)
ucus1=Ucus('TH32','IST','ANT',90,250,250)
ucus2=Ucus('KV97','IST','BUR',120,250,150)

print(ucus2.bilet_satis(4))
print(ucus2.bilet_satis(2))
print(ucus2.bilet_iptal())
#print(ucus2.koltuk_sayi_guncelle())
#print(ucus2.anons_yap())
print(ucus2.kalkis,ucus2.varis)
print(ucus1.kalkis,ucus1.varis)
print(ucus2.__dir__())

'''
class Onder():
    def sayi_metin(self,sayi ,metin):
        return '{}{}'.format(str(sayi),metin)

ond=Onder()
print(ond.sayi_metin(22,'metin'))
'''
'''
class Topla_cikar():
    def toplama(self,sayi1,sayi2):
        return sayi1 + sayi2
    def cikarma(self,sayi1,sayi2):
        return sayi1 - sayi2
top_cik=Topla_cikar()
print(top_cik.toplama(12,14))
print(top_cik.cikarma(12,14))
'''














