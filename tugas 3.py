# NILAI KULIAH
nilai = float(input("Masukkan nilai Anda (0–100): "))

if nilai > 100 or nilai < 0:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("Nilai Anda: A")
elif nilai >= 80:
    print("Nilai Anda: A-")
elif nilai >= 75:
    print("Nilai Anda: B+")
elif nilai >= 70:
    print("Nilai Anda: B")
elif nilai >= 65:
    print("Nilai Anda: B-")
elif nilai >= 60:
    print("Nilai Anda: C+")
elif nilai >= 55:
    print("Nilai Anda: C")
elif nilai >= 50:
    print("Nilai Anda: C-")
elif nilai >= 40:
    print("Nilai Anda: D")
else:
    print("Nilai Anda: E")