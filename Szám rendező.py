
""" addig kérünk be számot míg 0-át nem ad meg a felhasználó. Megkérdezzük. 1: + 2: - 3:páros 4:Összes szám""" 
print("Addig kérünk be számot, míg a felhasználó 0-át nem ad meg.\n \n")
szam=int(input("Kérek egy számot:"))
lista = []
while  szam != 0 :
    lista.append(szam)
    szam=int(input("Kérek egy számot:"))

menu=int(input("1: Pozitív számok, 2:Negatív számok 3:Páros számok, 4:Páratlan számok, 5:Összes szám: "))
if menu == 1:
    print("Pozitív számok: ")
    for i in lista:
        if i >= 0:
            print("  - ",i)
            
elif menu == 2:
    print("Negatív számok: ")
    for i in lista:
        if i < 0:
            print("  - ",i)

elif menu == 3:
    print("Páros számok: ")
    for i in lista:
        if i %2==0:
            print("  - ",i)
elif menu == 4:
    print("Páratlan számok: ")
    for i in lista:
        if i%2!=0:
             print("  - ",i)

elif menu == 5:
    print("Összes szám: ")
    for i in lista:
         print("  - ",i)
else:
    print("Nincs ilyen menü pont!")
    
a = input("")

        

    




