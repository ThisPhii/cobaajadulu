class kendaraan: 
    def __init__(self, nama, warna, harga):
        self.nama = nama
        self.warna = warna
        self.harga = harga

    def tampilkan(self):
        print("Rincian: ", self.nama, self.warna, self.harga)

    def kecepatanmaxpertama(self):
        print("kecepatan maximum kendaraan: ", self.nama, "adalah 150km/jam")

    def gantigearpertama(self):
        print("gantigear maximum kendaraan adalah sampai 6")
    
class mobil(kendaraan):
    def kecepatanmaxkedua(self):
        print("kecepatan maximum kendaraan: ", self.nama, "adalah 200km/jam")

    def gantigearkedua(self):
        print("gantigear maximum kendaraan adalah sampai 7")

#objek mobil
Avanza = mobil("Avanza", "Putih", 20000000)
Avanza.tampilkan()
Avanza.kecepatanmaxpertama()
Avanza.gantigearpertama()

jeep = mobil("jeep", "coklat", 30000000)
jeep.tampilkan()
jeep.kecepatanmaxkedua()
jeep.gantigearkedua()
