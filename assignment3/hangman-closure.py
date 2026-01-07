def make_hangman(secret_word):
    guesses=[]
    secretset=set(secret_word)
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        guesschars=set(guesses)
        result=[]
        for charecter in secret_word:
            if charecter in guesschars:
                result.append(charecter)
            else:
                result.append('_')
        print("".join(result))

        if secretset.issubset(guesschars):
            return True
        else:
            return False
    return hangman_closure



mesage="Define secret! "
secret_word = input(mesage)
game=make_hangman(secret_word)
game_won = False
while not game_won:
    newguess = input("Guess again! ")
    game_won=game(newguess)

if game_won:
    print("Congratulations! You guessed the word.")
