number = float(input("Sisesta arv: "))

if number > 0:
    sign = "positiivne"
elif number < 0:
    sign = "negatiivne"
else:
    sign = "null"

print(f"Arv on {sign}.")

if number > 0 and number.is_integer():
    if int(number) % 2 == 0:
        print("Arv on paaris.")
    else:
        print("Arv on paaritu.")









try:
    a = float(input("Sisesta esimene arv: "))
    b = float(input("Sisesta teine arv: "))
    c = float(input("Sisesta kolmas arv: "))
    
    if a > 0 and b > 0 and c > 0:
        if a + b + c == 180:
            if a == b == c:
                print("Kolmnurk on vordkulgne.")
            elif a == b or b == c or a == c:
                print("Kolmnurk on vordhaarne.")
            else:
                print("Kolmnurk on erinevate kulgedega.")
        else:
            print("Need ei saa olla kolmnurgad, sest kulgede summa ei ole 180.")
    else:
        print("Koik arvud peavad olema positiivsed.")
except:
    print("Viga sisestamisel. Palun sisesta arvud oigesti.")



vastus = input("\nKas soovid teada saada nädala päeva nime (jah/ei)? ").lower()

if vastus == "jah":
    paev_num = int(input("Sisesta arv vahemikus 1–7: "))
    paevad = {
        1: "Esmaspäev",
        2: "Teisipäev",
        3: "Kolmapäev",
        4: "Neljapäev",
        5: "Reede",
        6: "Laupäev",
        7: "Pühapäev"
    }
    if 1 <= paev_num <= 7:
        print(f"{paev_num}. päev on {paevad[paev_num]}.")
    else:
        print("Arv peab olema vahemikus 1–7!")
else:
    print("Olgu, ei küsi päeva nime.")



    paev = int(input("\nSisesta sünnipäeva päev (1–31): "))
kuu = int(input("Sisesta sünnikuu (1–12): "))

if 1 <= kuu <= 12 and 1 <= paev <= 31:
    if (kuu == 3 and paev >= 21) or (kuu == 4 and paev <= 19):
        taht = "Jäär"
    elif (kuu == 4 and paev >= 20) or (kuu == 5 and paev <= 20):
        taht = "Sõnn"
    elif (kuu == 5 and paev >= 21) or (kuu == 6 and paev <= 20):
        taht = "Kaksikud"
    elif (kuu == 6 and paev >= 21) or (kuu == 7 and paev <= 22):
        taht = "Vähk"
    elif (kuu == 7 and paev >= 23) or (kuu == 8 and paev <= 22):
        taht = "Lõvi"
    elif (kuu == 8 and paev >= 23) or (kuu == 9 and paev <= 22):
        taht = "Neitsi"
    elif (kuu == 9 and paev >= 23) or (kuu == 10 and paev <= 22):
        taht = "Kaalud"
    elif (kuu == 10 and paev >= 23) or (kuu == 11 and paev <= 21):
        taht = "Skorpion"
    elif (kuu == 11 and paev >= 22) or (kuu == 12 and paev <= 21):
        taht = "Ambur"
    elif (kuu == 12 and paev >= 22) or (kuu == 1 and paev <= 19):
        taht = "Kaljukits"
    elif (kuu == 1 and paev >= 20) or (kuu == 2 and paev <= 18):
        taht = "Veevalaja"
    else:
        taht = "Kalad"
    print("Sinu tähemärk on:", taht)
else:
    print("Vigased andmed – kontrolli kuu ja päeva väärtusi!")




    val = input("\nSisesta väärtus: ")

try:
    # Proovime esmalt teisendada täisarvuks
    if '.' not in val:
        num = int(val)
        print("Tegu on täisarvuga. 50% sellest on:", num * 0.5)
    else:
        # Kui sisaldab koma, siis ujukomaarv
        num = float(val)
        print("Tegu on ujukomaarvuga. 70% sellest on:", num * 0.7)
except ValueError:
    # Kui teisendamine ei õnnestu, on tekst
    if val.isalpha():
        print("Tegu on tekstiga:", val)
    else:
        print("Sisestatud väärtus ei ole arv ega puhas tekst.")



soov = input("\nKas soovid lahendada ruutvõrrandi (jah/ei)? ").lower()

if soov == "jah":
    a = float(input("Sisesta a: "))
    b = float(input("Sisesta b: "))
    c = float(input("Sisesta c: "))

    D = b ** 2 - 4 * a * c
    print("Diskriminant D =", D)

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"Kaks lahendust: x₁ = {x1}, x₂ = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Üks lahendus: x = {x}")
    else:
        print("Reaalarvulisi lahendusi ei ole.")
else:
    print("Head aega!")
