# ==============================================================================
# PROGRAMLAMA ÖDEVİ - KOŞULLU DURUMLAR (SORULAR)
# ==============================================================================

# %% [Problem 1: Beden Kitle İndeksi (BKİ)]
# ------------------------------------------------------------------------------
# Kullanıcıdan alınan boy (m) ve kilo (kg) değerlerine göre beden kitle
# indeksini hesaplayın ve aşağıdaki kurallara göre kategorisini ekrana yazdırın:
#
# Formül: BKİ = Kilo / (Boy * Boy)
#
# - BKİ 18.5'un altındaysa -------> Zayıf
# - BKİ 18.5 ile 25 arasındaysa ------> Normal
# - BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
# - BKİ 30'un üstündeyse -------------> Obez

print("=" * 45)
print("     PROBLEM 1: BEDEN KİTLE İNDEKSİ HESAPLAMA     ")
print("=" * 45)

# Kodunuzu buraya yazınız



# %% [Problem 2: En Büyük Sayıyı Bulma]
# ------------------------------------------------------------------------------
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

print("\n" + "=" * 45)
print("        PROBLEM 2: EN BÜYÜK SAYIYI BULMA        ")
print("=" * 45)

# Kodunuzu buraya yazınız



# %% [Problem 3: Harf Notu Hesaplama]
# ------------------------------------------------------------------------------
# Kullanıcının girdiği vize1, vize2 ve final notlarına göre harf notunu hesaplayın.
#
# Not Ağırlıkları:
# - Vize1 : %30
# - Vize2 : %30
# - Final : %40
#
# Harf Notu Skalası:
# Toplam Not >= 90 -----> AA
# Toplam Not >= 85 -----> BA
# Toplam Not >= 80 -----> BB
# Toplam Not >= 75 -----> CB
# Toplam Not >= 70 -----> CC
# Toplam Not >= 65 -----> DC
# Toplam Not >= 60 -----> DD
# Toplam Not >= 55 -----> FD
# Toplam Not <  55 -----> FF

print("\n" + "=" * 50)
print("        PROBLEM 3: HARF NOTU HESAPLAMA SİSTEMİ        ")
print("=" * 50)

# Kodunuzu buraya yazınız



# %% [Problem 4: Geometrik Şekil Tespiti]
# ------------------------------------------------------------------------------
# Kullanıcıya üçgenin mi yoksa dörtgenin mi tipini bulmak istediğini sorun.
#
# 1. Eğer kullanıcı "Dörtgen" cevabını verirse:
#    - 4 tane kenar uzunluğu isteyin.
#    - Kare mi, Dikdörtgen mi yoksa sıradan bir Dörtgen mi olduğunu bulun.
#
# 2. Eğer kullanıcı "Üçgen" cevabını verirse:
#    - 3 tane kenar uzunluğu isteyin.
#    - Öncelikle kenarların bir üçgen oluşturup oluşturmadığını (Üçgen Eşitsizliği) kontrol edin.
#      * Üçgen Eşitsizliği: Bir kenar uzunluğu, diğer iki kenarın farkının mutlak değerinden
#        büyük ve toplamından küçük olmalıdır. (|a-b| < c < a+b)
#      * Mutlak değer için Pythondaki `abs()` fonksiyonunu kullanabilirsiniz.
#    - Eğer geçerli bir üçgense; Eşkenar, İkizkenar veya Çeşitkenar olduğunu bulun.
#    - Geçerli değilse "Üçgen belirtmiyor" yazdırın.

print("\n" + "=" * 50)
print("           PROBLEM 4: GEOMETRİK ŞEKİL HESAPLAYICI          ")
print("=" * 50)

# Kodunuzu buraya yazınız