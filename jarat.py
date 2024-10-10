from abc import ABC

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float, max_letszam: int, indulas: str):

        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.max_letszam = max_letszam
        self.indulas = indulas

