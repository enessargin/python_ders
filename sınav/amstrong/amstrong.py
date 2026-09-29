def amstrong(say_str):
    n = len(say_str)

    toplam = 0
    for rakam in say_str:
        toplam += int(rakam) ** n

    if toplam == int(say_str):
        return True

    else: 
        return False

amstrong_sayilari = []
with open("amstrong/numbers.txt", "r") as file:

    for satir in file:
        satir = satir.strip()

        if not satir:
            continue
        
        if amstrong(satir):
            amstrong_sayilari.append(satir + "\n")

with open("amstrong/amstrong.txt", "w") as file:
    file.writelines(amstrong_sayilari)