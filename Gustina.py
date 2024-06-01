povrsinaZemlje1=int(input("Unesite povrsinuZemlje1-----"))
brojStanovnika1=int(input("Unesite brojStanovnika1-----"))
povrsinaZemlje2=int(input("Unesite povrsinuZemlje2-----"))
brojStanovnika2=int(input("Unesite brojStanovnika2-----"))
Gustina1=(povrsinaZemlje1/brojStanovnika1)
Gustina2=(povrsinaZemlje2/brojStanovnika2)
print(Gustina1)
print(Gustina2)
if(Gustina1>Gustina2):
    print("1. drzava ima vise")
else:
    print("2. drzava ima vise")
