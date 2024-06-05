# class Manusia:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur

#     def sapa(self):
#         print(f'Halo, nama saya {self.nama} dan umur saya {self.umur} tahun')

# Manusia1 = Manusia('Budi', 20)
# Manusia2 = Manusia('Andi', 22)

# Manusia1.sapa()
# Manusia2.sapa()

# class hewan:
#     def __init__(self, nama):
#         self.nama = nama

#     def suara(self):
#         pass

# class kucing(hewan):
#     def suara(self):
#         return('meow')
    
# class anjing(hewan):
#     def suara(self):
#         return('guk guk')
    
# class ayam(hewan):
#     def suara(self):
#         return('kukuruyuk')
    
# kucing = kucing("momo")
# anjing = anjing("donggo")
# ayam = ayam("cocka")

# print(f'{kucing.nama} bersuara {kucing.suara()}')
# print(f'{anjing.nama} bersuara {anjing.suara()}')
# print(f'{ayam.nama} bersuara {ayam.suara()}')

# buat program baru dengan class dan didalamnya ada sub class

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
    def prodi(self):
        pass
    def angkatan(self):
        pass

class Mahasiswa1(Mahasiswa):
    def prodi(self):
        return('teknik nuklir')
    def angkatan (self):
        return(2023)
class Mahasiswa2(Mahasiswa):
    def prodi(self):
        return('teknik mesin')
    def angkatan (self):
        return(2022)
class Mahasiswa3(Mahasiswa):
    def prodi(self):
        return('sastra inggris')
    def angkatan (self):
        return(2022)
mahasiswa1 = Mahasiswa1('budi')
mahasiswa2 = Mahasiswa2('wati')
mahasiswa3 = Mahasiswa3('ratna')

print(mahasiswa1.prodi())
print(f'{mahasiswa1.nama} adalah mahasiswa dari prodi {mahasiswa1.prodi()} angkatan {mahasiswa1.angkatan()}')
print(f'{mahasiswa2.nama} adalah mahasiswa dari prodi {mahasiswa2.prodi()} angkatan {mahasiswa2.angkatan()}')
print(f'{mahasiswa3.nama} adalah mahasiswa dari prodi {mahasiswa3.prodi()} angkatan {mahasiswa3.angkatan()}')