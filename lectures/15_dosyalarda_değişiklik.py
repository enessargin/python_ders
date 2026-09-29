
# Ön Hazırlık
with open("bilgiler.txt", "w") as file:
    file.write("Enes Sargın\n")
    file.write("PoliTo Öğrencisi\n")
    file.write("Türkiye\n")

# 1. Dosya Sonuna Ekleme
with open("bilgiler.txt", "a") as file:
    file.write("Otonom Navigasyon ve Kontrol Sistemleri\n")

# 2. Dosya Başına Ekleme
with open("bilgiler.txt", "r+") as file:
    icerik = file.read()
    icerik = "Ders Materyali - Python Programlama\n" + icerik
    file.seek(0)
    file.write(icerik)

# 3. Dosya Ortasına Ekleme
with open("bilgiler.txt", "r+") as file:
    liste = file.readlines()
    liste.insert(2, "Robotik ve Yapay Zeka Laboratuvarı\n")
    file.seek(0)
    file.writelines(liste)

print("Dosya güncelleme işlemleri tamamlandı.")