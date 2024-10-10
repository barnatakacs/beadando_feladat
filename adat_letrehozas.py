from legitarsasag import LegiTarsasag
from belfoldi import BelfoldiJarat
from nemzetkozi import NemzetkoziJarat

class Adat:
    def __init__(self, legi_tarsasag: LegiTarsasag):
        self.legi_tarsasag = legi_tarsasag

    def jaratok_letrehozasa(self):
        belfoldi_jaratok = [
            BelfoldiJarat('HU123', 'Budapest', 15000, 10, '2024-11-01'),
            BelfoldiJarat('HU456', 'Debrecen', 12000, 10, '2024-11-05'),
            BelfoldiJarat('HU789', 'Szeged', 13000, 10, '2024-12-07'),
            BelfoldiJarat('HU789', 'Szeged', 13000, 10, '2024-12-06'),
        ]

        nemzetkozi_jaratok = [
            NemzetkoziJarat('EU101', 'Varsó', 25000, 12, '2024-11-23'),
            NemzetkoziJarat('EU202', 'Barcelona', 30000, 12, '2024-11-24'),
            NemzetkoziJarat('EU303', 'London', 35000, 12, '2024-11-12'),
        ]

        for jarat in belfoldi_jaratok + nemzetkozi_jaratok:
            self.legi_tarsasag.jarat_hozzaad(jarat)

    def foglalasok_letrehozasa(self):
        self.legi_tarsasag.foglal('Kovács Béla', self.legi_tarsasag.jaratok[0], '2024-10-01', '2024-11-23')
        self.legi_tarsasag.foglal('Németh Anna', self.legi_tarsasag.jaratok[1], '2024-10-05',  '2024-11-24')
        self.legi_tarsasag.foglal('Szabó Péter', self.legi_tarsasag.jaratok[2], '2024-09-30', '2024-11-01')
        self.legi_tarsasag.foglal('Kiss Zoltán', self.legi_tarsasag.jaratok[3], '2024-10-10', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')
        self.legi_tarsasag.foglal('Tóth Éva', self.legi_tarsasag.jaratok[3], '2024-10-15', '2024-12-06')
        self.legi_tarsasag.foglal('Varga László', self.legi_tarsasag.jaratok[3], '2024-10-20', '2024-12-06')


    def start(self):
        self.jaratok_letrehozasa()
        self.foglalasok_letrehozasa()

        while True:
            print(f'\nÜdvözöljük a {self.legi_tarsasag.nev} légitársaság foglalási rendszerében')
            print('1 > Járatok listázása')
            print('2 > Foglalás')
            print('3 > Foglalás lemondása')
            print('4 > Foglalások listázása')
            print('5 > Kilépés')

            valasztas = input('Válasszon a fenti opciók közül!')

            if valasztas == '1':
                print('Elérhető járatok:')
                self.legi_tarsasag.jaratok_listaz()

            elif valasztas == '2':
                nev = input('Adja meg az utas nevét: ')
                jaratszam = input('Adja meg a járat számát: ')
                datum = input('Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ')
                indulas = input('Adja meg a indulás dátumát (ÉÉÉÉ-HH-NN): ')

                jarat = next((j for j in self.legi_tarsasag.jaratok if j.jaratszam == jaratszam and j.indulas==indulas), None)
                if jarat:
                    foglalas_eredmeny = self.legi_tarsasag.foglal(nev, jarat, datum, indulas)
                    print(foglalas_eredmeny)
                else:
                    print('A megadott járatszám nem létezik.')

            elif valasztas == '3':
                nev = input('Adja meg az utas nevét: ')
                jaratszam = input('Adja meg a járat számát: ')
                indulas = input('Adja meg a indulás dátumát: ')
                lemondas_eredmeny = self.legi_tarsasag.lemond(nev, jaratszam, indulas)
                print(lemondas_eredmeny)

            elif valasztas == '4':
                print('\nAktuális foglalások:')
                foglalasok = self.legi_tarsasag.foglalasok_listaz()
                print(foglalasok)

            elif valasztas == '5':
                print('Kilépés...')
                break

            else:
                print('Érvénztelen választás.')