mesta = ["Praha", "Viden", "Olomouc", "Svitavi", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,-Kc
2 - Viden   | 200,-Kc
3 - Olomouc | 120,-Kc
4 - Svitavy | 120,-Kc
5 - Zlin    | 100,-Kc
6 - Ostrava | 180,-Kc
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara, nabidka, end="")
print(cara)

destinace = input("CISLO DESTINACE: ")
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
email = input("EMAIL: ")
print(cara)

cilova_stanice = mesta[int(destinace) -1]
cilova_cena = ceny[int(destinace) -1]

print(cilova_stanice)
print(cilova_cena, ",-Kc")
print(cara)

print("Cestujici: ", jmeno, prijmeni)
print("Cilova stanice: ", cilova_stanice)  
print("Cena jizdneho: ", cilova_cena, ",-Kc")
print("Jizdenku jsme odeslali na  e-mail: ", email)    
print("Ahoj")