from jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, max_letszam: int, indulas: str):
        super().__init__(jaratszam, celallomas, jegyar * 1.2, max_letszam, indulas)

    def __str__(self):
        return f'Nemzetközi járat száma: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft, Indulás: {self.indulas}'