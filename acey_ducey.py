import random


class Player:
    def __init__(self):
        self.money = 100

    def set_money(self, amount):
        self.money = amount

    def get_money(self):
        return self.money


class Game:
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def play_game(self, player):
        while player.get_money() > 0:
            first_card, second_card, third_card = self.get_cards()
            if self.cards.index(first_card) > self.cards.index(second_card):
                first_card, second_card = second_card, first_card
            print(f"\n{first_card}\n{second_card}")
            amount_bet = self.bet_money(player)
            if amount_bet == 0:
                continue
            print(f"{third_card}")
            if self.cards.index(first_card) < self.cards.index(third_card) < self.cards.index(second_card):
                print("You win!")
                player.set_money(player.get_money() + amount_bet)
            else:
                print("Sorry, you lose")
                player.set_money(player.get_money() - amount_bet)
        play_again_choice = input("You ran out of money! Play again? ")
        if play_again_choice.lower()[0] == 'y':
            player.set_money(100)
            self.play_game(player)

    def get_cards(self):
        cards_to_choose_from = self.cards.copy()
        first_card = cards_to_choose_from[random.randint(0, 12)]
        cards_to_choose_from.remove(first_card)
        second_card = cards_to_choose_from[random.randint(0, 11)]
        cards_to_choose_from.remove(second_card)
        third_card = cards_to_choose_from[random.randint(0, 10)]
        return [first_card, second_card, third_card]

    def print_instructions(self):
        print("The dealer (computer) will deal 2 cards. You will then choose to bet on whether the next card will\n"
              "be in between the 2 cards. You start with $100 to bet with. If you don't want to play the current\n"
              "hand, you can enter '0' to choose not to play.")

    def bet_money(self, player):
        try:
            amount = int((input(f"Enter amount to bet (0 - {player.get_money()}): ")))
        except ValueError:
            print("That's not a valid value. Try again.")
            return self.bet_money(player)
        if player.get_money() - amount < 0:
            print(f"{amount} is an invalid amount. Try again.")
            return self.bet_money(player)
        return amount


if __name__ == '__main__':
    player_one = Player()
    new_game = Game()
    instructions_choice = input("Welcome to Acey Ducey. Do you want to read the instructions? ")
    if instructions_choice.lower()[0] == 'y':
        new_game.print_instructions()
    new_game.play_game(player_one)
