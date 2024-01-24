import random

def pozdrav():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generuj_tajne_cislo():
    cislo = ''.join(random.sample('123456789', 4))
    return cislo

def ohodnot_hadani(tajne_cislo, tip):
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    return bulls, cows

def vypis_vyhodnoceni(bulls, cows):
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

def main():
    pozdrav()
    
    tajne_cislo = generuj_tajne_cislo()
    hadal = False
    pokusy = 0

    while not hadal:
        tip = input("Enter a number:\n-----------------------------------------------\n>>> ")
        
        if len(tip) != 4 or not tip.isdigit() or tip[0] == '0' or len(set(tip)) < 4:
            print("Please enter a valid 4-digit number with unique digits.")
            continue

        pokusy += 1
        bulls, cows = ohodnot_hadani(tajne_cislo, tip)

        vypis_vyhodnoceni(bulls, cows)

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {pokusy} {'guess' if pokusy == 1 else 'guesses'}!")
            hadal = True

if __name__ == "__main__":
    main()