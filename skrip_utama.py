from luas.segitiga import hitung_luas as hitung_luas_segitiga
from luas.persegi import hitung_luas_persegi
from luas.lingkaran import hitung_luas_lingkaran
from volume.trapesium import hitung_luas_trapesium
from volume.bola import hitung_volume_bola
from volume.kubik import hitung_volume_kubus

print("=== Pilih operasi ===")
print("1. Luas Segitiga")
print("2. Luas Persegi")
print("3. Luas Lingkaran")
print("4. Luas Trapesium")
print("5. Volume Bola")
print("6. Volume Kubik")

pilih = input("Masukkan pilihan (1-6): ")

if pilih == "1":
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    print("Luas segitiga:", hitung_luas_segitiga(alas, tinggi))

elif pilih == "2":
    sisi = float(input("Masukkan sisi: "))
    print("Luas persegi:", hitung_luas_persegi(sisi))

elif pilih == "3":
    r = float(input("Masukkan jari-jari: "))
    print("Luas lingkaran:", hitung_luas_lingkaran(r))

elif pilih == "4":
    a = float(input("Masukkan sisi atas: "))
    b = float(input("Masukkan sisi bawah: "))
    t = float(input("Masukkan tinggi: "))
    print("Luas trapesium:", hitung_luas_trapesium(a, b, t))

elif pilih == "5":
    r = float(input("Masukkan jari-jari: "))
    print("Volume bola:", hitung_volume_bola(r))

elif pilih == "6":
    sisi = float(input("Masukkan sisi: "))
    print("Volume kubik:", hitung_volume_kubus(sisi))

else:
    print("Pilihan tidak tersedia.")
    