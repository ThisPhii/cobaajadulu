# from abc import ABC, abstractmethod

# class Bentuk(ABC):
#     @abstractmethod
#     def luas(self):
#         pass

#     def keliling(self):
#         pass

# class Persegi(Bentuk):
#     def __init__(self, sisi):
#         self.sisi = sisi

#     def luas(self):
#         return self.sisi * self.sisi
    
#     def keliling(self):
#         return 4 * self.sisi
    
# class Lingkaran(Bentuk):
#     def __init__(self, jari):
#         self.jari = jari

#     def luas(self):
#         return 3.14 * (self.jari ** 2)
    
#     def keliling(self):
#         return 2 * 3.14 * self.jari
    
# Persegi = Persegi(10)
# Lingkaran = Lingkaran(30)

# print("Luas Persegi:",Persegi.luas())
# print("Keliling Persegi:", Persegi.keliling())
# print("Luas Lingkaran:", Lingkaran.luas())
# print("Keliling Lingkaran:", Lingkaran.keliling())

from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self, judul, tahun_terbit):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        
    @abstractmethod
    def deskripsi(self):
        pass

class Buku(ItemPerpustakaan):
    def __init__(self, judul, tahun_terbit, pengarang, jumlah_halaman):
        super().__init__(judul, tahun_terbit,)
        self.pengarang = pengarang
        self.jumlah_halaman = jumlah_halaman

    def deskripsi(self):
        return(f"Buku : {self.judul},"
               f"tahun terbit : {self.tahun_terbit},"
               f"pengarang : {self.pengarang},"
               f"jumlah halaman : {self.jumlah_halaman}")

class Majalah(ItemPerpustakaan):
    def __init__(self, judul, tahun_terbit, edisi, penerbit):
        super().__init__(judul, tahun_terbit)
        self.edisi = edisi
        self.penerbit = penerbit

    def deskripsi(self):
        return(f"Buku : {self.judul},"
               f"tahun terbit: {self.tahun_terbit},"
               f"edisi : {self.edisi},"
               f"penerbit : {self.penerbit}")


Buku1 = Buku ("Pemrograman dasar Python" , 2015 , "Van Rossum" , 200)
Majalah1 = Majalah ("Si Bobo" , 2001 , "bulan mei" , "Kompas gramedia")

print(Buku1.deskripsi())
print(Majalah1.deskripsi())



