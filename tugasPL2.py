class manusia: 
    def __init__(self, nama, umur, profesi):
        self.nama = nama
        self.umur = umur
        self.profesi = profesi
        

    def keterangan(self):
        print("Nama saya", self.nama, "berumur", self.umur, "tahun")
    
    def peranan(self):
        print("Profesi saya", self.profesi)

class bertugas(manusia):
    def dokter(self):
        print("Tugas saya adalah membantu menyembuhkan orang sakit")

    def tentara(self):
        print("Tugas saya adalah menjaga pertahanan negara")

    def petani(self):
        print("Tugas saya adalah menanam padi, sayur, atau buah")

dokter = bertugas("Ana", 25, "dokter")
dokter.keterangan()
dokter.peranan()
dokter.dokter()

tentara = bertugas("Felix", 28, "Tentara")
tentara.keterangan()
tentara.peranan()
tentara.tentara()

petani = bertugas("Sumanto", 35, "Petani")
petani.keterangan()
petani.peranan()
petani.petani()