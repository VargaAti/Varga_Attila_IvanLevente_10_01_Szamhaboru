"""
Követelmények:
Bevezetés


A program üdvözölje a játékost, pl.:
 "Üdv a Számháború játékban!"


Játékos választása


A felhasználó írjon be egy számot 1–6 között.
Ha nem megfelelő számot ad meg (pl. 0 vagy 9), figyelmeztesse: "Csak 1 és 6 közötti számot adhatsz meg!"


Gép választása


A számot a gép véletlenszerűen válassza 1-6 között.


Győztes eldöntése (if/elif/else)


Ha a játékos száma > gép száma → "Nyertél!"
Ha a játékos száma < gép száma → "Vesztettél!"
Ha a kettő egyenlő → "Döntetlen!"


Pontszám nyilvántartása


A játék folyamán tárolni kell, hogy hányat nyert, vesztett és döntetlenezett a játékos.


Újra játszás


Minden kör után kérdés: Szeretnél újra játszani? (i/n)
Ha n, a program írja ki az összesített eredményt, pl.:
Végső eredmény: 3 nyerés, 2 vereség, 1 döntetlen.
"""
import random as r
folytatja = True
nyer_pontszam = 0
veszt_pontszam = 0
dont_pontszam = 0


while folytatja:
    #bekérjük a játékostól a számot és a gép is generál egy számot
    print("Üdv a számháború játékában!")
    felhasznalo = (input("Adj meg egy egész számot 1 és 6 között: "))
    gep = r.randint(1,6)
    
    if felhasznalo.isalpha():
        print("Csak számot adhatsz meg!")
        continue  # Ha betűt adott meg, ismét kéri a számot

    felhasznalo = int(felhasznalo)

    #összehasonlítjuk a gép és a felhasználó számát
    if felhasznalo > 6:
        print("Csak 1 és 6 közötti számot adhatsz meg!")
        break
    elif felhasznalo == gep:
        print("Döntetlen")
        dont_pontszam += 1
    elif felhasznalo > gep:
        print("Nyertél")
        nyer_pontszam += 1
    elif felhasznalo < gep:
        print("Vesztettél")
        veszt_pontszam += 1

    print(f"Eddigi eredmény: {nyer_pontszam} nyerés, {veszt_pontszam} vereség, {dont_pontszam} döntetlen.")

    ujrajatszod = input("Szeretnél újra játszani? i/n ")

    #újrajátszás
    if ujrajatszod != "i" and ujrajatszod != "n":
        print("Helytelen formátum! i/n")
        continue
    
    #helytelen adat bevitelének kezelése
    elif ujrajatszod == "n":
        print(f"Végő eredmény: {nyer_pontszam} nyerés, {veszt_pontszam} vereség, {dont_pontszam} döntetlen.")
        folytatja = False
        break