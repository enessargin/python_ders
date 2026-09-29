# ==============================================================================
# PYTHON PROGRAMLAMA DERS NOTLARI: DÖNGÜLER VE KONTROL İFADELERİ
# ==============================================================================


# %% [1. FOR DÖNGÜLERİ VE 'in' OPERATÖRÜ]
# ------------------------------------------------------------------------------
# 1.1 'in' Operatörü
# 'in' operatörü, bir elemanın liste, demet (tuple) veya string (karakter dizisi)
# içerisinde bulunup bulunmadığını kontrol eder. Sonuç True veya False döner.

print("--- 1.1 'in' Operatörü Örnekleri ---")
print("a" in "merhaba")      # True
print("mer" in "merhaba")    # True
print("t" in "merhaba")      # False
print(4 in [1, 2, 3, 4])     # True
print(10 in [1, 2, 3, 4])    # False
print(4 in (1, 2, 3))        # False

# 1.2 For Döngüsü Temel Yapısı
# For döngüsü; listeler, demetler, stringler ve sözlükler üzerinde gezinmeyi sağlar.
# Genel Yapı:
# for eleman in veri_yapisi:
#     Yapılacak İşlemler

print("\n--- 1.2 Listeler Üzerinde Gezinme ---")
liste = [1, 2, 3, 4, 5, 6, 7]

for eleman in liste:
    print("Eleman:", eleman)

# Liste Elemanlarını Toplama
toplam = 0
for eleman in liste:
    toplam += eleman
print("Liste Elemanlarının Toplamı:", toplam)

# Çift Elemanları Filtreleme
print("\nListe İçindeki Çift Sayılar:")
for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)

# 1.3 Karakter Dizileri (Stringler) Üzerinde Gezinme
print("\n--- 1.3 String Üzerinde Gezinme ---")
s = "Python"
for karakter in s:
    print(karakter)

# Karakterleri Çarparak Yazdırma
for karakter in s:
    print(karakter * 3)

# 1.4 Demetler (Tuples) Üzerinde Gezinme ve Demet Açma (Unpacking)
print("\n--- 1.4 Demet Üzerinde Gezinme ---")
demet = (1, 2, 3, 4, 5)
for eleman in demet:
    print(eleman)

# Çok Boyutlu Demetlerde Pratik Gezinme
liste_demet = [(1, 2), (3, 4), (5, 6), (7, 8)]

print("\nDemet Çiftlerini Birlikte Ekrana Basma:")
for (i, j) in liste_demet:
    print(f"i: {i}, j: {j}")

# Üçlü Demet Elemanlarını Çarpma
liste_uclu = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print("\nÜçlü Demet Elemanlarının Çarpımı:")
for (i, j, k) in liste_uclu:
    print(f"{i} x {j} x {k} = {i * j * k}")

# 1.5 Sözlükler (Dictionary) Üzerinde Gezinme
print("\n--- 1.5 Sözlükler Üzerinde Gezinme ---")
sozluk = {"bir": 1, "iki": 2, "üç": 3, "dört": 4}

# Sadece Anahtarları (Keys) Alma
print("Anahtarlar (Keys):")
for anahtar in sozluk.keys():
    print(anahtar)

# Sadece Değerleri (Values) Alma
print("\nDeğerler (Values):")
for deger in sozluk.values():
    print(deger)

# Anahtar-Değer Çiftlerini (Items) Birlikte Alma
print("\nAnahtar - Değer Çiftleri (Items):")
for (anahtar, deger) in sozluk.items():
    print(f"Anahtar: {anahtar} -> Değer: {deger}")


# %% [2. WHILE DÖNGÜLERİ]
# ------------------------------------------------------------------------------
# While döngüsü, belirtilen koşul 'True' olduğu sürece çalışmaya devam eder.
# Döngünün sonlanması için koşulun bir noktada 'False' olması gerekir.
#
# Genel Yapı:
# while (koşul):
#     İşlem 1
#     İşlem 2

print("\n" + "="*50)
print("--- 2. WHILE DÖNGÜLERİ ---")
print("="*50)

