#buatlah sebuah class untuk segitiga siku siku dengan atribut alas dan tinggi dan methodnya keliling dan luas

import math

class SegitigaSikuSiku:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi_miring = self._hitung_sisi_miring()

    def _hitung_sisi_miring(self):
        return math.sqrt(self.alas ** 2 + self.tinggi ** 2)

    def keliling(self):
        return self.alas + self.tinggi + self.sisi_miring

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Contoh penggunaan
segitiga1 = SegitigaSikuSiku(3, 4)
print("Alas:", segitiga1.alas)
print("Tinggi:", segitiga1.tinggi)
print("Sisi Miring:", segitiga1.sisi_miring)
print("Keliling:", segitiga1.keliling())
print("Luas:", segitiga1.luas())