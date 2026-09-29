
# -----------------------------------------------------------------------------
# 1. DOSYA OKUMA KİPİ ("r") VE HATA YÖNETİMİ
# -----------------------------------------------------------------------------
try:
    file = open("bilgiler.txt", "r")
    file.close()
except FileNotFoundError:
    print("Hata: Okunmak istenen dosya bulunamadı!")

# -----------------------------------------------------------------------------
# 2. FOR DÖNGÜSÜ İLE OKUMA
# -----------------------------------------------------------------------------
print("--- For Döngüsü ile Okuma ---")
try:
    file = open("bilgiler.txt", "r")
    for satir in file:
        print(satir, end="")
    file.close()
except FileNotFoundError:
    print("Dosya bulunamadı.")

# -----------------------------------------------------------------------------
# 3. read() FONKSİYONU
# -----------------------------------------------------------------------------
print("\n\n--- read() Fonksiyonu ile Okuma ---")
try:
    file = open("bilgiler.txt", "r")
    icerik = file.read()
    print("Dosya İçeriği:")
    print(icerik)
    file.close()
except FileNotFoundError:
    print("Dosya bulunamadı.")

# -----------------------------------------------------------------------------
# 4. readline() VE readlines() FONKSİYONLARI
# -----------------------------------------------------------------------------
try:
    file = open("bilgiler.txt", "r")
    print("\n--- readline() ile İlk Satır ---")
    print(file.readline(), end="")
    file.close()

    file = open("bilgiler.txt", "r")
    print("\n--- readlines() ile Liste Halinde Okuma ---")
    satirlar = file.readlines()
    print(satirlar)
    file.close()
except FileNotFoundError:
    print("Dosya bulunamadı.")