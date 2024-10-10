from jarat import Jarat
from datetime import datetime
from jegyfoglalas import JegyFoglalas

class LegiTarsasag:
    def __init__(self, nev: str):

        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def foglal(self, utas_nev: str, jarat: Jarat, datum: str, indulas: str):
        if not self.jarat_ellenorzes(jarat, indulas):
            return f'A {jarat.jaratszam} számú járaton nincs hely.'

        if self.datum_ellenorzes(datum):
            foglalas = JegyFoglalas(utas_nev, jarat, datum, indulas)
            self.foglalasok.append(foglalas)
            return 'Sikeres foglalás.'
        return 'Érvénytelen dátum.'

    def lemond(self, utas_nev: str, jaratszam: str, indulas: str):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam and foglalas.indulas == indulas:
                self.foglalasok.remove(foglalas)
                return f'Foglalás lemondva.'
        return f'Nem létezik a foglalás.'

    def foglalasok_listaz(self):
        if not self.foglalasok:
            return 'Nincs foglalás jelenleg.'

        foglalas_list = []
        for foglalas in self.foglalasok:
            foglalas_list.append(f'{foglalas.utas_nev}, {foglalas.jarat.jaratszam}, {foglalas.datum}')

        return '\n'.join(foglalas_list)

    @staticmethod
    def datum_ellenorzes(datum: str):
        try:
            foglalas_datum = datetime.strptime(datum, '%Y-%m-%d')
            return foglalas_datum >= datetime.now()
        except ValueError:
            return False

    def jarat_ellenorzes(self, jarat: Jarat, indulas:str):
        letszam = 0
        for foglalas in self.foglalasok:
            if foglalas.jarat == jarat and foglalas.jarat.indulas == indulas:
                letszam += 1
        if jarat.max_letszam > letszam:
            return True
        return False

    def jarat_hozzaad(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def jaratok_listaz(self):
        for jarat in self.jaratok:
            print(jarat)