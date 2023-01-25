# Import necessary libraries
import random

# The list of words
WORDS_LIST = ["acasa", "masa", "bloc", "apartament", "camera", "geam", "masina", "autocar", "tren", "vapor", "tanc", "troleibuz", "om", "caine", "crocodil", "vaca", " magar",
              "bou", "capra", "peste", "salariu", "bursa", "camin", "shaorma", "bere", "seminte", "motor", "tractor", "avion", "politist", "vames", "dodon"]

# Randomly select a word from the list        
selected_word = random.choice(WORDS_LIST)

# Get the length of the selected word
len_word = len(selected_word)

# Initialize the list of guessed letters 
guessed_letters = []

# Number of attempts allowed
attempts = 8

# Initialize the flag for if the user is right
is_user_right = True

# While loop for the game
while is_user_right:
    # Initialize the output string
    out = ""

    # Check if each letter in the selected word has been guessed   
    for user_letter in selected_word:
        if user_letter in guessed_letters:
            out += user_letter
        else:
            out = out + "_ "

    # Check if the user has guessed the word   
    if out == selected_word:
        print("You guessed! ", selected_word)
        break
    
    # Print the current state of the word
    print(f"Guess the word: {out}")
    # Get the user's next guess
    user_letter = input("Please enter the letter you want: ")
    
    # Check if the user has already guessed the letter
    if user_letter in guessed_letters:
        print("ALready guessed", user_letter)

    # Check if the user's guess is in the word   
    elif user_letter in selected_word:
        print("Corect letter")
        guessed_letters.append(user_letter)

    # If the user's guess is not in the word   
    else:
        attempts -= 1
        print("Wrong letter!")
        print(f"Attention, this letter does not exist in the given word, you have {attempts} attempts left!")

        # Print the current state of the hangman
        if attempts == 7:
            print("________      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
                                             
        elif attempts == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
                                              
        elif attempts == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
                                               
        elif attempts == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
                                               
        elif attempts == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
                                               
        elif attempts == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
                                               
        elif attempts == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
               
        elif attempts == 0:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("You DIED!")
            print(f"The word was: {selected_word}")
            break
      
    print()