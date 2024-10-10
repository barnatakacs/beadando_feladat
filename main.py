from legitarsasag import LegiTarsasag
from adat_letrehozas import Adat
from gui import AdatApp
import customtkinter as ctk


def main():
    #legitarsasag = LegiTarsasag('KLM')
    #adat = Adat(legitarsasag)
    #adat.start()

    legi_tarsasag = LegiTarsasag("KLM")
    app = AdatApp(ctk.CTk(), legi_tarsasag)
    app.root.mainloop()

if __name__ == "__main__":
    main()
