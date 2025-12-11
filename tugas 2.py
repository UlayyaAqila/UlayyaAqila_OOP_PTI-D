class SepedaMotor:
    # Variabel kelas (class variables)
    jumlah_motor = 0  # Menghitung jumlah total sepeda motor
    jenis_surat_lengkap = ["STNK", "BPKB", "Asuransi"]  # Daftar surat yang dianggap lengkap
    pabrikan = ["Honda", "Yamaha", "Suzuki", "Kawasaki"]  # Daftar pabrikan umum

    def __init__(self, merk, model, cc, tahun, warna, surat):
        # Menambah jumlah motor setiap instance baru dibuat
        SepedaMotor.jumlah_motor += 1
        
        # Variabel instan (instance variables)
        self.merk = merk
        self.model = model
        self.cc = cc
        self.tahun = tahun
        self.warna = warna
        self.surat = surat
        self.nomor_unit = SepedaMotor.jumlah_motor  # Setiap motor mendapat nomor unit unik
        self.kelengkapan_surat = self._cek_kelengkapan_surat()
    
    def _cek_kelengkapan_surat(self):
        """Method untuk mengecek kelengkapan surat"""
        return "Lengkap" if all(surat in self.surat for surat in self.jenis_surat_lengkap) else "Tidak Lengkap"

    def tampilkan_info(self):
        print(f"\nInfo Motor Unit #{self.nomor_unit}")
        print(f"Motor: {self.merk} {self.model}")
        print(f"CC: {self.cc} | Tahun: {self.tahun} | Warna: {self.warna}")
        print(f"Surat yang dimiliki: {', '.join(self.surat)}")
        print(f"Status Kelengkapan Surat: {self.kelengkapan_surat}")
        print("-" * 30)

    @classmethod
    def tampilkan_info_kelas(cls):
        """Method kelas untuk menampilkan informasi umum"""
        print("\nInformasi Umum Sepeda Motor:")
        print(f"Total unit terdaftar: {cls.jumlah_motor}")
        print(f"Pabrikan yang dikenal: {', '.join(cls.pabrikan)}")
        print(f"Surat lengkap yang diperlukan: {', '.join(cls.jenis_surat_lengkap)}")
        print("-" * 30)

motor1 = SepedaMotor(
    merk="Honda",
    model="Beat",
    cc="110",
    tahun="2022",
    warna="Merah",
    surat=["STNK", "BPKB", "Asuransi"]
)

motor2 = SepedaMotor(
    merk="Yamaha",
    model="Mio",
    cc="125",
    tahun="2021",
    warna="Hitam",
    surat=["STNK", "BPKB"]
)

print("Daftar Sepeda Motor:")
SepedaMotor.tampilkan_info_kelas()  # Menampilkan informasi kelas terlebih dahulu
motor1.tampilkan_info()
motor2.tampilkan_info()

# Mengakses variabel kelas
print(f"\nTotal sepeda motor yang terdaftar: {SepedaMotor.jumlah_motor}")