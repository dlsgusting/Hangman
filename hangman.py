playing = True

words = ["hello","bye", "today", "what"]
used_letters = ["a","b","c"]

def game():
    random_int = random.randint(0, len(words))
    guess_list = []
    for i in range(len(words[random_int])):
        guess_list.appenmd(0)

while playing:
    break