# Sayaç İle Belli Sayıda Döngü Çalıştırma
i = 0
while i < 5:
    print("i'nin değeri:", i)
    i += 1  # Sayaç artırılmazsa sonsuz döngü oluşur!

# İkişer İkişer Sayma
i = 0
while i < 10:
    print("Çift sayı:", i)
    i += 2

# Liste Üzerinde İndeks İle Gezinme
liste = ["Python", "Java", "C++", "JavaScript"]
index = 0
while index < len(liste):
    print(f"İndeks: {index} - Eleman: {liste[index]}")
    index += 1

# UYARI: Sonsuz Döngü (Infinite Loop)
# Aşağıdaki kod bloğunda 'i' değişkeni artırılmadığı için koşul her zaman True kalır
# ve program kilitlenir:
#
# i = 0
# while i < 10:
#     print(i)
#     # i += 1 Unutulursa SONSUZ DÖNGÜ oluşur!


# %% [3. range() FONKSİYONU]
# ------------------------------------------------------------------------------
# range() fonksiyonu; başlangıç, bitiş ve artış miktarına göre sayı dizileri oluşturur.
# Yapısı: range(başlangıç, bitiş, artış_miktarı)
# Not: Bitiş değeri dizilime DAHİL DEĞİLDİR.

print("\n" + "="*50)
print("--- 3. range() FONKSİYONU ---")
print("="*50)

# Temel Kullanımlar
print("range(0, 10):", *range(0, 10))        # 0'dan 9'a kadar
print("range(5, 12):", *range(5, 12))        # 5'ten 11'e kadar
print("range(10):", *range(10))              # Başlangıç verilmezse 0'dan başlar

# Adım Miktarı Belirleme
print("5'ten 20'ye 2'şer artış:", *range(5, 20, 2))
print("5'ten 50'ye 5'er artış:", *range(5, 50, 5))

# Geriye Doğru Sayma (Negatif Adım Miktarı)
print("20'den 1'e geriye doğru:", *range(20, 0, -1))

# range() Yapısını Listeye Dönüştürme
sayi_listesi = list(range(1, 6))
print("Listeye Dönüştürülmüş range:", sayi_listesi)

# range() Fonksiyonunu For Döngüsünde Kullanma
print("\nFor ve range() İle Yıldız Deseni Oluşturma:")
for i in range(1, 6):
    print("* " * i)


# %% [4. DÖNGÜ KONTROL İFADELERİ: break VE continue]
# ------------------------------------------------------------------------------
# 4.1 break İfadesi:
# Döngüyü karşılaşıldığı anda tamamen sonlandırır.
# İç içe döngülerde sadece içinde bulunduğu en içteki döngüyü bitirir.

print("\n" + "="*50)
print("--- 4. break VE continue İFADELERİ ---")
print("="*50)

print("--- 4.1 break Örnekleri ---")

# while ile break kullanımı
i = 0
while i < 20:
    print(i)
    if i == 5:
        print("i == 5 oldu, döngü kırılıyor...")
        break
    i += 1

# for ile break kullanımı
liste = [10, 20, 30, 40, 50]
for sayı in liste:
    if sayı == 30:
        print("30 sayısına ulaşıldı, for döngüsü durduruldu.")
        break
    print("Sayı:", sayı)

# 4.2 continue İfadesi:
# Döngü continue ifadesiyle karşılaştığında, altındaki işlemleri atlar
# ve doğrudan döngünün bir sonraki adımına (başına) geçer.

print("\n--- 4.2 continue Örnekleri ---")

# for ile continue kullanımı (Belirli elemanları pas geçme)
liste = [1, 2, 3, 4, 5, 6]
for sayı in liste:
    if sayı == 3 or sayı == 5:
        continue  # 3 ve 5 basılmayacak, pas geçilecek
    print("Sayı:", sayı)

# While Döngüsünde continue Kullanırken DİKKAT!
# While döngüsünde continue kullanılmadan önce sayaç artırılmazsa SONSUZ DÖNGÜ oluşur.

print("\nWhile İçinde Doğru continue Kullanımı:")
i = 0
while i < 10:
    if i == 2:
        i += 1  # continue'dan ÖNCE artırma yapılmalıdır!
        continue
    print("i:", i)
    i += 1