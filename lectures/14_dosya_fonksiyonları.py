

# -----------------------------------------------------------------------------
# 1. DOSYALARI OTOMATİK KAPATMA (with open)
# -----------------------------------------------------------------------------
print("--- 'with' Bloğu Kullanımı ---")
with open("bilgiler.txt", "r") as file:
    for satir in file:
        print(satir, end="")

# -----------------------------------------------------------------------------
# 2. İMLEÇ KONUMU (tell) VE İMLEÇ HAREKETİ (seek)
# -----------------------------------------------------------------------------
print("\n\n--- Imleç Hareketleri (tell ve seek) ---")
with open("bilgiler.txt", "r") as file:
    print("Başlangıç Konumu:", file.tell())
    
    file.seek(5)
    print("seek(5) sonrası konum:", file.tell())
    
    icerik = file.read(10)
    print("Okunan 10 Karakter:", icerik)
    
    file.seek(0)
    print("Başa dönüldü, ilk 6 karakter:", file.read(6))