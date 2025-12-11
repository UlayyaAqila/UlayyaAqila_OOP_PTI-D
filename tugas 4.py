class mhs_alumni:
    def __init__(self):
        self.lulus_tahun = 2025

class mahasiswa_aktif:
    def __init__(self):
        self.masuk_tahun = 2024

class ktm(mhs_alumni, mahasiswa_aktif):
    def __init__(self, nama):
        mhs_alumni.__init__(self)
        mahasiswa_aktif.__init__(self)
        self.nama = nama

class ijazah(mhs_alumni, mahasiswa_aktif):
    def __init__(self, nama):
        mhs_alumni.__init__(self)
        mahasiswa_aktif.__init__(self)
        self.nama = nama

class beasiswa(mhs_alumni, mahasiswa_aktif):
    def __init__(self, nama, jenis_beasiswa):
        mhs_alumni.__init__(self)
        mahasiswa_aktif.__init__(self)
        self.nama = nama
        self.jenis_beasiswa = jenis_beasiswa

ktm_obj = ktm("Leti Mutia")
print(f"KTM: {ktm_obj.nama}, Masuk: {ktm_obj.masuk_tahun}, Lulus: {ktm_obj.lulus_tahun}")

ijazah_obj = ijazah("Abdalis Sani")
print(f"Ijazah: {ijazah_obj.nama}, Masuk: {ijazah_obj.masuk_tahun}, Lulus: {ijazah_obj.lulus_tahun}")

beasiswa_obj = beasiswa("Aqila Cantik", "Prestasi")
print(f"Beasiswa: {beasiswa_obj.nama}, Jenis: {beasiswa_obj.jenis_beasiswa}, Masuk: {beasiswa_obj.masuk_tahun}, Lulus: {beasiswa_obj.lulus_tahun}")    