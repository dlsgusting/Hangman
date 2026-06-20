import random
playing = True

words = ["hello","bye", "today", "what", "goodbye"]
used_letters = ["a","b","c"]

def game():
    random_int = random.randint(0, len(words) -1)
    guess_list = []
    for i in range(len(words[random_int])):
        guess_list.append(0)
    print(f"Current solve: {guess_list}")

while playing:
    game()
    playing = False