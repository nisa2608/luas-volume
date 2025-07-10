def hitung_luas(alas, tinggi):
    return 0.5 * alas * tinggi

if __name__ == "__main__":
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = hitung_luas(alas, tinggi)
    print(f"Luas segitiga adalah: {luas}")