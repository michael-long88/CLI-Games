import random


class Game:
    def __init__(self):
        self.game_running = True

    def play_game(self):
        number_to_guess = random.randint(1, 10)
        guesses = 0
        while self.is_game_running() and guesses < 4:
            print(f"Guess #{guesses + 1}")
            player_guess = self.guess_number()
            if player_guess == number_to_guess:
                self.game_running = False
                self.win()
            else:
                self.check_guess(player_guess, number_to_guess)
            guesses += 1
        if self.is_game_running():
            self.game_over()

    def is_game_running(self):
        return self.game_running

    def guess_number(self):
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Sorry, that isn't a valid value. Try again")
            return self.guess_number()
        if not 1 <= guess <= 10:
            print(f"Sorry, {guess} is not a valid choice. Please try again.")
            return self.guess_number()
        return guess

    def check_guess(self, guess, number):
        if guess > number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    def win(self):
        print("Congratulations! The device has been defused!")
        self.play_again()

    def game_over(self):
        print(" \\ **** /")
        print("-- BOOM --")
        print(" / **** \\")
        self.play_again()

    def play_again(self):
        choice = input("Play again? ")
        if choice.lower()[0] == 'y':
            self.game_running = True
            self.play_game()


if __name__ == '__main__':
    new_game = Game()
    print(
        "Welcome to Countdown. You have 4 attempts to guess a number between 1 and 10 in order to disarm a "
        "device.\nIf you don't manage to guess the number, the device will explode. After each guess, the "
        "computer will tell\nyou if your guess is too high or too low.")
    new_game.play_game()
