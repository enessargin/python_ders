
# -----------------------------------------------------------------------------
# 1. DOSYA AÇMAK VE KAPATMAK
# -----------------------------------------------------------------------------
file = open("bilgiler.txt", "w")
file.close()

# -----------------------------------------------------------------------------
# 2. "w" KİPİ İLE DOSYAYA YAZMAK
# -----------------------------------------------------------------------------
file = open("bilgiler.txt", "w")

file.write("Enes Sargın\n")
file.write("Politecnico di Torino - PoliTo\n")
file.write("Türkiye\n")

file.close()

# -----------------------------------------------------------------------------
# 3. "a" KİPİ İLE DOSYAYA EKLEME YAPMAK (Append)
# -----------------------------------------------------------------------------
file = open("bilgiler.txt", "a")

file.write("Elektronik ve Haberleşme Mühendisliği\n")
file.write("Robotik ve Otonom Sistemler\n")

file.close()

print("Dosya açma ve yazma işlemleri başarıyla tamamlandı.")