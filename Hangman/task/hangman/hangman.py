import random

amount_wins = 0
amount_loses = 0
word_list = ["python", "java", "swift", "javascript"]


def print_word(guessed):
    global word, hint, guessed_word
    for i in range(len(word)):
        if word[i] in guessed:
            hint[i] = word[i]
    print("")
    guessed_word = ''.join(hint)
    print(guessed_word)


print("H A N G M A N")
game_type = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
while game_type != "exit":
    if game_type == "play":
        remaining_attempts = 8
        word = random.choice(word_list)
        hint = list(len(word) * "-")
        end_of_game = False
        guesses = []
        guessed_word = ""

        print(f"\n{len(word) * '-'}")
        while remaining_attempts > 0:
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("Please, input a single letter.")
            elif not guess.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif guess in guesses:
                print("You've already guessed this letter.")
            elif guess in set(word) and guess not in guesses:
                guesses.append(guess)
            else:
                guesses.append(guess)
                print("That letter doesn't appear in the word.")
                remaining_attempts -= 1
            print_word(guesses)
            if guessed_word == word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                amount_wins += 1
                end_of_game = True
                break

        if remaining_attempts == 0 and not end_of_game:
            print("You lost!")
            amount_loses += 1

        print("\nThanks for playing!")
    elif game_type == "results":
        print(f"You won: {amount_wins} times.")
        print(f"You lost: {amount_loses} times.")

    game_type = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
