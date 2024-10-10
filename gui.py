import customtkinter as ctk
from legitarsasag import LegiTarsasag
from belfoldi import BelfoldiJarat
from nemzetkozi import NemzetkoziJarat
import tkinter.messagebox as mb



class AdatApp:
    def __init__(self, root, legi_tarsasag: LegiTarsasag):
        self.legi_tarsasag = legi_tarsasag
        self.root = root
        self.root.title(f"{self.legi_tarsasag.nev} Foglalási Rendszer")
        self.root.geometry("350x450")

        self.label = ctk.CTkLabel(root, font=('Arial', 25), text=f"{self.legi_tarsasag.nev} Foglalási Rendszer")
        self.label.pack(pady=20)

        self.jaratlista_btn = ctk.CTkButton(root, width=220, height=50, font=('Arial', 20), fg_color="#f59842", hover_color='#b54e09', text='Járatok listázása', command=self.jaratok_listazasa)
        self.jaratlista_btn.pack(pady=10)

        self.foglalaslista_btn = ctk.CTkButton(root, width=220, height=50, font=('Arial', 20), fg_color='#f59842', hover_color='#b54e09', text='Foglalások listázása', command=self.foglalasok_listazasa)
        self.foglalaslista_btn.pack(pady=10)

        self.foglalas_btn = ctk.CTkButton(root, width=220, height=50, font=('Arial', 20), fg_color='#f59842', hover_color='#b54e09', text='Foglalás', command=self.foglalas)
        self.foglalas_btn.pack(pady=10)

        self.lemondas_btn = ctk.CTkButton(root, width=220, height=50, font=('Arial', 20), fg_color='#f59842', hover_color='#b54e09', text='Lemondás', command=self.lemondas)
        self.lemondas_btn.pack(pady=10)

        self.kilepes_btn = ctk.CTkButton(root, width=220, height=50, font=('Arial', 20), fg_color='#b50909', hover_color='#660202', text='Kilépés', command=root.quit)
        self.kilepes_btn.pack(pady=10)

        self.jaratok_letrehozasa()
        self.foglalasok_letrehozasa()

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

    def jaratok_listazasa(self):
        jaratok_window = ctk.CTkToplevel(self.root)
        jaratok_window.attributes("-topmost", True)
        jaratok_window.title('Elérhető járatok')
        jaratok_window.geometry('800x400')

        label = ctk.CTkLabel(jaratok_window, font=('Arial', 20), text='Elérhető Járatok:')
        label.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(jaratok_window, width=780, height=320)
        scrollable_frame.pack(pady=10, padx=10)


        for jarat in self.legi_tarsasag.jaratok:
            jarat_label = ctk.CTkLabel(scrollable_frame, corner_radius=5, fg_color='#f59842', width=750, height=40, font=('Arial', 17), text=str(jarat))
            jarat_label.pack(pady=20)

    def foglalas(self):
        foglalas_window = ctk.CTkToplevel(self.root)
        foglalas_window.attributes("-topmost", True)
        foglalas_window.geometry('300x400')
        foglalas_window.title('Foglalás')

        nev_lbl = ctk.CTkLabel(foglalas_window, font=('Arial', 18), text='Utas neve:')
        nev_lbl.pack(pady=5)
        nev_entry = ctk.CTkEntry(foglalas_window)
        nev_entry.pack(pady=10)

        jaratszam_lbl = ctk.CTkLabel(foglalas_window, font=('Arial', 18),  text='Járatszám:')
        jaratszam_lbl.pack(pady=5)
        jaratszam_entry = ctk.CTkEntry(foglalas_window)
        jaratszam_entry.pack(pady=10)

        datum_lbl = ctk.CTkLabel(foglalas_window, font=('Arial', 18),  text='Foglalás dátuma (ÉÉÉÉ-HH-NN):')
        datum_lbl.pack(pady=5)
        datum_entry = ctk.CTkEntry(foglalas_window)
        datum_entry.pack(pady=10)

        indulas_lbl = ctk.CTkLabel(foglalas_window, font=('Arial', 18),  text='Indulás dátuma (ÉÉÉÉ-HH-NN):')
        indulas_lbl.pack(pady=5)
        indulas_entry = ctk.CTkEntry(foglalas_window)
        indulas_entry.pack(pady=10)

        megerosites_btn = ctk.CTkButton(foglalas_window, width=280, height=40, font=('Arial', 18), fg_color='#f59842', hover_color='#b54e09',  text='Foglalás megerősítése', command=lambda: foglalas_megerositese(nev_entry.get(), jaratszam_entry.get().upper(), datum_entry.get(), indulas_entry.get()))
        megerosites_btn.pack(pady=10)

        def foglalas_megerositese(nev, jaratszam, datum, indulas):
            jarat = next((j for j in self.legi_tarsasag.jaratok if j.jaratszam == jaratszam and j.indulas == indulas), None)
            if jarat:
                mb.showinfo('Foglalás', self.legi_tarsasag.foglal(nev, jarat, datum, indulas))
                foglalas_window.destroy()
            else:
                mb.showerror('Hiba', 'Hiba történt, próbálja újra!')

    def lemondas(self):
        lemondas_window = ctk.CTkToplevel(self.root)
        lemondas_window.attributes("-topmost", True)
        lemondas_window.geometry('300x320')
        lemondas_window.title('Lemondás')

        nev_lbl = ctk.CTkLabel(lemondas_window, font=('Arial', 18), text='Utas neve:')
        nev_lbl.pack(pady=5)
        nev_entry = ctk.CTkEntry(lemondas_window)
        nev_entry.pack(pady=10)

        jaratszam_lbl = ctk.CTkLabel(lemondas_window, font=('Arial', 18), text='Járatszám:')
        jaratszam_lbl.pack(pady=5)
        jaratszam_entry = ctk.CTkEntry(lemondas_window)
        jaratszam_entry.pack(pady=10)

        indulas_lbl = ctk.CTkLabel(lemondas_window, font=('Arial', 18), text='Indulás dátuma (ÉÉÉÉ-HH-NN):')
        indulas_lbl.pack(pady=5)
        indulas_entry = ctk.CTkEntry(lemondas_window)
        indulas_entry.pack(pady=10)

        megerosites_btn = ctk.CTkButton(lemondas_window, width=280, height=40, font=('Arial', 18), fg_color='#f59842', hover_color='#b54e09', text='Lemondás megerősítése', command=lambda: lemondas_megerositese(nev_entry.get(), jaratszam_entry.get().upper(), indulas_entry.get()))
        megerosites_btn.pack(pady=10)

        def lemondas_megerositese( nev, jaratszam, indulas):
            mb.showinfo('Lemondás', self.legi_tarsasag.lemond(nev, jaratszam, indulas))
            lemondas_window.destroy()


    def foglalasok_listazasa(self):
        foglalasok_window = ctk.CTkToplevel(self.root)
        foglalasok_window.attributes("-topmost", True)
        foglalasok_window.title('Aktuális Foglalások')
        foglalasok_window.geometry('800x400')

        label = ctk.CTkLabel(foglalasok_window, font=('Arial', 20), text='Aktuális Foglalások:')
        label.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(foglalasok_window, width=780, height=320)
        scrollable_frame.pack(pady=10, padx=10)

        for foglalas in self.legi_tarsasag.foglalasok:
            foglalas_label = ctk.CTkLabel(scrollable_frame, corner_radius=5, fg_color='#f59842', width=750, height=40, font=('Arial', 17), text=str(foglalas))
            foglalas_label.pack(pady=20)




