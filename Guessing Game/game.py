import random

class GuessingGame:
    def __init__(self, min_value=1, max_value=100):
        """Initialize the game with a random target number."""
        self.min_value = min_value
        self.max_value = max_value
        self.target_number = random.randint(min_value, max_value)
        self.attempts = 0

    def make_guess(self, guess):
        """Check the guess and return feedback."""
        self.attempts += 1
        if guess < self.target_number:
            return "Too low! Try again."
        elif guess > self.target_number:
            return "Too high! Try again."
        else:
            return f"Congratulations! You guessed it in {self.attempts} attempts."
