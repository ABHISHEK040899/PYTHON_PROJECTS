import random
import time
print("\n Weilcom to Hangman game\n****@@@****\nCreated by: ABHISHEK SHARMA\n****@@@****")
name=input("Enter your name: \n")
print(f"HELLOW {name} ! BEST OF LUCK!")
time.sleep(2)
print("THE GAME IS GOING TO START \n LET'S PLAY......'")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess=["ABHISHEK","ANSHU","NEHA","RAGHAV","VANSH","TUTION","MRIDUL"]
    word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display="_"*length
    already_guessed=[]
    play_game=""
def play_loop():
    global play_game
    play_game=input("DO YOU WANT TO PLAY AGAIN ? y=yes,n=no\n")
    while play_game not in ["Y","N","y","n"]:
        play_game = input("DO YOU WANT TO PLAY AGAIN ? y=yes,n=no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print(f"THANK YOU PLAYING {name.upper()}! ")
        exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit=5
    guess=input(f"THIS IS THE HANGMAN WORD: {display} Enter your guess in capital letter:\n")
    guess=guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print("INVALID INPUT, TRY A LETTER\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_"+word[index+1:]
        print(display+"\n")
    elif guess in already_guessed:
        print("TRY ANOTHER LETTER.\n")
    else:
        count +=1
        if count==1:
            time.sleep(2)
            print("   _______\n"
                  "   |       \n"
                  "   |       \n"
                  "   |       \n"
                  "   |       \n"
                  "   |       \n"
                  "   |       \n"
                  "___|____    \n")
            print("wrong guess."+ str(limit-count) +"guesses remaining \n")
        elif count==2:
            time.sleep(2)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print("**********@@@@@@@@@*********\n Congrats! You have guessed the word correctly!\n **********@@@@@@@@*********")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()





