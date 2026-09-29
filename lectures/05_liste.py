# ==============================================================================
# LİSTELER (LISTS)
# ==============================================================================
# Listeler sıralı verileri saklamak için kullanılır. Metinlerin (string) aksine
# DEĞİŞTİRİLEBİLİR (mutable) bir yapıya sahiptirler. Tek bir liste içinde
# farklı veri tipleri saklanabilir.
# ==============================================================================

# %% [1. Liste Oluşturma]
# ------------------------------------------------------------------------------
# Köşeli parantez [] kullanılarak liste tanımlanır.

liste = [3, 4, 5, 6, "Elma", 3.14, 5.324]
print("Çeşitli veri tipli liste:", liste)

# Boş liste oluşturma yöntemleri:
bos_liste1 = []
bos_liste2 = list()

# len() fonksiyonu listenin kaç elemandan oluştuğunu söyler.
liste3 = [3, 4, 5, 6, 6, 7, 8, 9, 0, 0, 0]
print("Liste3 eleman sayısı:", len(liste3))

# Metinleri (string) listeye dönüştürme:
s = "Merhaba"
lst = list(s)
print("Metnin listeye dönüştürülmüş hali:", lst)


# %% [2. Indeksleme ve Parçalama (Slicing)]
# ------------------------------------------------------------------------------
liste = [3, 4, 5, 6, 7, 8, 9, 10]

print("0. eleman:", liste[0])
print("4. eleman:", liste[4])
print("Sonuncu eleman (liste[-1]):", liste[-1])

# Parçalama (Slicing) [Başlangıç : Bitiş : Adım]
print("Baştan 4. indekse kadar (4 dahil değil):", liste[:4])
print("1. indeksten 5. indekse kadar:", liste[1:5])
print("5. indeksten sonuna kadar:", liste[5:])
print("2'şer atlayarak alma:", liste[::2])
print("Listeyi tersten yazdırma:", liste[::-1])


# %% [3. Temel Liste İşlemleri ve Değiştirilebilirlik]
# ------------------------------------------------------------------------------

# --- Liste Birleştirme ---
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]
print("İki listenin toplamı:", liste1 + liste2)

# --- Eleman Ekleme ve Güncelleme ---
liste = [1, 2, 3, 4]
liste = liste + ["Enes"]
print("Eleman eklenmiş liste:", liste)

liste[0] = 10  # Doğrudan eleman değiştirilebilir
print("0. elemanı güncellenmiş liste:", liste)

liste[:2] = [40, 50]  # Dilimleme ile toplu güncelleme
print("İlk iki elemanı güncellenmiş liste:", liste)

# --- Liste Çarpma ---
liste_carpim = [1, 2, 3, 4, 5]
print("3 ile çarpılmış geçici liste:", liste_carpim * 3)


# %% [4. Temel Liste Metodları]
# ------------------------------------------------------------------------------

# --- append() Metodu ---
# Listenin en sonuna yeni bir eleman ekler.
ornek_liste = [3, 4, 5, 6]
ornek_liste.append(7)
ornek_liste.append("Enes")
print("append sonrası liste:", ornek_liste)

# --- pop() Metodu ---
# Belirtilen indeksteki elemanı listeden çıkarır ve geriye döndürür.
# Indeks verilmezse varsayılan olarak son elemanı çıkarır.
liste_pop = [1, 2, 3, 4, 5]
cikarilan_son = liste_pop.pop()
print(f"Çıkarılan son eleman: {cikarilan_son}, Kalan liste: {liste_pop}")

cikarilan_indeksli = liste_pop.pop(2)
print(f"2. indeksten çıkarılan: {cikarilan_indeksli}, Kalan liste: {liste_pop}")

# "Enes" elemanı ekleyip geri çıkaralım:
liste_pop.append("Enes")
print("Enes eklendikten sonra liste:", liste_pop)
cikarilan_isim = liste_pop.pop()
print(f"pop() ile çıkarılan isim: {cikarilan_isim}")

# Olmayan indekse erişmeye çalışıldığında hata alınır:
try:
    print(liste_pop[50])
except:
    print("[HATA ÖRNEĞİ]")

# --- sort() Metodu ---
# Liste elemanlarını yerinde (in-place) sıralar.
sayi_listesi = [34, 1, 56, 334, 23, 2, 3, 19]
sayi_listesi.sort()
print("Küçükten büyüğe sıralı:", sayi_listesi)

sayi_listesi.sort(reverse=True)
print("Büyükten küçüğe sıralı:", sayi_listesi)

metin_listesi = ["Elma", "Armut", "Muz", "Kiraz"]
metin_listesi.sort()
print("Alfabetik sıralı:", metin_listesi)


# %% [5. İç İçe Listeler (Nested Lists)]
# ------------------------------------------------------------------------------
# Listeler matris veya ağaç yapıları oluşturmak için iç içe kullanılabilir.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

matris = [l1, l2, l3]
print("Matris yapısı:", matris)

# 2. satır, 1. sütun elemanına ulaşma (l2'nin ilk elemanı)
print("matris[1][0] Elemanı:", matris[1][0])