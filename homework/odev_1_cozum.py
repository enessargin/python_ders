# ==============================================================================
# PROGRAMLAMA ÖDEVİ ÇÖZÜMLERİ
# ==============================================================================

# %% [Soru 1 Çözümü: 3 Sayının Çarpımı ve Formatlama]
# ------------------------------------------------------------------------------
# input() fonksiyonu kullanıcıdan veriyi her zaman metin (string) olarak alır.
# Matematiksel işlem yapabilmek için int() ile tamsayıya çeviriyoruz.

print("--- Soru 1: 3 Sayının Çarpımı ---")
a = int(input("Lütfen 1. sayıyı giriniz (a): "))
b = int(input("Lütfen 2. sayıyı giriniz (b): "))
c = int(input("Lütfen 3. sayıyı giriniz (c): "))

carpim = a * b * c

# .format() kullanarak süslü parantezlerin {} yerine sırasıyla değişkenleri koyuyoruz.
print("{} x {} x {} = {} dir\n".format(a, b, c, carpim))


# %% [Soru 2 Çözümü: Beden Kitle İndeksi (BKİ)]
# ------------------------------------------------------------------------------
# Boy ondalıklı bir sayı olabileceği için float(), kilo ise int() olarak alınır.
# Üs alma işlemi için Python'da ** operatörü kullanılır.

print("--- Soru 2: Beden Kitle İndeksi ---")
boy = float(input("Boyunuzu giriniz (Örn: 1.75): "))
kilo = int(input("Kilonuzu giriniz (Örn: 70): "))

bki = kilo / (boy ** 2)

print("Beden Kitle İndeksiniz: {}\n".format(bki))


# %% [Soru 3 Çözümü: Yakıt Tutarı Hesaplama]
# ------------------------------------------------------------------------------
print("--- Soru 3: Yakıt Tutarı Hesaplama ---")
yakan_miktar = float(input("Kilometrede harcanan tutar (TL): "))
kilometre = int(input("Kaç km yol yaptınız?: "))

toplam_tutar = yakan_miktar * kilometre

print("Toplam Ödemeniz Gereken Tutar: {} TL\n".format(toplam_tutar))


# %% [Soru 4 Çözümü: Kullanıcı Bilgilerini Alt Alta Yazdırma]
# ------------------------------------------------------------------------------
# Metinlerde alt satıra geçmek için escape karakteri olan '\n' kullanılır.

print("--- Soru 4: Bilgi Formu ---")
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
numara = input("Numaranız: ")

print("\nKullanıcı Bilgileri İşleniyor...\n")
# \n karakteri sayesinde tek bir print fonksiyonunda alt alta yazdırıyoruz:
print("{}\n{}\n{}\n".format(ad, soyad, numara))


# %% [Soru 5 Çözümü: İki Değişkenin Değerini Değiştirme (Swapping)]
# ------------------------------------------------------------------------------
# Python'a özgü pratik yöntem: a, b = b, a ifadesiyle geçici bir üçüncü değişkene 
# ihtiyaç duymadan iki değişkenin değerini takas edebiliriz.

print("--- Soru 5: Değer Değiştirme (Takas) ---")
a = input("a değerini giriniz: ")
b = input("b değerini giriniz: ")

print("Değiştirilmeden Önceki Değerler -> a: {} | b: {}".format(a, b))

# Takas İşlemi
a, b = b, a

print("Değiştirildikten Sonraki Değerler -> a: {} | b: {}\n".format(a, b))


# %% [Soru 6 Çözümü: Hipotenüs Hesaplama]
# ------------------------------------------------------------------------------
# Bir sayının 0.5'inci kuvvetini almak (** 0.5), o sayının karekökünü almak demektir.

print("--- Soru 6: Dik Üçgende Hipotenüs Bulma ---")
a = int(input("1. Dik Kenar (a): "))
b = int(input("2. Dik Kenar (b): "))

# c^2 = a^2 + b^2  =>  c = (a^2 + b^2)^0.5
hipotenus = (a ** 2 + b ** 2) ** 0.5

print("Hesaplanan Hipotenüs Uzunluğu (c): {}\n".format(hipotenus))