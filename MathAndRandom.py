import random
import math
from collections import Counter

#print(help(random))
#print(help(math))
#print(random.__dir__())

#print(random.random())  #0-1
#print(random.uniform(5,15))  #5-15
#print(random.randint(5,15))
#print(random.randint(5,15))
#print(random.choice(range(1,10)))
#print(random.sample(range(10),k=4)) #random 4 sayı

#liste=[*range(1,10)]
#print(liste)
#random.shuffle(liste)
#print(liste)

#print(math.ceil(54.2)) # yukarı yuvarlama
#print(math.floor(54.2)) # tabana yuvarlama
#print(math.factorial(5))
#print(math.pow(3,2))# 3 ün 2. kuvveti ==3**2

list1 = random.sample(range(10), k=4)
list2 = random. sample(range(10), k=4)
list3 = random. sample(range(10), k=4)
list4 = random. sample(range(10), k=4)

liste_listesi = [list1, list2, list3, list4]
list_toplam = list1 + list2 + list3 + list4
print(liste_listesi)
print(list_toplam)

for index,liste in enumerate(liste_listesi):
    print('{}.liste \t {}'.format(index+1,liste))
print(Counter(list_toplam))  #hangi sayıdan kaç tane old. sayar sayac

sarki="""Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev"""
sarki=sarki.lower()
print(Counter(sarki.split()).most_common())




