# ==============================================================================
# PROGRAMLAMA ÖDEVİ - HATALAR VE İSTİSNALAR (SORULAR)
# ==============================================================================

# %% [PROBLEM 1]
"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345", "sadas", "324a", "14", "kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. 
Bunu yaparken try, except bloklarını kullanmayı unutmayın.
"""

# Kodlarınızı buraya yazınız:


# %% [PROBLEM 2]
"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
Bu fonksiyon, eğer sayı çift ise 'return' ile bu değeri dönsün. 
Ancak sayı tek sayı ise fonksiyon 'raise' ile 'ValueError' hatası fırlatsın. 

Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın 
ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""

# Kodlarınızı buraya yazınız:

# %% [PROBLEM 1 ÇÖZÜMÜ]
liste = ["345", "sadas", "324a", "14", "kemal"]

for eleman in liste:
    try:
        # Eğer dönüştürme başarısız olursa exception bloğuna geçer ve print çalışmaz
        eleman = int(eleman)
        print(eleman)
    except:
        # pass deyimi hiçbir işlem yapmadan devam edilmesini sağlar
        pass


# %% [PROBLEM 2 ÇÖZÜMÜ]
def çift_mi(sayı):
    if sayı % 2 == 0:
        return sayı
    else:
        raise ValueError


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass
