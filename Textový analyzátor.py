"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kýr
email: jerenimo@seznam.cz
discord: Jan K.
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


#Vyžádá si od uživatele přihlašovací jméno a heslo

cara = "-" * 45

username= {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
    }

pocet_textu = len(TEXTS)


print("Vítejte v našem textovém analyzátoru!")
print(cara)

uzivatel = input("username: ")
heslo = input("password: ")
print(cara)

if uzivatel in username:
    spravne_heslo = username[uzivatel]
    if heslo == spravne_heslo:
        print("Vítejte v aplikaci,", uzivatel,)
        print(f"Vy máte",{pocet_textu}, "texty, které je třeba analyzovat.")
        print(cara)
    else:
        print("Špatné heslo, ukončuji program.")
        quit()
else:
    print("Neregistrovaný uživatel, ukončuji program.")
    quit()


#Program nechá uživatele vybrat mezi texty, uloženými v proměnné TEXTS

vyber_textu = input(f"Zadejte číslo 1 až {pocet_textu} pro výběr: ")

if not vyber_textu.isdigit():
    print("Neplatný vstup. Musíte zadat číslo. Ukončuji program.")
    quit()

vyber_textu = int(vyber_textu)

if vyber_textu < 1 or vyber_textu > pocet_textu:
    print("Neplatná volba čísla textu. Ukončuji program.")
    quit()

vybrany_text =  TEXTS[vyber_textu -1]
print(cara)


#Pro vybraný text spočítá následující statistiky
#počet slov

slova = vybrany_text.split()
pocet_slov = len(slova)
print(f"Počet slov ve vybraném textu: {pocet_slov}")

#počet slov začínajících velkými písmeny

pocet_slov_VP = 0
for slovo in slova:
    if slovo.istitle():
        pocet_slov_VP += 1

print(f"Počet slov začínajících velkým písmenem: {pocet_slov_VP}")

#počet slov psaných velkými písmeny
 
pocet_slov_velkymi = 0

for slovo in slova:
    if slovo.isupper() and slovo.isalpha():
        pocet_slov_velkymi += 1

print(f"Počet slov psaných velkými písmeny: {pocet_slov_velkymi}")

#počet slov psaných malými písmeny

pocet_slov_malymi = 0

for slovo in slova:
    if slovo.islower():
        pocet_slov_malymi += 1

print(f"Počet slov psaných malými písmeny: {pocet_slov_malymi}")

#počet čísel (ne cifer)

pocet_cisel = 0

for slovo in slova:
    if slovo.isdigit():
        pocet_cisel += 1

print(f"Počet čísel: {pocet_cisel}")

#sumu všech čísel (ne cifer) v textu

suma_cisel = 0

for slovo in slova:
    if slovo.isdigit():
        suma_cisel += int(slovo)

print(f"Suma všech čísel v textu: {suma_cisel}")

print(cara)

#Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu

print("LEN|  OCCURENCES  |NR.")
print(cara)

vyskyt_slov_delka = {}

for slovo in slova:
    delka_slova = len(slovo)
    if delka_slova not in vyskyt_slov_delka:
        vyskyt_slov_delka[delka_slova] = 1
    else:
        vyskyt_slov_delka[delka_slova] += 1
        
for delka, pocet in sorted(vyskyt_slov_delka.items()):
    print(f"{delka:3d}| {'*'*pocet:12s} | {pocet:1d}")
print(cara)












