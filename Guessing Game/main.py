from game import GuessingGame

def main():
    game = GuessingGame()
    print(f"Guess a number between {game.min_value} and {game.max_value}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            result = game.make_guess(guess)
            print(result)
            if "Congratulations" in result:
                break
        except ValueError:
            print("Please enter a valid integer.")
    
if __name__ == "__main__":
    main()
