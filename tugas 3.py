class Person:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def display(self):
        return f"Nama: {self.nama}\nUsia: {self.usia}"


class Lecturer(Person):
    def __init__(self, nama, usia, nidn, mata_kuliah):
        super().__init__(nama, usia)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def teach(self):
        return f"{self.nama} sedang mengajar {self.mata_kuliah}."

    def display(self):
        data = super().display()
        return f"{data}\nNIM: {self.nidn}\nMata Kuliah: {self.mata_kuliah}"


class Student(Person):
    def __init__(self, nama, usia, nim, jurusan):
        super().__init__(nama, usia)
        self.nim = nim
        self.jurusan = jurusan

    def study(self):
        return f"{self.nama} sedang belajar di jurusan {self.jurusan}."

    def display(self):
        data = super().display()
        return f"{data}\nNIM: {self.nim}\nJurusan: {self.jurusan}"


# === DATA SESUAI GAMBAR ===
dosen = Lecturer("Edy", 30, "123456", "Pemrograman Berorientasi Objek")
mahasiswa = Student("Ulayya Aqilah", 19, "24241148", "Pendidikan Teknologi Informasi")

# === OUTPUT ===
print("=== Data Dosen ===")
print(dosen.display())
print(" ", dosen.teach())

print("\n=== Data Mahasiswa ===")
print(mahasiswa.display())
print(" ", mahasiswa.study())university.display_all_data()
