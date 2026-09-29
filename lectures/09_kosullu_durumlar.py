# ==============================================================================
# KOŞULLU DURUMLAR (if - elif - else)
# ==============================================================================

# %% [1. Python Blok Yapısı ve Girintiler (Indentation)]
# ------------------------------------------------------------------------------
# Python'da kod blokları süslü parantez {} yerine GIRINTILER (Tab / 4 Boşluk) 
# ile belirlenir.

a = 2  # Blok 1

if a == 2:
    print("a değişkeninin değeri 2'dir.")  # Blok 2 (Girintili)
print("Bu satır girintisizdir ve her durumda çalışır.\n")  # Blok 1


# %% [2. if - else Kalıbı]
# ------------------------------------------------------------------------------
# if : Koşul True ise çalışır.
# else: Yukarıdaki if koşulu False olduğunda çalışır.

print("--- 18 Yaş Kontrol Örneği ---")
yas = int(input("Lütfen yaşınızı giriniz: "))

if yas < 18:
    print("Bu mekana giremezsiniz.")
else:
    print("Mekana hoş geldiniz.")


# %% [3. if - elif - else Kalıbı]
# ------------------------------------------------------------------------------
# Birden fazla koşul kontrol edilecekse 'elif' kullanılır.
# Şartlardan hangisi ilk olarak True sağlarsa o blok çalışır ve yapı sonlanır.

print("\n--- Menü/İşlem Seçimi Örneği ---")
islem = int(input("Lütfen bir işlem seçiniz (1, 2 veya 3): "))

if islem == 1:
    print("1. işlem seçildi.")
elif islem == 2:
    print("2. işlem seçildi.")
elif islem == 3:
    print("3. işlem seçildi.")
else:
    print("Geçersiz İşlem!")


# %% [4. Önemli Fark: 'if-elif-else' ve 'if-if-if' Blokları]
# ------------------------------------------------------------------------------
# - 'elif' kullandığınızda tek bir doğru koşul bulunduğunda kontrol biter.
# - 'if-if-if' yazarsanız Python TÜM if şartlarını tek tek baştan aşağı kontrol eder.

print("\n--- Harf Notu Hesaplama (Doğru Yöntem: elif) ---")
note = float(input("Lütfen ders notunuzu giriniz (0-100): "))

if note >= 90:
    print("Harf Notunuz: AA")
elif note >= 85:
    print("Harf Notunuz: BA")
elif note >= 80:
    print("Harf Notunuz: BB")
elif note >= 75:
    print("Harf Notunuz: CB")
elif note >= 70:
    print("Harf Notunuz: CC")
elif note >= 65:
    print("Harf Notunuz: DC")
elif note >= 60:
    print("Harf Notunuz: DD")
else:
    print("Dersten Kaldınız.")


# --- Hatalı Mantık Örneği (Sadece if kullanılması durumu) ---
# Not 95 girilirse, 90, 85, 80... şartlarının hepsi True olacağı için 
# ekrana bütün not harfleri basılır:
"""
if note >= 90:
    print("AA")
if note >= 85:
    print("BA")
if note >= 80:
    print("BB")
# ... bu kullanım hatalı sonuçlar doğurur.
"""