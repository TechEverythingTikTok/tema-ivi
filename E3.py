# E3

from random import randint

ROCK        = 1
PAPER       = 2
SCISSORS    = 3

ROCK_BEATS = SCISSORS
ROCK_LOSES = PAPER

PAPER_BEATS = ROCK
PAPER_LOSES = SCISSORS

SCISSORS_BEAT = PAPER
SCISSORS_LOSE = ROCK

ROCK_BEATS_SCISSORS_MESSAGE = "piatra invinge foarfeca"
PAPER_BEATS_ROCK_MESSAGE    = "hartia invinge piatra"
SCISSORS_BEAT_PAPER_MESSAGE = "foarfeca invinge hartia"

print("Hai sa jucam piatra, hartie, foarfeca.")

while True:
    rand_guess = randint(1, 3)
    user_guess = input("Piatra, hartie sau foarfeca > ").lower()
    user_guess_num = 0

    if user_guess == "piatra":
        user_guess_num = ROCK
    elif user_guess == "hartie":
        user_guess_num = PAPER
    elif user_guess == "foarfeca":
        user_guess_num = SCISSORS
    else:
        print("Ai introdus un input invalid.")
        break

    if user_guess_num == ROCK:
        if rand_guess == ROCK_BEATS:
            print("Ai castigat! Calculatorul a ales foarfeca. Ai castigat deoarece: " + ROCK_BEATS_SCISSORS_MESSAGE)
        elif rand_guess == ROCK_LOSES:
            print("Ai pierdut! Calculatorul a ales hartie. Ai pierdut deoarece: " + PAPER_BEATS_ROCK_MESSAGE)
        else:
            print("Egalitate! Tu si calculatorul ati ales piatra.")
    elif user_guess_num == PAPER:
        if rand_guess == PAPER_BEATS:
            print("Ai castigat! Calculatorul a ales piatra. Ai castigat deoarece: " + PAPER_BEATS_ROCK_MESSAGE)
        elif rand_guess == PAPER_LOSES:
            print("Ai pierdut! Calculatorul a ales foarfeca. Ai pierdut deoarece: " + SCISSORS_BEAT_PAPER_MESSAGE)
        else:
            print("Egalitate! Tu si calculatorul ati ales hartie.")
    elif user_guess_num == SCISSORS:
        if rand_guess == SCISSORS_BEAT:
            print("Ai castigat! Calculatorul a ales hartie. Ai castigat deoarece: " + SCISSORS_BEAT_PAPER_MESSAGE)
        elif rand_guess == SCISSORS_LOSE:
            print("Ai pierdut! Calculatorul a ales piatra. Ai pierdut deoarece: " + ROCK_BEATS_SCISSORS_MESSAGE)
        else:
            print("Egalitate! Tu si calculatorul ati ales foarfeca.")

    inp = input("Inca o runda? (da/nu) > ").lower()

    if inp == "da": continue
    else: break