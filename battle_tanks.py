import random
import math


class BattleTanks:
    def __init__(self, name, modifier=0):
        self.velocity = 100
        self.position = random.randint(1, 1000) + modifier
        self.name = name

    def player_shoot(self, game, angle, target):
        shot_distance = self.get_shot_distance(angle)
        distance_to_target = abs(shot_distance - target.get_position())
        if target.is_target_hit(shot_distance, target.get_position()):
            game.game_over(target)
        else:
            self.print_miss_shot(angle, shot_distance, distance_to_target)

    def computer_shoot(self, game, angle, target):
        shot_distance = self.get_shot_distance(angle)
        if target.is_target_hit(shot_distance, target.get_position()):
            game.game_over(target)

    # S = v^2/g * sin(2a)
    # v = initial velocity
    # g = gravity
    # a = initial angle
    def get_shot_distance(self, angle):
        sin_param = math.radians(2 * angle)
        sin_value = math.sin(sin_param)
        velocity_squared = self.velocity ** 2
        numerator = velocity_squared * sin_value
        return numerator / 9.8

    def is_target_hit(self, shot_distance, target_position):
        if shot_distance - 40 <= target_position <= shot_distance + 40:
            return True
        return False

    def get_position(self):
        return self.position

    def print_miss_shot(self, angle, shot_distance, distance_to_target):
        too_far = """
               ________ 
          ====|        |
         _____|        |_____                    \\  |  /
        (                    )                    \\ | /
         \\__________________/                 _____\\|/_____
        """

        print(too_far)
        print(f"Your shot with an angle of {angle} impacted {shot_distance}m away and missed "
              f"by {distance_to_target}m")


class Game:
    def __init__(self):
        self.player_one = BattleTanks("Player 1")
        self.player_two = BattleTanks("Player 2", (self.player_one.get_position() + 50))
        self.game_running = True

    def play_game(self):
        self.print_title()
        print("Welcome to BattleTanks! The rules of the game are simple. Each player, you and the computer, will take "
              "turns lobbing rounds at each other.\nBased on the angle that you enter, the game will calculate "
              "the distance that the round will travel. If the round hits within 10 meters, then the game will end.")
        while self.is_game_running():
            player_shot_angle = self.get_player_shot_angle()
            self.player_one.player_shoot(new_game, player_shot_angle, self.player_two)
            computer_shot_angle = self.get_computer_shot_angle()
            self.player_two.computer_shoot(new_game, computer_shot_angle, self.player_one)

    def print_title(self):
        title_screen = """
                       ________                                          ________
                      |        |====            BATTLE              ====|        |
                 _____|        |_____                              _____|        |_____
                (                    )          TANKS             (                    )
                 \\__________________/                              \\__________________/
                """
        print(title_screen)

    def get_player_shot_angle(self):
        try:
            angle = int(input("Please enter the angle at which to shoot (1 - 89): "))
        except ValueError:
            print("That is not a valid value. Try again.")
            return self.get_player_shot_angle()
        if 1 <= angle <= 89:
            return angle
        else:
            print(f"Sorry, '{angle}' is not a valid value. Please try again.")
            return self.get_player_shot_angle()

    def get_computer_shot_angle(self):
        return random.randint(1, 89)

    def is_game_running(self):
        return self.game_running

    def game_over(self, destroyed_tank):
        print(f"Looks like {destroyed_tank.name} got destroyed. *Sad trombone*")
        self.game_running = False
        self.play_again()

    def play_again(self):
        player_choice = input("Play again? ")
        if player_choice.lower()[0] == 'y':
            self.reset_tank_positions()
            self.play_game()

    def reset_tank_positions(self):
        self.player_one = BattleTanks("Player 1")
        self.player_two = BattleTanks("Player 2", (self.player_one.get_position() + 50))
        self.game_running = True


if __name__ == '__main__':
    new_game = Game()
    new_game.play_game()
