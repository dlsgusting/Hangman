import random
playing = True

words = ["hello","bye", "today", "what", "goodbye"]
valid_answer = "abcdefghijklmnopqrstuvwxyz"
used_letters = ["a","b","c"]

random_int = random.randint(0, len(words) -1)
word_list = list(words[random_int])
guess_list = []
for i in words[random_int]:
    guess_list.append(0)

def choose_letter():
    print("Choose a letter a-z")
    letter = str(input())
    while letter not in valid_answer:
        print("You didn't choose a letter, choose gain.")
        letter = str(input())
    return letter



while playing:
    print(f"Current solve: {guess_list_display}")
    letter = game()

    if letter in words[random_int]:
        position = word_list.index(letter)
        guess_list[position] = letter

    playing = False