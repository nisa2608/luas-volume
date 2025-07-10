import math

def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

if __name__ == "__main__":
    r = float(input("Masukkan jari-jari bola: "))
    volume = hitung_volume_bola(r)
    print(f"Volume bola adalah {volume}")