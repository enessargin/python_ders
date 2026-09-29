# ==============================================================================
# Python'da Sayılar ve Değişkenler
# ==============================================================================
# Bu bölümde temel sayı türlerini (Integer, Float), temel aritmetik işlemleri
# ve değişken tanımlama kurallarını inceliyoruz.

# ------------------------------------------------------------------------------
# 1. Temel Matematik Operatörleri
# ------------------------------------------------------------------------------

# Toplama işlemi
print("--- Toplama ve Çıkarma ---")
print("3 + 4 =", 3 + 4)  # 7
print("5 - 17 =", 5 - 17)  # -12 (Negatif tam sayılar)

# Çarpma işlemi
print("\n--- Çarpma ve Bölme ---")
print("13 * 4 =", 13 * 4)  # 52

# Bölme işlemi
# NOT: Python 3'te iki tam sayı bölündüğünde sonuç her zaman float (ondalıklı) döner.
print("4 / 2 =", 4 / 2)  # 2.0


# ------------------------------------------------------------------------------
# 2. Değişkenler ve Atama (Assignment)
# ------------------------------------------------------------------------------
# Değişkenler, verileri hafızada tutan isimli kapsüllerdir.
print("\n--- Değişkenler ---")

i = 10  # 'i' adında bir değişken oluşturduk ve 10 değerini atadık.
print("i'nin değeri:", i)
print("i * i * i =", i * i * i)  # Değişkeni matematiksel işlemlerde kullanabiliriz.

# Değişkenin değerini güncelleme ('=' operatörü ile)
i = 15
print("i'nin yeni değeri:", i)

# Birden fazla değişken ile işlem yapma
a = 4
b = 3
c = a + 2 * b  # Önce sağ taraftaki işlem hesaplanır, sonra 'c'ye atanır.
print("c'nin değeri (a + 2*b):", c)  # 10


# ------------------------------------------------------------------------------
# 3. Değişken İsimlendirme Kuralları
# ------------------------------------------------------------------------------
# 1. Değişken isimleri sayı ile başlayamaz.
# 2. Kelimeler arasında boşluk olamaz.
# 3. Özel semboller (?, !, @, # vb.) kullanılamaz (Sadece '_' kullanılabilir).
# 4. Python'a özel anahtar kelimeler (while, for, not vb.) kullanılamaz.

# Geçerli değişken ismi:
_i = 5

# Hatalı kullanım örneği:
# i? = 5  # SyntaxError verir.


# ------------------------------------------------------------------------------
# 4. Değişkenlerle Pratik İpuçları
# ------------------------------------------------------------------------------
print("\n--- Pratik Yöntemler ---")

# Pratik 1: İki değişkenin değerini takas etme (Swapping)
x = 4
y = 3
print(f"Değişimden önce: x={x}, y={y}")

x, y = y, x  # Değerler tek satırda yer değiştirir.
print(f"Değişimden sonra: x={x}, y={y}")

# Pratik 2: Değer artırma ve azaltma kısayolları
sayi = 10
sayi += 1  # 'sayi = sayi + 1' ile aynı anlamdadır.
print("10 + 1 (+= 1):", sayi)  # 11

sayi -= 3  # 'sayi = sayi - 3' ile aynı anlamdadır.
print("11 - 3 (-= 3):", sayi)  # 8

sayi *= 2  # 'sayi = sayi * 2' ile aynı anlamdadır.
print("8 * 2 (*= 2):", sayi)  # 16


# ------------------------------------------------------------------------------
# 5. Yorum Satırları
# ------------------------------------------------------------------------------
# Tek satırlık yorumlar '#' simgesiyle yapılır.

"""
Bu bir çok satırlı yorum/açıklama bloğudur.
Python çalışırken bu alanları göz ardı eder.
"""