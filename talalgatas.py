
"""
(ezt a feladatot while ciklussal érdemes megoldani)
Írj egy számkitaláló programot, ami előre gondol egy számra, majd erre vár tippeket.
A program segítsen egy-egy rossz tipp esetén, hogy milyen irányban érdemes tovább kutakodni. 
A program számolja, hogy hány tippből tudta eltalálni az illető a gondolt számot.
Például:
Gondoltam.
75   (a felhasználó írta be)
Mondj kisebbet
50
Mondj kisebbet
28
Mondj nagyobbat
40
Mondj kisebbet
30
Mondj kisebbet
29
TALÁLT!
"""

import random
kitalaltszam = random.randint(1, 100)
print("Gondoltam")
felhasznalo = 0
#print(kitalaltszam)

while kitalaltszam != felhasznalo:
    felhasznalo = int(input())
    if felhasznalo > kitalaltszam:
        print("Mondj kisebbet")
    if felhasznalo < kitalaltszam:
        print("Mondj nagyobbat")
    if felhasznalo == kitalaltszam:
        print("TALÁLT!")

