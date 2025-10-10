class SepedaMotor:
    def __init__(self, nama_motor):
        self.nama_motor = nama_motor
        self.mesin_nyala = False
        self.kecepatan = 0
        self.bahan_bakar = 100
        self.jarak_tempuh = 0

    def nyalakan_mesin(self):
        if not self.mesin_nyala:
            self.mesin_nyala = True
            print(f"🔑 Mesin {self.nama_motor} dinyalakan.")
        else:
            print(f"⚙️ Mesin {self.nama_motor} sudah menyala.")

    def matikan_mesin(self):
        if self.mesin_nyala:
            self.mesin_nyala = False
            self.kecepatan = 0
            print(f"🔚 Mesin {self.nama_motor} dimatikan.")
        else:
            print(f"⚠️ Mesin {self.nama_motor} sudah mati.")

    def gas(self, tambah):
        if not self.mesin_nyala:
            print(f"❌ Nyalakan mesin {self.nama_motor} dulu sebelum gas.")
            return
        if self.bahan_bakar <= 0:
            print(f"⛽ Bahan bakar {self.nama_motor} habis! Tidak bisa jalan.")
            return

        self.kecepatan += tambah
        if self.kecepatan > 120:
            self.kecepatan = 120
            print(f"🚀 {self.nama_motor} mencapai kecepatan maksimum (120 km/jam)!")
        else:
            print(f"🏍️ Kecepatan {self.nama_motor} sekarang: {self.kecepatan} km/jam")

        self.bahan_bakar -= tambah * 0.5
        self.jarak_tempuh += tambah * 0.2
        if self.bahan_bakar < 0:
            self.bahan_bakar = 0

    def rem(self, kurang):
        if self.kecepatan > 0:
            self.kecepatan -= kurang
            if self.kecepatan < 0:
                self.kecepatan = 0
            print(f"🛑 Kecepatan {self.nama_motor} sekarang: {self.kecepatan} km/jam")
        else:
            print(f"✅ {self.nama_motor} sudah berhenti.")

    def status(self):
        print(f"""
==== STATUS MOTOR {self.nama_motor} ====
Mesin       : {'Nyala' if self.mesin_nyala else 'Mati'}
Kecepatan   : {self.kecepatan} km/jam
Bahan bakar : {self.bahan_bakar:.1f} %
Jarak tempuh: {self.jarak_tempuh:.1f} km
=======================================
""")

# Nama motor langsung ditentukan di sini 👇
motor = SepedaMotor("SCOOPY")

while True:
    print(f"""
==============================
 SIMULASI MOTOR {motor.nama_motor.upper()}
==============================
1. Nyalakan mesin
2. Matikan mesin
3. Gas
4. Rem
5. Lihat status
6. Keluar
==============================
""")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        motor.nyalakan_mesin()
    elif pilihan == "2":
        motor.matikan_mesin()
    elif pilihan == "3":
        try:
            tambah = int(input("Tambah kecepatan berapa km/jam: "))
            motor.gas(tambah)
        except ValueError:
            print("⚠️ Masukkan angka saja!")
    elif pilihan == "4":
        try:
            kurang = int(input("Kurangi kecepatan berapa km/jam: "))
            motor.rem(kurang)
        except ValueError:
            print("⚠️ Masukkan angka saja!")
    elif pilihan == "5":
        motor.status()
    elif pilihan == "6":
        print(f"Terima kasih! Simulasi {motor.nama_motor} selesai 🚦")
        break
    else:
        print("⚠️ Pilihan tidak valid, coba lagi.")
