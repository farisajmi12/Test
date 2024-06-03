# Soal 2:
# Deskripsi:
# Sebuah perusahaan ingin mengelola data karyawannya. Buatlah kelas Karyawan dengan atribut
# dan metode yang sesuai. Implementasikan fungsi hitung_gaji yang menghitung gaji karyawan
# berdasarkan jam kerja dan tarif gaji.
# Persyaratan:
# • Kelas Karyawan harus memiliki atribut seperti nama, jabatan, jam_kerja, dan
# tarif_gaji.
# • Fungsi hitung_gaji harus menerima objek Karyawan sebagai parameter.
# • Fungsi hitung_gaji harus menghitung gaji karyawan dengan rumus: gaji =
# jam_kerja * tarif_gaji.
# • Cetak informasi tentang gaji karyawan yang dihitung.
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
karyawan1 = Karyawan("Faris", "Manager", 160, 70000)
karyawan2 = Karyawan("Hendro", "Supervisor", 180, 50000 )
cetak_informasi_gaji(karyawan1)
cetak_informasi_gaji(karyawan2)

