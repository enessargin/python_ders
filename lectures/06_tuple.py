# ==============================================================================
# DEMETLER (TUPLES)
# ==============================================================================
# Demetler (tuple), listelere oldukça benzer ancak en önemli farkları
# DEĞİŞTİRİLEMEZ (immutable) oluşlarıdır.
# Programlarımızda değerlerin kaza ile değiştirilmesini istemediğimiz
# durumlarda veri güvenliği için demetleri tercih ederiz.
# ==============================================================================

# %% [1. Demet Oluşturma]
# ------------------------------------------------------------------------------
# Demet elemanları parantez () içine alınarak tanımlanır.

demet = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Demet içeriği:", demet)

# type() fonksiyonu verinin tipini doğrulamamızı sağlar.
print("Demet türü:", type(demet))

# TEK ELEMANLI DEMET TANIMLAMA:
# Tek elemanlı bir demet oluştururken elemanın sonuna mutlaka virgül (,)
# koymalıyız. Aksi takdirde Python bunu normal bir tamsayı (int) olarak algılar.
tek_elemanli_demet = (1,)
print("Tek elemanlı demet:", tek_elemanli_demet)
print("Tek elemanlı demet türü:", type(tek_elemanli_demet))


# %% [2. Indeksleme ve Parçalama (Slicing)]
# ------------------------------------------------------------------------------
# Demetlerde indeksleme listelerle ve metinlerle birebir aynı çalışır.

demet = (1, 2, 3, 4, 5, 6, 7)

# 0. indeksteki elemana ulaşma
print("0. indeks:", demet[0])

# 4. indeksteki elemana ulaşma
print("4. indeks:", demet[4])

# Son indeksteki elemana negatif indeksleme ile ulaşma
print("Son eleman (demet[-1]):", demet[-1])

# 2. indeksten başlayıp sonuna kadar alma (Slicing)
print("2. indeksten sonuna kadar:", demet[2:])


# %% [3. Temel Demet Metodları]
# ------------------------------------------------------------------------------

# --- index() Metodu ---
# Verilen bir elemanın demetteki ilk indeks sırasını döndürür.
demet_metod = (1, 2, 3, "Enes", "Polito", "Merhaba")

print("'Enes' elemanının indeksi:", demet_metod.index("Enes"))
print("1 elemanının indeksi:", demet_metod.index(1))

# --- count() Metodu ---
# Verilen değerin demet içerisinde kaç defa geçtiğini sayar.
demet_sayi = (1, 23, 34, 34, 2, 1, 4, 5, 1, 1, 34)

print("Demet içindeki '1' sayısı:", demet_sayi.count(1))
print("Demet içindeki '34' sayısı:", demet_sayi.count(34))


# %% [4. Değiştirilmeme Özelliği (Immutability)]
# ------------------------------------------------------------------------------
# Demetlerin elemanları sonradan değiştirilemez veya doğrudan silinemez.

demet_sabit = ("Elma", "Armut", "Muz")

try:
    # Bu işlem hata verecektir:
    demet_sabit[0] = "Kiraz"
except:
    print("Hata Mesajı")

try:
    # Demetlerde remove() gibi eleman silme metodları bulunmaz:
    demet_sabit.remove("Elma")
except:
    print("Hata Mesajı")
