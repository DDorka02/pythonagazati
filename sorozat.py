import random


def listaba():
    lista = []
    for i in range(10):
        szam = random.randrange(10, 350)
        lista.append(szam)
    return lista


def kiir(lista):
    print("II/A, B, C:", end="\n\t")
    for i in range(len(lista)-1):
        print(lista[i], end="#")
    print(lista[-1])


def parosok_szama(lista):
    db = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            db += 1
    return db


def kozol_kiir(db: int):
    print(f"II/D, E: \n\t A párosok száma: {db}")


def file_kiir(db: int):
    f = open("kimutatas.txt", "w", encoding="utf8")
    f.write(f"II/F: \n\t A párosok száma: {db}")
    f.close()
