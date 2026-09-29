# ==============================================================================
# SÖZLÜKLER (DICTIONARIES)
# ==============================================================================
# Sözlükler, verileri sırayla (indeksle) değil, "Anahtar-Değer" (Key-Value)
# ilişkisiyle tutan veritipleridir.
# Örnek: 'freedom' (Key) -> 'özgürlük' (Value)
# ==============================================================================

# %% [1. Sözlük Oluşturma]
# ------------------------------------------------------------------------------
# Süslü parantez {} ve iki nokta (:) kullanarak key:value çiftleri tanımlanır.

sozluk1 = {"sıfır": 0, "bir": 1, "iki": 2, "üç": 3}
print("Sözlük 1:", sozluk1)

# Boş sözlük oluşturma yöntemleri:
bos_sozluk_1 = {}
bos_sozluk_2 = dict()
print("Boş sözlük örneği:", bos_sozluk_1)


# %% [2. Değerlere Erişmek ve Değiştirmek]
# ------------------------------------------------------------------------------
# Elemanlara ulaşmak için indeks numarası yerine anahtar (Key) ismi kullanılır.

print("'bir' anahtarının değeri:", sozluk1["bir"])
print("'iki' anahtarının değeri:", sozluk1["iki"])

# Olmayan bir anahtar çağrıldığında hata alınır:
try:
    print(sozluk1["beş"])
except:
    print("[HATA ÖRNEĞİ]")

# Karmaşık yapıda sözlükler ve değer güncelleme:
a = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "üç": 15}

print("'iki' anahtarının listesi:", a["iki"])
# İç içe yapılardan eleman çekme:
print("İç içe listeden eleman çekme (a['iki'][1][1]):", a["iki"][1][1])

# Değer güncelleme:
a["üç"] += 5
print("'üç' anahtarının güncellenmiş değeri:", a["üç"])


# %% [3. Dinamik Eleman Ekleme ve Sıralama]
# ------------------------------------------------------------------------------
# Sözlüklere sonradan yeni bir anahtar-değer çifti eklenebilir.

a = {"bir": 1, "iki": 2, "üç": 3}
a["dört"] = 4
print("Yeni eleman eklenmiş sözlük:", a)


# %% [4. İç İçe (Nested) Sözlükler]
# ------------------------------------------------------------------------------
# Sözlüklerin içinde başka sözlükler tanımlanabilir.

a = {
    "sayılar": {"bir": 1, "iki": 2, "üç": 3},
    "meyveler": {"kiraz": "yaz", "portakal": "kış", "erik": "yaz"}
}

print("Sayılar sözlüğünden 'bir':", a["sayılar"]["bir"])
print("Meyveler sözlüğünden 'kiraz' mevsimi:", a["meyveler"]["kiraz"])


# %% [5. Temel Sözlük Metodları]
# ------------------------------------------------------------------------------
yeni_sozluk = {"bir": 1, "iki": 2, "üç": 3}

# values(): Sözlüğün sadece değerlerini (values) getirir.
print("Values (Değerler):", yeni_sozluk.values())

# keys(): Sözlüğün sadece anahtarlarını (keys) getirir.
print("Keys (Anahtarlar):", yeni_sozluk.keys())

# items(): Anahtar ve değerleri demet (tuple) ikilileri halinde getirir.
print("Items (Çiftler):", yeni_sozluk.items())