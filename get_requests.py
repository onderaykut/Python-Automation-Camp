import json

import requests

bolgeler_URL='https://data.police.uk/api/forces'

response= requests.get(bolgeler_URL)
#print(response)  #<Response [200]>

#help(response)
#print(response.status_code) #200
#print(response.url) #https://data.police.uk/api/forces
#print(response.json())


#crime_categories_URL='https://data.police.uk/api/crime-categories'
#print(requests.get(crime_categories_URL))  #<Response [200]>
#payload={ 'date':'2011-08'}
#response = requests.get(crime_categories_URL,params=payload)

#print(response.status_code) #200
#print(response.url) #https://data.police.uk/api/crime-categories?date=2011-08
#print(response.json())
#print(json.dumps(response.json(),indent=4))
                                                                                                           #
                                                                                                           # data = response.json()
                                                                                                            #with open('crime_categories.json', 'w', encoding='utf-8') as f:
                                                                                                             #   json.dump(data, f, indent=4)
                                                                                                            #print("JSON dosyası başarıyla kaydedildi!")
                                                                                                            #
lokasyonsuz_suclar='https://data.police.uk/api/crimes-no-location'
payload={
    'category':'all-crime',
   'date':'2023-01',
    'force':'leicestershire'}
#?category=all-crime&date=2024-01&force=leicestershire
response=requests.get(lokasyonsuz_suclar,params=payload)
#print(response.json())
#print(requests.get(lokasyonsuz_suclar)) #<Response [200]>

from collections import Counter
class SucRaporu():
    def __init__(self,bolge,tarih,suc_tipi='all-crime'):
        self.bolge=bolge
        self.tarih=tarih
        self.suc_tipi=suc_tipi
        self.suclar=self.suclari_bul()

    def suclari_bul(self):
        suc_url='https://data.police.uk/api/crimes-no-location'
        payload={
            'category':self.suc_tipi,
            'date':self.tarih,
            'force':self.bolge
        }
        response = requests.get(suc_url, params=payload)
        if response.status_code==200:
            return response.json()
        else:
            return None
    def suclari_raporla(self):
        suclar_listesi=[]
        if self.suclar is not None:
            for suc in self.suclar:
                suclar_listesi.append(suc['category'])

            return Counter(suclar_listesi)




suc_raporu1=SucRaporu('city-of-london','2024-01') #default suc_tipi='all-crime'
#print(suc_raporu1.suclar)
#print(suc_raporu1.suclari_raporla())
#print(suc_raporu1.suclari_bul())
















