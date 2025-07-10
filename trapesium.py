def hitung_luas_trapesium(a, b, t):
    return 0.5 * (a + b) * t

if __name__ == "__main__":
    a = float(input("Masukkan panjang sisi atas (a): "))
    b = float(input("Masukkan panjang sisi bawah (b): "))
    t = float(input("Masukkan tinggi (t): "))
    
    luas = hitung_luas_trapesium(a, b, t)
    print(f"Luas trapesium adalah {luas}")