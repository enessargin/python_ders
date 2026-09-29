# ==============================================================================
# PROGRAMLAMA ÖDEVİ - FONKSİYONLAR (SORULAR)
# ==============================================================================

# %% [PROBLEM 1]
"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. 
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 2]
"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) 
dönen bir tane fonksiyon yazın.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 3]
"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) 
dönen bir tane fonksiyon yazın.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 4]
"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 5]
"""
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran 
bir fonksiyon yazın. (a <= 100, b <= 100)
"""

# Kodlarınızı buraya yazınız:

## 2. Çözümler Dosyası (`fonksiyonlar_odev_cozumleri.py`)

# ==============================================================================
# PROGRAMLAMA ÖDEVİ - FONKSİYONLAR (ÇÖZÜMLER)
# ==============================================================================

# %% [PROBLEM 1 ÇÖZÜMÜ]
def mukemmel(sayı):
    toplam = 0
    for i in range(1, sayı):
        if (sayı % i == 0):
            toplam += i
    return toplam == sayı


for i in range(1, 1001):
    if (mukemmel(i)):
        print("Mükemmel Sayı:", i)


# %% [PROBLEM 2 ÇÖZÜMÜ]
def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):
        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))


# %% [PROBLEM 3 ÇÖZÜMÜ]
def ekok_bulma(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i
            sayı1 //= i
            sayı2 //= i
        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i
            sayı1 //= i
        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i
            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:", ekok_bulma(sayı1, sayı2))


# %% [PROBLEM 4 ÇÖZÜMÜ]
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))
print(okunus(sayı))


# %% [PROBLEM 5 ÇÖZÜMÜ]
def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):
            c = (i ** 2 + j ** 2) ** 0.5
            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))
    return pisagor_listesi


for i in pisagor_bulma():
    print(i)
