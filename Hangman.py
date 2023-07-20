
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

from queue import Empty
import random
import time                                                               
# Define the game function
def play_game():

    # Read in the file
    text_file_out_R = open("countries.txt", "r")
    text_file_out = text_file_out_R.readlines()
    Countries = ""
    for line in text_file_out:
        Countries += line

    # Split the countries by lines and define the chosen word and word length
    countries = Countries.split()
    chosen_word = random.choice(countries)
    chosen_word = chosen_word.lower()
    word_length = len(chosen_word)

    # Create a variable called 'lives' to keep track of the number of lives left. 
    lives = 6
    # The game is running
    end_of_game = False
    
    # Design and game information
    print(logo)
    time.sleep(1)
    print("\nHangman - Country Edition")
    time.sleep(1)
    print("\n\tEach gap represents a letter or space (use '.' to guess a space.)")
    time.sleep(1)

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
    while not end_of_game:
    #Join all the elements in the list and turn it into a String.
        print(f"\n{' '.join(display)}")

        print(stages[lives])
        # guessing question
        guess = input("Guess a letter: ").lower()

        # If the user has entered a letter they've already guessed or didnt use any letters, print a message to let them know.
        if guess in display:
            print(f"\nYou've already guessed {guess}")
        elif guess == "":
            print(f"\nYou've not guessed anything")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
            elif letter =="":
                display[position] and print(f"\nYou have not guessed anything")

        #Check if user is wrong.
        if guess not in chosen_word:
            # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("\nYou lose. The country is ", chosen_word)

        print(stages[lives])

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("\nYou win!!!\n The country is ", chosen_word)
        
        
    restart = input("Press 'y' to play again or press 'n' to stop playing ")
    while end_of_game == True:
        restart
        if restart == 'y' or restart == 'Y':
            play_game()
        elif restart == 'n' or restart == 'N':
            print("Thank you for playing my game, I hope you enjoyed it :)")
            end_of_game = False
        else:
            restart
    return

play_game()