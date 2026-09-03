import random
import json
def pick_word():
    words = [
    "apple", "beach", "brain", "bread", "chair", "cloud", "crane", "dance",
    "dream", "earth", "flame", "fruit", "ghost", "grape", "green", "heart",
    "house", "juice", "lemon", "light", "money", "music", "night", "ocean",
    "paint", "party", "phone", "piano", "pizza", "plant", "power", "queen",
    "radio", "river", "robot", "scale", "shark", "shirt", "smile", "snake",
    "space", "spice", "storm", "table", "tiger", "train", "water", "whale",
    "world", "zebra"
    ]
    choosen_word = random.choice(words)
    return choosen_word



def main():
    name = input("Welcome to Wordle! Press Enter your name to start the game: ")
    try:
        with open("guesses.json", "r") as f:
            all_scores = json.load(f)
            if not isinstance(all_scores, list):
                all_scores = []
    except (FileNotFoundError, json.JSONDecodeError):
        all_scores = []
    guesses = 0
    word = pick_word()
    positions = ["first", "second", "third", "fourth", "fifth"]
    while True:
        user_ans = input("Guess the word: ").lower().strip()
        if len(user_ans) != 5:
            print("Please enter a 5-letter word.")
            continue
        guesses +=1
        if user_ans == word:
            print("Congratulations! You guessed the word correctly.")
            break
            
        for i in range(5):
            if user_ans[i] == word[i]:
                print(f"The letter '{user_ans[i]}' is in the position ({positions[i]} letter).")
            elif user_ans[i] in word:
                print(f"The letter '{user_ans[i]}' is in the word but in the wrong position.")
            else:
                print(f"The letter '{user_ans[i]}' is not in the word.")
        
    all_scores.append({"Player": name, "guesses": guesses })
    print (f"You guessed the word in {guesses} attempts.")
    with open("guesses.json", "w") as file:
        json.dump(all_scores, file, indent=4)



              

main()