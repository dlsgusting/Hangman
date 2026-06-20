import random
playing = True

words = ["hello","bye", "today", "what", "goodbye"]
valid_answer = "abcdefghijklmnopqrstuvwxyz"
used_letters = ["a","b","c"]

random_int = random.randint(0, len(words) -1)
guess_list = {}
guess_list_display = []
for i in words[random_int]:
    guess_list[i] = 0
    guess_list_display.append(0)

def choose_letter():
    print("Choose a letter a-z")
    letter = input()
    while letter not in valid_answer:
        print("You didn't choose a letter, choose gain.")
        letter = input()
    return letter



while playing:
    print(f"Current solve: {guess_list_display}")
    game()
    playing = False