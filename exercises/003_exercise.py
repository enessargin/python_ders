# ==============================================================================
# HESAP MAKİNESİ PROGRAMI
# ==============================================================================
# Bu program, kullanıcıdan alınan iki sayı ve seçilen işlem numarasına göre
# temel matematiksel hesaplamaları gerçekleştirir.
# ==============================================================================

# %% [1. Menü Ekrana Yazdırma ve Girdilerin Alınması]
# ------------------------------------------------------------------------------
# Üç tırnak (""") kullanarak çok satırlı metinleri (Dostring / Banner) 
# tek bir print içerisinde kolayca düzenleyebiliriz.

print("""-------------------------------------------------
Hesap Makinesi Programına Hoş Geldiniz! 

İşlemler:
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
-------------------------------------------------
""")

# Kullanıcıdan sayı verilerini alıyoruz:
a = int(input("Birinci Sayıyı Giriniz: "))
b = int(input("İkinci Sayıyı Giriniz: "))

# İşlem seçimini metin (string) olarak alıyoruz:
islem = input("Yapmak istediğiniz işlem numarasını giriniz (1-4): ")


# %% [2. Koşullu Bloklar ile Hesaplama]
# ------------------------------------------------------------------------------

if islem == "1":
    # Toplama İşlemi
    toplam = a + b
    print("\n{} ile {} sayısının toplamı: {}".format(a, b, toplam))

elif islem == "2":
    # Çıkarma İşlemi
    fark = a - b
    print("\n{} ile {} sayısının farkı: {}".format(a, b, fark))

elif islem == "3":
    # Çarpma İşlemi
    carpim = a * b
    print("\n{} ile {} sayısının çarpımı: {}".format(a, b, carpim))

elif islem == "4":
    # Bölme İşlemi
    if b == 0:
        # Matematiksel olarak bir sayı 0'a bölünemez (ZeroDivisionError)
        print("\n[HATA] Bir sayı 0'a bölünemez!")
    else:
        bolum = a / b
        print("\n{} sayısının {} sayısına bölümü: {}".format(a, b, bolum))

else:
    # 1, 2, 3 veya 4 dışında bir değer girilirse:
    print("\nLütfen geçerli bir işlem numarası giriniz!")