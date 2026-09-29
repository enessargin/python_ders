
# %% Fonksiyon Nedir?
"""
Fonksiyonlar programlamada belli işlevleri olan ve tekrar tekrar kullandığımız yapılardır.
Kod tekrarını engeller ve programın daha derli toplu durmasını sağlar.

- Gömülü Fonksiyonlar (Built-in): print(), type() vb.
- Kullanıcı Tanımlı Fonksiyonlar (User-defined): Bizim tanımladığımız fonksiyonlar.

Tanımlama Yapısı:
    def fonksiyon_adı(parametre1, parametre2...):
        # Fonksiyon bloğu
        Yapılacak işlemler
        # Dönüş değeri (Opsiyonel)
"""

# %% Fonksiyon Tanımlama ve Çağırma (Function Call)
def selamla():
    print("Selam arkadaşlar...")
    print("Nasılsınız?")

# Fonksiyonun tipini kontrol etme
print(type(selamla))

# Fonksiyon çağrısı
selamla()

# İstediğimiz kadar tekrar çağırabiliriz
selamla()
selamla()


# %%  Parametreler ve Argümanlar
# Fonksiyon tanımlarken belirtilen değişkenler: Parametre
def selamla_isim(isim):
    print("Merhaba:", isim)

# Fonksiyon çağrılırken gönderilen değerler: Argüman
selamla_isim("Kemal")
selamla_isim("Ayşe")


# 3 Parametreli toplama fonksiyonu
def toplama(a, b, c):
    print("Toplamları:", a + b + c)

toplama(3, 4, 5)
toplama(10, 11, 29)


# %% Örnek Uygulama: Faktöriyel Hesabı
def faktoriyel(sayı):
    faktoriyel_degeri = 1
    if sayı == 0 or sayı == 1:
        print("Faktoriyel", faktoriyel_degeri)
    else:
        while sayı >= 1:
            faktoriyel_degeri *= sayı
            sayı -= 1
        print("Faktoriyel", faktoriyel_degeri)

faktoriyel(5)  # 120
faktoriyel(6)  # 720
faktoriyel(1)  # 1
faktoriyel(0)  # 1



# %% Return Neden Gereklidir?
"""
'return' ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesini sağlar.
Böylelikle elde edilen değer bir değişkende saklanabilir veya başka fonksiyonlarda kullanılabilir.

Eğer return kullanılmazsa fonksiyon 'None' (NoneType) değer üretir.
"""

# Return kullanmayan fonksiyon örneği:
def toplama_yazdir(a, b, c):
    print("Toplamları", a + b + c)

def ikiyle_carp_yazdir(a):
    print("2 ile çarpılmış hali", a * 2)

toplam = toplama_yazdir(3, 4, 5)
print("Değişken Tipi:", type(toplam))  # NoneType döner
# ikiyle_carp_yazdir(toplam)  # TypeError hatası verir!


# %%  Return Kullanımı
def toplama(a, b, c):
    return a + b + c

def ikiyle_carp(a):
    return a * 2

toplam = toplama(3, 4, 5)
print("Sonuç:", ikiyle_carp(toplam))  # 24


# %%  İç İçe Fonksiyon Çağrıları
def üçle_carp(a):
    print("1. fonksiyon çalıştı")
    return a * 3

def ikiyle_topla(a):
    print("2. fonksiyon çalıştı")
    return a + 2

def dörde_böl(a):
    print("3. fonksiyon çalıştı")
    return a / 4

print("Zincirleme İşlem Sonucu:", dörde_böl(ikiyle_topla(üçle_carp(5))))


# %%  Return Sonrası Kodların Durumu
def toplama_test(a, b, c):
    print("Toplama fonksiyonu çalıştı.")
    return a + b + c
    print("Bu satır asla çalışmayacak!")  # Return çalıştığı anda fonksiyon sonlanır.

print(toplama_test(1, 2, 3))

# %%  Varsayılan (Default) Parametre Değerleri
def selamla(isim="İsimsiz"):
    print("Selam", isim)

selamla()          # Parametre verilmezse varsayılan değer kullanılır -> "Selam İsimsiz"
selamla("Serhat")   # Parametre verilirse bizim değerimiz geçerli olur -> "Selam Serhat"


# Birden fazla varsayılan parametre kullanımı
def bilgilerigoster(ad="Bilgi Yok", soyad="Bilgi Yok", numara="Bilgi Yok"):
    print("Ad:", ad, "Soyad:", soyad, "Numara:", numara)

bilgilerigoster()
bilgilerigoster("Enes ", "Sargın")

# Özel parametre ataması (Keyword Arguments)
bilgilerigoster(numara="123456")
bilgilerigoster(ad="Enes", numara="123456")


# %%  Esnek Sayıda Argüman Alma (*args / Yıldızlı Parametre)
"""
Fonksiyona kaç tane argüman gönderileceği önceden belli değilse '*' kullanılır.
Gelen argümanlar fonksiyon içinde bir 'Tuple' (demet) olarak ele alınır.
"""

def toplama(*parametreler):
    toplam = 0
    print("Gelen parametreler:", parametreler)
    for i in parametreler:
        toplam += i
    return toplam

print("Toplam:", toplama(3, 4, 5, 6, 7, 8, 9, 10))
print("Toplam:", toplama(1, 2, 3))
print("Toplam:", toplama())

# %% Yerel (Local) Değişkenler
"""
Fonksiyon bloğu içinde tanımlanan değişkenlerdir.
Fonksiyonun çalışması bittiğinde bellekten silinirler ve dışarıdan erişilemezler.
"""

def fonksiyon_yerel():
    a = 10  # Yerel değişken
    print("Fonksiyon içi a:", a)

fonksiyon_yerel()
# print(a)  # NameError hatası verir! 'a' fonksiyon dışında tanımlı değildir.


# %% Global Değişkenler
"""
Programın en dış seviyesinde tanımlanan değişkenlerdir.
Fonksiyonlar dahil kodun her yerinden erişilebilirler.
"""

b = 5  # Global değişken

def fonksiyon_global():
    print("Global b değişkeni:", b)

fonksiyon_global()


# Global ve Yerel İsim Çakışması
c = 10  # Global c

def fonksiyon_cakisma():
    c = 2  # Yerel c (Global olanı gizler/maskeler)
    print("Fonksiyon içi c:", c)

fonksiyon_cakisma()
print("Fonksiyon dışı c:", c)


# %%  'global' Deyimi
"""
Fonksiyon içinden global seviyedeki bir değişkeni değiştirmek istiyorsak 'global' anahtar kelimesi kullanılır.
"""

d = 10  # Global d

def fonksiyon_global_degistir():
    global d
    d = 4  # Doğrudan globaldeki d değişkenini günceller
    print("Fonksiyon içi güncel d:", d)

fonksiyon_global_degistir()
print("Fonksiyon dışı güncel d:", d)


# %% Blok Kapsamları (if / while)
# Not: 'if' ve 'while' blokları içinde tanımlanan değişkenler yerel DEĞİLDİR, global kapsama aittir.

if True:
    t = 10
    print("if bloğu içi t:", t)

print("if bloğu dışı t:", t)
