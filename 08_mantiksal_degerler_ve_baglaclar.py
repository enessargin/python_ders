# ==============================================================================
# MANTIKSAL DEĞERLER (BOOLEAN), KARŞILAŞTIRMA OPERATÖRLERİ VE MANTIKSAL BAĞLAÇLAR
# ==============================================================================

# %% [1. Mantıksal Değerler (Boolean)]
# ------------------------------------------------------------------------------
# Boolean veri tipi sadece iki değer alır: True (Doğru) veya False (Yanlış).

a = True
print("a değişkeninin tipi:", type(a))

b = False
print("b değişkeninin tipi:", type(b))

# --- bool() Fonksiyonu ve Sayıların Mantıksal Karşılığı ---
# Python'da 0 sayısı False, 0 dışındaki tüm sayılar True kabul edilir.
print("bool(12.4):", bool(12.4))
print("bool(0.0):", bool(0.0))
print("bool(-1):", bool(-1))

# --- None Değeri ---
# Değeri henüz belirlenmemiş değişkenler geçici olarak None yapılabilir.
deger = None
print("Henüz atanmamış değer:", deger)
deger = 4
print("Atandıktan sonraki değer:", deger)


# %% [2. Karşılaştırma Operatörleri]
# ------------------------------------------------------------------------------
# ==  : Eşit mi?
# !=  : Eşit değil mi?
# >   : Büyük mü?
# <   : Küçük mü?
# >=  : Büyük veya eşit mi?
# <=  : Küçük veya eşit mi?

print("\n--- Karşılaştırma Örnekleri ---")
print("'Enes' == 'Enes':", "Enes" == "Enes")
print("'Enes' == 'Polito':", "Enes" == "Polito")
print("'Enes' != 'Polito':", "Enes" != "Polito")
print("'Oğuz' < 'Enes':", "Oğuz" < "Enes")  # Alfabetik sıralamaya göre bakar

print("2 < 3:", 2 < 3)
print("54 >= 54:", 54 >= 54)
print("34 <= 45:", 34 <= 45)


# %% [3. Mantıksal Bağlaçlar (and, or, not)]
# ------------------------------------------------------------------------------

# --- and (VE) Operatörü ---
# Bağlanan TÜM koşulların True olmasını ister. Biri bile False ise sonuç False olur.
print("\n--- and Operatörü ---")
print("1 < 2 and 'Enes' == 'Enes':", 1 < 2 and "Enes" == "Enes")
print("2 > 3 and 'Enes' == 'Enes':", 2 > 3 and "Enes" == "Enes")
print("2 == 2 and 3.14 < 2.54:", 2 == 2 and 3.14 < 2.54)

# --- or (VEYA) Operatörü ---
# Bağlanan koşullardan EN AZ BİRİNİN True olması yeterlidir.
print("\n--- or Operatörü ---")
print("1 < 2 or 'Enes' != 'Enes':", 1 < 2 or "Enes" != "Enes")
print("2 > 3 or 'Enes' != 'Enes':", 2 > 3 or "Enes" != "Enes")
print("2 > 3 or 'Enes' != 'Enes' or 3.14 < 4.32:", 2 > 3 or "Enes" != "Enes" or 3.14 < 4.32)

# --- not (DEĞİL) Operatörü ---
# Mantıksal değeri tersine çevirir (True -> False, False -> True).
print("\n--- not Operatörü ---")
print("not (2 == 2):", not 2 == 2)
print("not ('Python' == 'Php'):", not "Python" == "Php")

# --- Operatörleri Karmaşık Kullanma (Parantez Kullanımı) ---
print("\n--- Karmaşık Bağlaç Kullanımı ---")
sonuc1 = not (2.14 > 3.49 or (2 != 2 and "Enes" == "Enes"))
print("İşlem Sonucu 1:", sonuc1)

sonuc2 = "Araba" < "Zula" and ("Bebek" < "Çocuk" or (not 14))
print("İşlem Sonucu 2:", sonuc2)