# ==============================================================================
# Karakter Dizileri (Stringler)
# ==============================================================================
# Stringler metinsel verileri temsil eder. Her metin, karakterlerden
# oluşan sıralı bir dizidir.

# ------------------------------------------------------------------------------
# 1. String Oluşturma Yöntemleri
# ------------------------------------------------------------------------------
# Tek tırnak ('), çift tırnak (") veya üçlü tırnak (""") kullanılabilir.
str1 = 'Enes Sargın Selam'
str2 = "Enes Sargın Selam"
str3 = """Enes Sargın Selam"""

# DİKKAT: Hangi tırnakla başladıysak onunla bitirmeliyiz!
# Hatalı: "Merhaba' -> SyntaxError verir.

# Kesme işareti içeren metinlerde dış tırnağı çift tırnak seçmek kolaylık sağlar:
cumle = "Enes'in bugün dersi var"
print(cumle)


# ------------------------------------------------------------------------------
# 2. String İndeksleme (Indexing)
# ------------------------------------------------------------------------------
# Python'da indeksler 0'dan başlar.
# Pozitif İndeksler :  0   1   2   3
# Metin            :  e   n   e   s
# Negatif İndeksler: -4  -3  -2  -1

metin = "enes"
print("\n--- İndeksleme ---")
print("İlk karakter (metin[0]):", metin[0])  # 'e'
print("İkinci karakter (metin[1]):", metin[1])  # 'n'

# Negatif indeksler sondan geriye doğru sayar:
print("Son karakter (metin[-1]):", metin[-1])  # 's'
print("Sondan ikinci (metin[-2]):", metin[-2])  # 'e'


# ------------------------------------------------------------------------------
# 3. String Parçalama (Slicing)
# ------------------------------------------------------------------------------
# Formül: [başlangıç : bitiş : atlama_değeri]
# NOT: Bitiş indeksi dahil DEĞİLDİR!

dil = "Python Programlama Dili"
print("\n--- Parçalama (Slicing) ---")
print("a[4:10]   ->", dil[4:10])  # 4'ten başla, 10'a kadar (10 haric) -> 'on Pro'
print("a[:10]    ->", dil[:10])  # Baştan başla, 10'a kadar -> 'Python Pro'
print("a[4:]     ->", dil[4:])  # 4'ten başla, sona kadar -> 'on Programlama Dili'
print("a[:]      ->", dil[:])  # Tüm metni kopyalar
print("a[:-1]    ->", dil[:-1])  # Son karakter hariç tümü
print("a[::2]    ->", dil[::2])  # 2'şer atlayarak al -> 'Pto rgalm ii'
print("a[::-1]   ->", dil[::-1])  # String'i TERS ÇEVİRİR -> 'iliD amalmargorP nohtyP'


# ------------------------------------------------------------------------------
# 4. String Özellikleri ve Değiştirilemezlik (Immutability)
# ------------------------------------------------------------------------------
print("\n--- String Özellikleri ---")

# 1. Uzunluk bulma: len() fonksiyonu
print("Metin Uzunluğu:", len(dil))  # 23

# 2. Immutable (Değiştirilemez) Yapı
# Python'da string'in tek bir karakteri doğrudan değiştirilemez.
isim = "Enes"
try:
    isim[0] = 'T'  # TypeError hatası fırlatır
except TypeError as e:
    print("Hata Aldık! String elemanları doğrudan değiştirilemez:", e)

# 3. Stringlerde Toplama (Birleştirme) ve Çarpma
s1 = "Python "
s2 = "Programlama "
s3 = "Dili"
print("Birleştirme (+):", s1 + s2 + s3)

# Metni bir sayı ile çarparak tekrarlama:
print("Çarpma (*):", "Python" * 3)  # 'PythonPythonPython'