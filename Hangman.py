import random
import string
import os
import words
import hangmanstages
from words import wordList
from hangmanstages import stages

def displayHangman(tries):
    return stages [tries]

def getWord():
    word = random.choice(wordList)
    return word.upper()

os.system('cls')
print("          HANGMAN            ")
print ("---------------------------")
name = (input("      Wat is je naam? "))

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6

    os.system('cls')
    print("          HANGMAN            ")
    print ("---------------------------")
    print ("Hallo, ", name)
    print("Laten we beginnen")
    print(displayHangman(tries))
    print(wordCompletion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Raad een letter of een woord: ").upper()

        if len(guess) == 1 and guess.isalpha():
            os.system('cls')
            if guess in guessedLetters:
                print("          HANGMAN            ")
                print ("---------------------------")
                print("Deze letter heb je al gerade: ", guess)
                

            elif guess not in word:
                os.system('cls')
                print("          HANGMAN            ")
                print ("---------------------------")
                print(guess, "is niet juist.")
                tries -= 1
                print("Je hebt nog", tries, "pogingen")
                guessedLetters.append(guess)

            else:
                os.system('cls')
                print("          HANGMAN            ")
                print ("---------------------------")
                print(guess, "is juist.")
                guessedLetters.append(guess)
                word_as_list = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                wordCompletion = "".join(word_as_list)
                if "_" not in wordCompletion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                os.system('cls')
                print("          HANGMAN            ")
                print ("---------------------------")
                print("Dit woord heb je al geraden.", guess)

            elif guess != word:
                os.system('cls')
                print("          HANGMAN            ")
                print ("---------------------------")
                print(guess, "is niet het juiste woord.")
                tries -= 1
                print("Je hebt nog", tries, "pogingen")
                guessedWords.append(guess)

            else:
                guessed = True
                wordCompletion = word

        else:
            os.system('cls')
            print("          HANGMAN            ")
            print ("---------------------------")
            print("Dit is geen geldige schatting.")
        print(displayHangman(tries))
        print(wordCompletion)
        print("\n")

    if guessed:
        os.system('cls')
        print("               HANGMAN            ")
        print ("    ---------------------------")
        print("_______________________________________")
        print("|       Je hebt het woord geraden.    |")
        print("   Je had nog", tries, "pogingen over.   ")
        print("|______________________________________|")

    else:
        os.system('cls')
        print("               HANGMAN            ")
        print ("    ---------------------------")
        print("_______________________________________")
        print("|             Je bent af.              |")
        print("         Het woord was", word, "           ")
        print("|______________________________________|")

def main():
    word = getWord()
    play(word)

    while input("Wil je opnieuw spelen? (J/N) ").upper() == "J":
        word = getWord()
        play(word)


if __name__ == "__main__":
    main()