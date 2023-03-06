import random

# List of valid colors and number of tries allowed
colors = ["R", "G", "B", "Y", "W", "O"]
tries = 10

# Length of code to be guessed
code_length = 4

# Function to generate a random code of length 'code_length' using the colors in 'colors'
def generate_code():
    code = []

    # Generate each color in the code randomly
    for _ in range(code_length):
        color = random.choice(colors)
        code.append(color)

    # Return the generated code
    return code 

# Function to get a user's guess for the code
def guess_code():
    while True:
        # Get input from the user, convert to uppercase, and split into a list of colors
        guess = input("Guess: ").upper().split(" ")

        # If the number of colors in the guess is not equal to code_length, ask user to guess again
        if len(guess) != code_length:
            print(f"You must guess {code_length} colors.")
            continue

        # If any of the colors in the guess are not valid, ask user to guess again
        for color in guess:
            if color not in colors:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            # If guess is valid, return the guess
            break
    return guess 

# Function to check the user's guess against the real code and return the number of correct and incorrect positions
def check_code(guess, real_code):
    #Create a dictionary to count the number of each color in the code.
    color_counts = {}
    #Initialize variables to count the number of correct and incorrect colors.
    correct_pos = 0
    incorrect_pos = 0

    #Loop through each color in the real code to count the number of each color.
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    #Loop through each color in the guess to check for correct positions.
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            #If a color is in the correct position, subtract one from its count in the color_counts dictionary.
            color_counts[guess_color] -= 1

    #Loop through each color in the guess to check for incorrect positions.
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            #If a color is in the incorrect position, subtract one from its count in the color_counts dictionary.
            color_counts[guess_color] -= 1
            
    #Return the number of correct and incorrect positions.
    return correct_pos, incorrect_pos

#Function to tie the game together.
def game():
    
    #Print the welcome message and the valid colors.
    print(f"Welcome to mastermind, you have {tries} to guess the code...")
    print("The valid colors are ", *colors)
    
    # Generate the code to be guessed
    code = generate_code()
    
    # Loop through the game for the number of tries allowed
    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        # Check if the guess is correct, and end the game if it is
        if correct_pos == code_length:
            print(f"You guessed the code in {attempts} tries!")
            break     
        # Print the number of correct and incorrect positions in the guess
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        # Print the code if the user runs out of tries
        print("You ran out of tries, the code was: ", *code)

# Run the game if this is the main file being executed
if __name__ == "__main__":
    game()




