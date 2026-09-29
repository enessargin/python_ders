# ==============================================================================
# KULLANICI GİRİŞİ KONTROL SİSTEMİ
# ==============================================================================
# Bu örnekte 'and', '==' ve '!=' mantıksal operatörleri kullanılarak
# kullanıcı adı ve parola doğrulama senaryoları simüle edilmektedir.
# ==============================================================================

# %% [1. Sistem Verilerinin Tanımlanması]
# ------------------------------------------------------------------------------
print("********************\nKullanıcı Giriş Paneli\n********************\n")

# Sistemde kayıtlı varsayılan bilgiler:
sys_kul_adi = "enes"
sys_parola = "12345"

# Kullanıcıdan giriş bilgilerini alıyoruz:
kullanici_adi = input("Kullanıcı Adınızı Giriniz: ")
parola = input("Parolanızı Giriniz: ")


# %% [2. Doğrulama ve Hata Kontrolleri]
# ------------------------------------------------------------------------------

# Durum 1: Kullanıcı adı yanlış, Parola doğruysa
if kullanici_adi != sys_kul_adi and parola == sys_parola:
    print("\n[HATA] Kullanıcı Adı Hatalı!")

# Durum 2: Kullanıcı adı doğru, Parola yanlışsa
elif kullanici_adi == sys_kul_adi and parola != sys_parola:
    print("\n[HATA] Parola Hatalı!")

# Durum 3: İki bilgi de yanlışsa
elif kullanici_adi != sys_kul_adi and parola != sys_parola:
    print("\n[HATA] Kullanıcı Adı ve Parola Hatalı!")

# Durum 4: Bütün şartlar doğrulandıysa (İki bilgi de doğru)
else:
    print("\n[BAŞARILI] Tebrikler, başarıyla giriş yaptınız!")