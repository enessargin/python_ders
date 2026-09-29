# ==============================================================================
# print() Fonksiyonu, Özel Karakterler ve Formatlama
# ==============================================================================
# Bu bölümde ekrana veri basma tekniklerini, kaçış dizilerini ve
# string formatlama yöntemlerini öğreniyoruz.

# ------------------------------------------------------------------------------
# 1. Temel print() Kullanımı
# ------------------------------------------------------------------------------
print("--- Temel print() ---")
print(35)  # Sayıları doğrudan basabiliriz.
print("Enes", "Sargın", "Selam")  # Virgül ile ayırarak yan yana yazdırabiliriz.


# ------------------------------------------------------------------------------
# 2. Kaçış Karakterleri (Escape Characters)
# ------------------------------------------------------------------------------
print("\n--- Kaçış Karakterleri ---")

# \n : Alt satıra geçer (New Line)
print("Merhaba\nNasılsın\nİyi misin")

# \t : Bir TAB kadar (genellikle 4-8 karakter) boşluk bırakır
print("Ocak\tMart\tŞubat")


# ------------------------------------------------------------------------------
# 3. type() Fonksiyonu
# ------------------------------------------------------------------------------
# Bir değişkenin/değerin veri tipini öğrenmek için kullanılır.
print("\n--- Veri Tipleri (type) ---")
print("65'in tipi      :", type(65))  # <class 'int'>
print("5.87'nin tipi   :", type(5.87))  # <class 'float'>
print("'Enes'in tipi   :", type("Enes"))  # <class 'str'>


# ------------------------------------------------------------------------------
# 4. print() Parametreleri: 'sep' ve '*' (Unpacking)
# ------------------------------------------------------------------------------
print("\n--- print() Özellikleri ---")

# 'sep' Parametresi: Yazdırılan elemanların arasına konulacak karakteri belirler.
# Varsayılan değeri boşluktur (" ").
print(3, 4, 5, 6, 7, sep=".")  # 3.4.5.6.7
print("06", "04", "2015", sep="/")  # 06/04/2015
print("Enes", "Sargın", "Selam", sep="\n")  # Her kelimeyi ayrı satıra yazar

# Yıldızlı (*) Parametreler: String'i karakterlerine ayırarak print'e sunar.
print(*"Python")  # 'P y t h o n'
print(*"TBMM", sep=".")  # 'T.B.M.M'


# ------------------------------------------------------------------------------
# 5. String Formatlama (.format())
# ------------------------------------------------------------------------------
# Metin içerisine değişken yerleştirmek için kullanılır.
print("\n--- Formatlama ---")

# Yöntem 1: Sırasıyla süslü parantezlere ({}) yerleştirme
a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dır".format(a, b, a + b))

# Yöntem 2: İndeks numarası vererek sırayı değiştirme
# {0}=43, {1}="Enes", {2}=54
metin = "{1} {0} {2}".format(43, "Enes", 54)
print(metin)  # "Enes 43 54"

# Yöntem 3: Ondalıklı sayı basamak hassasiyeti ayarlama ({:.Nf})
# .2f -> Virgülden sonra 2 basamak al demektir (yuvarlama yapar).
pi = 3.1463
sayi2 = 5.324
sayi3 = 7.324324
print("{:.2f} {:.2f} {:.3f}".format(pi, sayi2, sayi3))  # 3.15 5.32 7.324

# NOT (f-string): Python 3.6+ ile gelen formatlama yöntemi:
print(f"Modern Kullanım (f-string): {a} + {b} = {a + b}")