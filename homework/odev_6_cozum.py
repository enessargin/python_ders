
# =============================================================================
# PROJE 1 ÇÖZÜMÜ: Harf Notlarına Göre Kalanlar ve Geçenler
# =============================================================================

def not_hesapla(satir):
    satir = satir.strip()
    if not satir:
        return None
    
    elemanlar = satir.split(",")
    isim = elemanlar[0]
    vize1 = int(elemanlar[1])
    vize2 = int(elemanlar[2])
    final = int(elemanlar[3])
    
    toplam_not = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
    
    if toplam_not >= 90:
        harf = "AA"
    elif toplam_not >= 85:
        harf = "BA"
    elif toplam_not >= 80:
        harf = "BB"
    elif toplam_not >= 75:
        harf = "CB"
    elif toplam_not >= 70:
        harf = "CC"
    elif toplam_not >= 65:
        harf = "DC"
    elif toplam_not >= 60:
        harf = "DD"
    elif toplam_not >= 55:
        harf = "FD"
    else:
        harf = "FF"
        
    durum = "Gecti" if harf not in ["FD", "FF"] else "Kaldi"
    return isim, harf, durum

# Örnek Notlar Dosyası Oluşturma
with open("notlar.txt", "w") as file:
    file.write("Ahmet Yılmaz,70,60,80\n")
    file.write("Mehmet Demir,40,50,30\n")
    file.write("Ayşe Kaya,85,90,95\n")
    file.write("Fatma Çelik,50,45,50\n")

gecenler = []
kalanlar = []

with open("notlar.txt", "r") as file:
    for satir in file:
        sonuc = not_hesapla(satir)
        if sonuc:
            isim, harf, durum = sonuc
            bilgi = f"{isim} -> Harf Notu: {harf}\n"
            if durum == "Gecti":
                gecenler.append(bilgi)
            else:
                kalanlar.append(bilgi)

with open("gecenler.txt", "w") as file:
    file.writelines(gecenler)

with open("kalanlar.txt", "w") as file:
    file.writelines(kalanlar)

print("Proje 1 tamamlandı: 'gecenler.txt' ve 'kalanlar.txt' oluşturuldu.")


# =============================================================================
# PROJE 2 ÇÖZÜMÜ: Futbolcuları Takımlarına Göre Ayırma
# =============================================================================

# Örnek Futbolcular Dosyası Oluşturma
with open("futbolcular.txt", "w") as file:
    file.write("Fernando Muslera,Galatasaray\n")
    file.write("Atiba Hutchinson,Beşiktaş\n")
    file.write("Simon Kjaer,Fenerbahçe\n")
    file.write("Mauro Icardi,Galatasaray\n")
    file.write("Edin Dzeko,Fenerbahçe\n")
    file.write("Vincent Aboubakar,Beşiktaş\n")

gs = []
bjk = []
fb = []

with open("futbolcular.txt", "r") as file:
    for satir in file:
        satir = satir.strip()
        if not satir:
            continue
        satir_elemanlari = satir.split(",")
        isim = satir_elemanlari[0]
        takim = satir_elemanlari[1]
        
        if takim == "Fenerbahçe":
            fb.append(satir + "\n")
        elif takim == "Galatasaray":
            gs.append(satir + "\n")
        elif takim == "Beşiktaş":
            bjk.append(satir + "\n")

with open("gs.txt", "w") as file1:
    file1.writelines(gs)

with open("fb.txt", "w") as file2:
    file2.writelines(fb)

with open("bjk.txt", "w") as file3:
    file3.writelines(bjk)

print("Proje 2 tamamlandı: 'gs.txt', 'fb.txt' ve 'bjk.txt' oluşturuldu.")