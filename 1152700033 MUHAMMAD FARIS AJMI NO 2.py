class Karyawan:
    def __init__(self, nama, jabatan, jam_kerja, tarif_gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.jam_kerja = jam_kerja
        self.tarif_gaji = tarif_gaji

def hitung_gaji(karyawan):
    gaji = karyawan.jam_kerja * karyawan.tarif_gaji
    return gaji

def cetak_informasi_gaji(karyawan):
    gaji = hitung_gaji(karyawan)
    print(f"Nama: {karyawan.nama}")
    print(f"Jabatan: {karyawan.jabatan}")
    print(f"Jam Kerja: {karyawan.jam_kerja}")
    print(f"Tarif Gaji: {karyawan.tarif_gaji}")
    print(f"Gaji: {gaji}")
    print("=" * 30)

# Contoh penggunaan
karyawan1 = Karyawan("Faris", "Supervisor", 170, 40000)
karyawan2 = Karyawan("Emir", "Administrasi", 150, 35000)
karyawan3 = Karyawan("Dio", "Teknisi", 180, 45000)

cetak_informasi_gaji(karyawan1)
cetak_informasi_gaji(karyawan2)
cetak_informasi_gaji(karyawan3)
