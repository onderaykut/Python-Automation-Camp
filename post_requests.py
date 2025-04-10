import requests

from get_requests import payload

from PIL import Image
from io import BytesIO
#grafik_URL='https://www.image-charts.com/chart'
#response = requests.post(grafik_URL, data=payload)
#image=Image.open(BytesIO(response.content))
#image.show()
#print(response.status_code)
#print(response.content)
#print(type(response.content))


class Futbolcu():

    def __init__(self,isim,hiz,sut,pas,top_surme,defans,fizik):
        self.isim=isim
        self.hiz=hiz
        self.sut=sut
        self.pas=pas
        self.top_surme=top_surme
        self.defans=defans
        self.fizik=fizik

    def yetenek_hazirla(self):
        return ','.join([
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_surme),
            str(self.defans),
            str(self.fizik)
        ])

    def yetenek_gorsellestir(self):
        from PIL import Image
        from io import BytesIO
        grafik_URL = 'https://www.image-charts.com/chart'
        payload = {
            'chco':'3092de',
            'chd':'t:' + self.yetenek_hazirla(),
            'chdl':self.isim,
            'chdlp':'b',
            'chs':'480x480',
            'cht':'r',
            'chtt':'Futbolcu Özellikleri',
            'chl': 'hiz|sut|pas|top_surus|defans|fizik',
            'chx1': '0:|0|20|40|60|80|100',
            'chxt':'x',
            'chxr':'0,0.0,100.0',
            'chm':'B,AAAAAABB,0,0,0',
        }
        response = requests.post(grafik_URL, data=payload)
        image=Image.open(BytesIO(response.content))
        image.show()
messi=Futbolcu('Messi',98,87,89,98,87,91)
ronaldo=Futbolcu('Ronaldo',98,80,89,98,87,99)

print(messi.yetenek_hazirla())





















