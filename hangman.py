import random
playing = True

words = ["hello","bye", "today", "what", "goodbye"]
valid_answer = "abcdefghijklmnopqrstuvwxyz"
used_letters = []

random_int = random.randint(0, len(words) -1)
the_word = words[random_int]
word_list = list(the_word)
guess_list = [0 for letter in the_word]
chances = 6


def game_state():
    gamestate = ["solve","guess"]
    print("Solve or guess?")
    chosen = input().lower()
    while chosen not in gamestate:
        print("not a valid option, choose again")
        chosen = input().lower()
    
    return chosen


def choose_letter():
    print("Choose a letter a-z")
    letter = str(input()).lower()
    while letter not in valid_answer or letter in used_letters or len(letter) != 1:
        print("invalid input, choose again.")
        letter = str(input()).lower()
    return letter

def solve():
    print("What is the word?")
    word_guess = input().lower()

    return word_guess

while playing:
    if chances == 0:
        print(f"You ran out of tries, you lose! The word was {the_word}")
        playing = False
        break
    elif 0 not in guess_list:
        print(f"You win! You had {chances} lives left.")
        playing = False
        break

    print(f"Current solve: {guess_list}")
    print(f"Used letters {used_letters}")

    chosen = game_state()

    if chosen == "solve":
        player_solution = solve()
        if player_solution != the_word:
            chances -= 1
            print(f"Wrong, you have {chances} chances left.")
        else:
            print(f"Correct. you win! You had {chances} lives left.")
            playing = False
            break
        continue
        
    letter = choose_letter()
    

    if letter in the_word:
        print("Correct!")
        for index, let in enumerate(the_word):
            if letter == let:
                guess_list[index] = letter
        used_letters.append(letter)
    else:
        chances -= 1
        print(f"Wrong, you have {chances} chancecs left.")
        used_letters.append(letter)

