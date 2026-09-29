# ==============================================================================
# Matematik Operatörleri ve İşlem Sırası
# ==============================================================================
# Bu bölümde Python'da bulunan tüm temel ve gelişmiş aritmetik operatörleri
# inceliyoruz.

# 1. Toplama (+) ve Çıkarma (-)
print("--- Toplama & Çıkarma ---")
print("14 + 15 =", 14 + 15)  # Tam sayılar
print("3.1 + 4.8 =", 3.1 + 4.8)  # Ondalıklı sayılar
print("28 - 35 - 40 =", 28 - 35 - 40)

# 2. Çarpma (*)
print("\n--- Çarpma ---")
print("4 * 5 =", 4 * 5)
print("3.14 * 4.5 =", 3.14 * 4.5)

# 3. Bölme (/) vs Tam Sayı Bölmesi (//)
print("\n--- Bölme Operatörleri ---")
# Ondalıklı Bölme (/): Sonucu her zaman float döndürür.
print("4 / 2 =", 4 / 2)  # 2.0
print("10 / 3 =", 10 / 3)  # 3.3333...

# Tam Sayı Bölmesi (//): Bölümün sadece tam sayı kısmını alır (yuvarlama yapmaz, tabanını alır).
print("13 // 4 =", 13 // 4)  # 13'ün içinde 4, 3 defa var -> 3
print("22 // 7 =", 22 // 7)  # 3

# 4. Mod Alma (%) - Kalanı Bulma
print("\n--- Kalanı Bulma (Mod) ---")
print("13 % 4 =", 13 % 4)  # 13'ün 4'e bölümünden kalan -> 1
print("14 % 2 =", 14 % 2)  # Çift sayı kontrolünde sıkça kullanılır -> 0

# 5. Üs Alma (**)
print("\n--- Üs Alma ve Karekök ---")
print("4 ** 3 =", 4 ** 3)  # 4 * 4 * 4 = 64
print("2 ** 4 =", 2 ** 4)  # 16

# İpucu: Bir sayının 0.5'inci (1/2) üssünü almak o sayının karekökünü verir!
print("64 ** 0.5 (Karekök 64) =", 64 ** 0.5)  # 8.0

# 6. İşaret Değiştirme (-)
print("\n--- İşaret Değiştirme ---")
a = 4
print("a:", a, "-> -a:", -a)  # -4
b = -13
print("b:", b, "-> -b:", -b)  # 13


# ------------------------------------------------------------------------------
# İşlem Sırası (Precedence)
# ------------------------------------------------------------------------------
# Matematiksel kurallar geçerlidir:
# 1. Parantez içi
# 2. Üs alma
# 3. Çarpma ve Bölme
# 4. Toplama ve Çıkarma
# 5. Eşit önceliklilerde soldan sağa işlem yapılır.

print("\n--- İşlem Sırası Örneği ---")
islem1 = 8 + 4 * 3 / 2 - 18  # Önce (4*3)=12, sonra (12/2)=6.0, sonra 8+6.0-18 = -4.0
print("8 + 4 * 3 / 2 - 18 =", islem1)

# Okunabilirliği artırmak için karmaşık işlemlerde parantez kullanmak tavsiye edilir:
islem2 = 8 + ((4 * 3) / 2) - 18
print("Parantezli Hali:", islem2)