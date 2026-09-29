
noktalama_isaretleri = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
temiz_metin = ""



with open("strawberry/strawberry.txt","r") as file:
    tum_metin = file.read()

    for karakter in tum_metin:

        if karakter in noktalama_isaretleri:
                temiz_metin += " "
        else:
            temiz_metin += karakter,


kelimeler = temiz_metin.split()

for i in range(len(kelimeler)-2):

    k1 = kelimeler[i]
    k2 = kelimeler[i + 1]
    k3 = kelimeler[i + 2]

    if len(k1) == len(k2) == len(k3):
        ucle_tuple = (k1.upper(), k2.upper(),k3.upper())
        print(ucle_tuple)

