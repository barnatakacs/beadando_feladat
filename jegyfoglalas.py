from jarat import Jarat

class JegyFoglalas:
    def __init__(self, utas_nev: str, jarat: Jarat, datum: str, indulas: str):

        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum
        self.indulas = indulas

    def __str__(self):
        return f'Név: {self.utas_nev}, Járat: {self.jarat.jaratszam}, Indulás: {self.indulas}, Foglalás dátuma: {self.datum}'






