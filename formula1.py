from Balkez import Balkez


def listaba():
    lista = []
    f = open("kimutatas.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    for i in range(len(sorok)):
        bal = Balkez(sorok[i])
        lista.append(bal)
    return lista


def kiir(lista: list[Balkez]):
    print(f"III/A, B: \n\t A balkezesek száma: {len(lista)}")
