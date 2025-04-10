'''
for sayi in range(1,100+1):
    print(sayi)
    sayi+=1
'''
'''
def harfleri_yazdir():

    kelime=input('Bir kelime yazin: ')

    for harf in kelime:
        print(harf)

harfleri_yazdir()

print(harfleri_yazdir())
'''
'''
def carpim_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i * j:5}", end=" ")  # Her sonucu 5 karakterlik alan içinde yaz
            print()
print(carpim_tablosu())
'''
'''
def cift_tek():
    sayi=input('Bir sayi girin: ')
    sayi=int(sayi)

    for x in range(1,sayi+1):
        if x%2==0:
            print('Çift sayi',x)
        else:
            print('Tek sayi', x)
print(cift_tek())
'''
'''
def fibonacci():
    fibonacci=[0, 1,]

    for _ in range(2,100):
        yeni_sayi = (fibonacci[-1]) + (fibonacci[-2])
        fibonacci.append(yeni_sayi)
        if len(fibonacci)>10:
            break
    return fibonacci
print(fibonacci())
'''




