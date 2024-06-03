class Buku:
    def __init__(self, judul, penulis, harga, stok):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.stok = stok

class Pelanggan:
    def __init__(self, nama, alamat, saldo):
        self.nama = nama
        self.alamat = alamat
        self.saldo = saldo

def beli_buku(buku, pelanggan):
    if buku.stok > 0:
        if pelanggan.saldo >= buku.harga:
            pelanggan.saldo -= buku.harga
            buku.stok -= 1
            print(f"Pembelian berhasil!")
            print(f"{pelanggan.nama} telah membeli buku '{buku.judul}' seharga {buku.harga}.")
            print(f"Sisa saldo {pelanggan.nama}: {pelanggan.saldo}")
            print(f"Sisa stok buku '{buku.judul}': {buku.stok}")
        else:
            print(f"Saldo tidak cukup untuk membeli buku '{buku.judul}'.")
            print(f"Saldo {pelanggan.nama}: {pelanggan.saldo}, Harga buku: {buku.harga}")
    else:
        print(f"Stok buku '{buku.judul}' habis.")

# Contoh penggunaan
buku1 = Buku("Pemrograman Python", "Guido van Rossum", 150000, 10)
buku2 = Buku("Pemrograman Java", "James Gosling", 200000, 5)

pelanggan1 = Pelanggan("Faris", "Jl. Merdeka No. 10", 300000)
pelanggan2 = Pelanggan("Revina", "Jl. Sudirman No. 20", 100000)

beli_buku(buku1, pelanggan1)
print("\n")
beli_buku(buku2, pelanggan2)
print("\n")
beli_buku(buku1, pelanggan2)
