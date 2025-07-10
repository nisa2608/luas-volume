import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

if __name__ == "__main__":
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = hitung_luas_lingkaran(r)
    print(f"Luas lingkaran adalah {luas}")