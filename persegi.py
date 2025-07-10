def hitung_luas_persegi(sisi):
    return sisi * sisi

if __name__ == "__main__":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = hitung_luas_persegi(sisi)
    print(f"Luas persegi adalah {luas}")