def deco(f):

    def wrapper():
        print('Baslangic')
        f()
        print('Bitiş')
    return wrapper
#Decorator
@deco
def yazdir():
    print('Yazdir')

yazdir()