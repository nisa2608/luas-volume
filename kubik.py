def hitung_volume_kubus(sisi):
    return sisi ** 3

if __name__ == "__main__":
    s = float(input("Masukkan panjang sisi kubus: "))
    volume = hitung_volume_kubus(s)
    print(f"Volume kubus adalah {volume}")