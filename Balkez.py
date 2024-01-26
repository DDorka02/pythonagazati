# név;első;utolsó;súly (fontban);magasság (inchben)
class Balkez():
    def __init__(self, sor: str):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.elso = adatok[1]
        self.utolso = adatok[2]
        self.suly = int(adatok[3])
        self.magassag = int(adatok[4])
