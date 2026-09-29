ucus_kapasite = {}
ucus_koltuklar = {} #["","","",""]

with open("flights/flights.txt", "r") as file:

    for satir in file:
        satir = satir.strip() 

        if not satir:
            continue

        elemanlar = satir.split()

        flight_id = elemanlar[0]
        rows = int(elemanlar[2]) 
        cols = int(elemanlar[3])

        toplam_koltuk = rows * cols
        ucus_kapasite[flight_id] = (rows, cols)

        koltuklar = []

        for i in range(toplam_koltuk):
            koltuklar.append("")
        ucus_koltuklar[flight_id] = koltuklar

with open("flights/bookings.txt", "r") as file:

    for satir in file:
        satir = satir.strip() 
    
        if not satir:
            continue
    
        elemanlar = satir.split()
        op_code = elemanlar[0]
        flight_id = elemanlar[1]

        if op_code == "BOOK":
            isim = elemanlar[2] + " " + elemanlar[3]
            koltuk_sayisi = int(elemanlar[4])

            bos_koltuklar = []

            for i in range(len(ucus_koltuklar[flight_id])):
                if ucus_koltuklar[flight_id][i] == "":
                    bos_koltuklar.append(i)

            if len(bos_koltuklar) >= koltuk_sayisi:

                for i in range(koltuk_sayisi):
                    hedef_index = bos_koltuklar[i]
                    ucus_koltuklar[flight_id][hedef_index] = isim

                else:
                    print("{} - Fail".format(satir))

        elif op_code == "CANCEL":

            isim = elemanlar[2] + " " + elemanlar[3]

            for i in range(len(ucus_koltuklar[flight_id])):
                if ucus_koltuklar[flight_id][i] == isim:
                    ucus_koltuklar[flight_id][i] = ""

for flight_id in ucus_koltuklar:

    print("Flight {}:".format(flight_id))

    rows, cols = ucus_kapasite[flight_id]
    index = 0

    for r in range(1, rows+1):
        for c in range(1, cols+1):
            kisi = ucus_koltuklar[flight_id][index]

            if kisi != "":
                print("{}, {}, {}".format(r,c,kisi))
            index += 1

