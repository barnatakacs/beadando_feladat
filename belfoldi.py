from jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, max_letszam: int, indulas: str):
        super().__init__(jaratszam, celallomas, jegyar * 0.7, max_letszam, indulas)

    def __str__(self):
        return f'Belföldi járat száma: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft, Indulás: {self.indulas}'