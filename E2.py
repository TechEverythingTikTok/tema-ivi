# E2

from random import randint

guesses = 0
num = randint(1, 10000)

print("Ma gandesc la un numar intre 1 si 10000...")

while True:
    guesses += 1
    guess = int(input("Ghici un numar > "))
    if guess > num:
        print("Numarul tau este prea mare.")
    elif guess < num:
        print("Numarul tau este prea mic.")
    else:
        print("Ai ghichit! Felicitari")
        break

print("Ai ghicit numarul in " + str(guesses) + " de incercari")