# ==============================================================================
# PROGRAMLAMA ÖDEVİ - DÖNGÜLER (SORULAR)
# ==============================================================================


# %% [PROBLEM 1]
"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 2]
"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan her birinin 4. kuvvetinin toplamı 
(3 basamaklı sayılar için 3. kuvveti) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek: 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 3]
"""
1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 4]
"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam" değişkenini bastırın.

İpucu: while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 5]
"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. 
Bu işlemi 'continue' ile yapmaya çalışın.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 6]
"""
List comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmaya çalışın.
"""

# Kodlarınızı buraya yazınız:


# ==============================================================================
# PROGRAMLAMA ÖDEVİ - DÖNGÜLER (ÇÖZÜMLER)
# ==============================================================================

# %% [PROBLEM 1 ÇÖZÜMÜ]
sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı, "mükemmel bir sayıdır.")
else:
    print(sayı, "mükemmel bir sayı değildir.")


# %% [PROBLEM 2 ÇÖZÜMÜ]
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayı değildir.")


# %% [PROBLEM 3 ÇÖZÜMÜ]
for i in range(1, 11):
    print("*************************************************")
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, i * j))


# %% [PROBLEM 4 ÇÖZÜMÜ]
toplam = 0

while True:
    sayı = input("Sayı:")
    
    if (sayı == "q"):
        break
    sayı = int(sayı)
    toplam += sayı
    
print("Girdiğiniz Sayıların Toplamı:", toplam)


# %% [PROBLEM 5 ÇÖZÜMÜ]
for i in range(1, 101):
    if (i % 3 != 0):
        continue
    print(i)


# %% [PROBLEM 6 ÇÖZÜMÜ]
liste = [x for x in range(1, 101) if x % 2 == 0]
print(liste)
