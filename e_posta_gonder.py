import ssl
import smtplib

kullanici='aykutonder0@gmail.com'
sifre='dqvr lhsg kqoz zquw'

#alici=kullanici
alici='cemsahin.html@gmail.com'

mesaj='bre pythondan mail gondermeye calisiyom da denemek için attim'

context=ssl.create_default_context()
#port=465
#host='smtp.gmail.com'
#eposta_sunucu=smtplib.SMTP_SSL(host=host,port=port,context=context)
#eposta_sunucu.login(kullanici,sifre)
#eposta_sunucu.sendmail(kullanici,alici,mesaj )
baslik='baslik'
#google sifre
#dqvr lhsg kqoz zquw


#  EKLENTİLİ EPOSTA GONDERİMİ
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

posta=MIMEMultipart()
posta['From']=kullanici
posta['To']=alici
posta['Subject']=baslik
posta.attach(MIMEText(mesaj,'plain'))
eklenti_dosya_ismi='yeni_dosya.txt'

with(open(eklenti_dosya_ismi,'rb'))as eklenti_dosyasi:
    payload=MIMEBase('application','octate-stream')
    payload.set_payload((eklenti_dosyasi).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition','attachment',filename=eklenti_dosya_ismi)
    posta.attach(payload)
    posta_str=posta.as_string()

port=465
host='smtp.gmail.com'
eposta_sunucu=smtplib.SMTP_SSL(host=host,port=port,context=context)
eposta_sunucu.login(kullanici,sifre)
eposta_sunucu.sendmail(kullanici,alici,posta_str)






