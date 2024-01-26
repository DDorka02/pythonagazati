import random


def film():
    print("I/A: ")
    nev = input("\tRendező neve: ")
    cim = input("\tFilm címe: ")
    print("I/B:")


def veletlen_szam():
    pont = random.randrange(0, 10)
    print(f"\tPontozás (0-10):{pont}")
    if pont < 4:
        print("\tGyenge film.")
    elif pont < 8:
        print("\tÉrdemes megnézni")
    else:
        print("\tKihagytatlan film!")
