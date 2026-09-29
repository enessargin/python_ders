# ==============================================================================
# PROGRAMLAMA ÖDEVİ - KOŞULLU DURUMLAR (ÇÖZÜMLER)
# ==============================================================================
# Bu dosya ödev sorularının eksiksiz ve açıklamalı çözümlerini içermektedir.
# ==============================================================================

# %% [Problem 1: Beden Kitle İndeksi (BKİ) - Çözüm]
# ------------------------------------------------------------------------------
print("=" * 45)
print("     PROBLEM 1: BEDEN KİTLE İNDEKSİ HESAPLAMA     ")
print("=" * 45)

boy = float(input("Lütfen boyunuzu metre cinsinden giriniz (Örn: 1.74): "))
kilo = float(input("Lütfen kilonuzu kg cinsinden giriniz (Örn: 76): "))

bki = kilo / (boy ** 2)

print("\nBeden Kitle İndeksiniz: {:.2f}".format(bki))

if bki < 18.5:
    print("Kategori: Zayıf")
elif 18.5 <= bki < 25:
    print("Kategori: Normal")
elif 25 <= bki < 30:
    print("Kategori: Fazla Kilolu")
else:
    print("Kategori: Obez")


# %% [Problem 2: En Büyük Sayıyı Bulma - Çözüm]
# ------------------------------------------------------------------------------
print("\n" + "=" * 45)
print("        PROBLEM 2: EN BÜYÜK SAYIYI BULMA        ")
print("=" * 45)

a = int(input("1. Sayıyı giriniz (a): "))
b = int(input("2. Sayıyı giriniz (b): "))
c = int(input("3. Sayıyı giriniz (c): "))

if a >= b and a >= c:
    en_buyuk = a
elif b >= a and b >= c:
    en_buyuk = b
else:
    en_buyuk = c

print("\nGirilen sayılar ({}, {}, {}) arasındaki en büyük sayı: {}".format(a, b, c, en_buyuk))


# %% [Problem 3: Harf Notu Hesaplama - Çözüm]
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print("        PROBLEM 3: HARF NOTU HESAPLAMA SİSTEMİ        ")
print("=" * 50)

vize1 = float(input("1. Vize Notunuzu Giriniz: "))
vize2 = float(input("2. Vize Notunuzu Giriniz: "))
final = float(input("Final Notunuzu Giriniz: "))

genel_not = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)

print("\nGenel Not Ortalamanız: {:.2f}".format(genel_not))

if genel_not >= 90:
    harf_notu = "AA"
elif genel_not >= 85:
    harf_notu = "BA"
elif genel_not >= 80:
    harf_notu = "BB"
elif genel_not >= 75:
    harf_notu = "CB"
elif genel_not >= 70:
    harf_notu = "CC"
elif genel_not >= 65:
    harf_notu = "DC"
elif genel_not >= 60:
    harf_notu = "DD"
elif genel_not >= 55:
    harf_notu = "FD"
else:
    harf_notu = "FF"

print("Harf Notunuz: {}".format(harf_notu))


# %% [Problem 4: Geometrik Şekil Tespiti - Çözüm]
# ------------------------------------------------------------------------------
print("\n" + "=" * 50)
print("           PROBLEM 4: GEOMETRİK ŞEKİL HESAPLAYICI          ")
print("=" * 50)

sekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz? (Dörtgen / Üçgen): ").strip().capitalize()

if sekil == "Dörtgen":
    print("\nLütfen 4 kenar uzunluğunu sırasıyla giriniz:")
    a = float(input("Kenar-1: "))
    b = float(input("Kenar-2: "))
    c = float(input("Kenar-3: "))
    d = float(input("Kenar-4: "))
    
    if a == b == c == d:
        print("\nSonuç: Bu şekil bir KARE'dir.")
    elif (a == c and b == d) or (a == b and c == d) or (a == d and b == c):
        print("\nSonuç: Bu şekil bir DİKDÖRTGEN'dir.")
    else:
        print("\nSonuç: Bu şekil SIRADAN BİR DÖRTGEN'dir.")

elif sekil == "Üçgen":
    print("\nLütfen 3 kenar uzunluğunu giriniz:")
    a = float(input("Kenar-1: "))
    b = float(input("Kenar-2: "))
    c = float(input("Kenar-3: "))
    
    # Üçgen Olma Şartı (Üçgen Eşitsizliği): |a-b| < c < a+b
    is_ucgen = (abs(a - b) < c < a + b) and (abs(a - c) < b < a + c) and (abs(b - c) < a < b + a)
    
    if is_ucgen:
        if a == b == c:
            print("\nSonuç: Bu bir EŞKENAR ÜÇGEN'dir.")
        elif a == b or a == c or b == c:
            print("\nSonuç: Bu bir İKİZKENAR ÜÇGEN'dir.")
        else:
            print("\nSonuç: Bu bir ÇEŞİTKENAR ÜÇGEN'dir.")
    else:
        print("\n[HATA] Bu kenar uzunlukları bir ÜÇGEN BELİRTMİYOR!")

else:
    print("\n[HATA] Geçersiz bir şekil ismi girdiniz. Lütfen 'Dörtgen' veya 'Üçgen' yazınız.")