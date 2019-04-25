import random


class Characters:
    def __init__(self):
        self.hair = ['red', 'blonde', 'brown', 'white', 'black']
        self.eyes = ['green', 'blue', 'brown']
        self.facial_hair = ['beard', 'mustache', 'full', 'clean-shaven']
        self.gender = ['male', 'female']
        self.characters = ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric',
                           'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Phillip', 'Richard',
                           'Robert', 'Sam', 'Susan', 'Tom']
        self.character_attributes = {
            'Alex': {
                'hair': 'black',
                'eyes': 'brown',
                'facial hair': 'mustache',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Alfred': {
                'hair': 'red',
                'eyes': 'green',
                'facial hair': 'mustache',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Anita': {
                'hair': 'blonde',
                'eyes': 'blue',
                'facial hair': 'clean-shaven',
                'gender': 'female',
                'glasses': False,
                'hat': False,
            },
            'Anne': {
                'hair': 'black',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'female',
                'glasses': False,
                'hat': False,
            },
            'Bernard': {
                'hair': 'brown',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': True,
            },
            'Bill': {
                'hair': 'red',
                'eyes': 'brown',
                'facial hair': 'beard',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Charles': {
                'hair': 'blonde',
                'eyes': 'brown',
                'facial hair': 'mustache',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Claire': {
                'hair': 'red',
                'eyes': 'blue',
                'facial hair': 'clean-shaven',
                'gender': 'female',
                'glasses': True,
                'hat': True,
            },
            'David': {
                'hair': 'blonde',
                'eyes': 'brown',
                'facial hair': 'beard',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Eric': {
                'hair': 'blonde',
                'eyes': 'green',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': True,
            },
            'Frans': {
                'hair': 'red',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'George': {
                'hair': 'white',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': True,
            },
            'Herman': {
                'hair': 'red',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Joe': {
                'hair': 'blonde',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': True,
                'hat': False,
            },
            'Maria': {
                'hair': 'brown',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'female',
                'glasses': False,
                'hat': True,
            },
            'Max': {
                'hair': 'black',
                'eyes': 'brown',
                'facial hair': 'mustache',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Paul': {
                'hair': 'white',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': True,
                'hat': False,
            },
            'Peter': {
                'hair': 'white',
                'eyes': 'blue',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Phillip': {
                'hair': 'black',
                'eyes': 'brown',
                'facial hair': 'beard',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Richard': {
                'hair': 'brown',
                'eyes': 'brown',
                'facial hair': 'full',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Robert': {
                'hair': 'brown',
                'eyes': 'blue',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': False,
                'hat': False,
            },
            'Sam': {
                'hair': 'white',
                'eyes': 'brown',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': True,
                'hat': False,
            },
            'Susan': {
                'hair': 'white',
                'eyes': 'green',
                'facial hair': 'clean-shaven',
                'gender': 'female',
                'glasses': False,
                'hat': False,
            },
            'Tom': {
                'hair': 'black',
                'eyes': 'blue',
                'facial hair': 'clean-shaven',
                'gender': 'male',
                'glasses': True,
                'hat': False,
            },
        }

    def get_hair_colors(self):
        return self.hair

    def get_facial_hair_styles(self):
        return self.facial_hair

    def get_eye_colors(self):
        return self.eyes

    def get_characters(self):
        return self.characters

    def get_character_attributes(self):
        return self.character_attributes

    def get_genders(self):
        return self.gender


class Game:
    def __init__(self):
        self.character_group = Characters()
        self.game_running = True
        self.character_pool = self.character_group.get_characters()

    def get_character_pool(self):
        return self.character_pool

    def set_character_pool(self, new_pool):
        self.character_pool = new_pool

    def game_won(self):
        self.game_running = False

    def is_game_running(self):
        return self.game_running

    def play_game(self):
        character_to_guess = self.character_group.get_characters()[random.randint(0, 23)]
        while self.is_game_running():
            self.get_number_of_attributes_left()
            self.guess_or_eliminate_choices(character_to_guess)

    def guess_or_eliminate_choices(self, character_to_guess):
        player_choice = input("Would you like to [g]uess who it is or [e]liminate some more choices?")
        if player_choice.lower()[0] == 'e':
            self.get_input(character_to_guess)
        elif player_choice.lower()[0] == 'g':
            print(f"The remaining characters are {self.get_character_pool()}")
            self.guess_who(character_to_guess)
        else:
            print(f"Sorry, '{player_choice}' is not a valid option. Try again.")
            self.guess_or_eliminate_choices(character_to_guess)

    def get_number_of_attributes_left(self):
        hair = {color: 0 for color in self.character_group.get_hair_colors()}
        eye = {color: 0 for color in self.character_group.get_eye_colors()}
        facial_hair = {hair: 0 for hair in self.character_group.get_facial_hair_styles()}
        gender = {sex: 0 for sex in self.character_group.get_genders()}
        glasses = 0
        hat = 0
        for name in self.get_character_pool():
            for key, value in self.character_group.get_character_attributes()[name].items():
                if key == 'hair':
                    hair[value] += 1
                elif key == 'eyes':
                    eye[value] += 1
                elif key == 'facial hair':
                    facial_hair[value] += 1
                elif key == 'gender':
                    gender[value] += 1
                elif key == 'glasses' and value is True:
                    glasses += 1
                elif key == 'hat' and value is True:
                    hat += 1

        print(f"There are currently {hair['red']} people with red hair, {hair['black']} people with black hair, "
              f"{hair['brown']} people with brown hair, {hair['blonde']} people with blonde hair, and {hair['white']} "
              f"people with white hair.")
        print(f"There are currently {eye['green']} people with green eyes, {eye['blue']} people with blue eyes, and "
              f"{eye['brown']} people with brown eyes.")
        print(f"There are currently {facial_hair['beard']} people with a beard, {facial_hair['mustache']} people with "
              f"a mustache, {facial_hair['full']} people with a beard and mustache, and {facial_hair['clean-shaven']} "
              f"people that are clean-shaven.")
        print(f"There are {gender['male']} males and {gender['female']} females.")
        print(f"There are {glasses} people with glasses and {hat} people with hats.")

    def get_input(self, character_to_guess):
        attribute_choice = input("What would you like ask about? (hair, eyes, facial hair, sex, glasses, or hats) ")
        self.attribute_input_check(attribute_choice.lower()[:3], character_to_guess)

    def attribute_input_check(self, attribute, character_to_guess):
        if attribute == 'hat':
            self.does_character_have_a_hat(character_to_guess)
        elif attribute == 'gla':
            self.does_character_have_glasses(character_to_guess)
        elif attribute == 'hai':
            hair_choice = input("Ask about red hair, black hair, brown hair, blonde hair, or white hair?")
            self.hair_input_check(character_to_guess, hair_choice.lower()[:3])
        elif attribute == 'eye':
            eye_choice = input("Ask about green eyes, blue eyes, or brown eyes?")
            self.eye_input_check(character_to_guess, eye_choice.lower()[:2])
        elif attribute == 'fac':
            facial_hair_choice = input("Ask about beard, mustache, both, or clean-shaven?")
            self.facial_hair_input_check(character_to_guess, facial_hair_choice.lower()[:2])
        elif attribute == 'sex':
            sex_choice = input("Ask if they are male or female?")
            self.sex_input_choice(character_to_guess, sex_choice.lower()[0])
        else:
            print(f"Sorry, {attribute} is not a valid choice. Try again.")
            return self.get_input(character_to_guess)

    def does_character_have_a_hat(self, character_to_guess):
        print("Does the person have a hat?")
        if self.character_group.get_character_attributes()[character_to_guess]['hat']:
            print("The character does have a hat!")
            self.remove_characters_with_non_matching_attribute('hat', True)
        else:
            print("The character does not have a hat!")
            self.remove_characters_with_non_matching_attribute('hat', False)

    def does_character_have_glasses(self, character_to_guess):
        print("Does the person have glasses?")
        if self.character_group.get_character_attributes()[character_to_guess]['glasses']:
            print("The character does have glasses!")
            self.remove_characters_with_non_matching_attribute('glasses', True)
        else:
            print("The character does not have glasses!")
            self.remove_characters_with_non_matching_attribute('glasses', False)

    def hair_input_check(self, character_to_guess, hair_color):
        if hair_color == 'red':
            print("Does the person have red hair?")
            if self.do_they_have_this_color_hair(character_to_guess, 'red'):
                print("The character does have red hair!")
                self.remove_characters_with_non_matching_attribute('hair', 'red')
            else:
                print("The character does not have red hair!")
                self.remove_characters_with_matching_attribute('hair', 'red')
        elif hair_color == 'bla':
            print("Does the person have black hair?")
            if self.do_they_have_this_color_hair(character_to_guess, 'black'):
                print("The character does have black hair!")
                self.remove_characters_with_non_matching_attribute('hair', 'black')
            else:
                print("The character does not have black hair!")
                self.remove_characters_with_matching_attribute('hair', 'black')
        elif hair_color == 'bro':
            print("Does the person have brown hair?")
            if self.do_they_have_this_color_hair(character_to_guess, 'brown'):
                print("The character does have brown hair!")
                self.remove_characters_with_non_matching_attribute('hair', 'brown')
            else:
                print("The character does not have brown hair!")
                self.remove_characters_with_matching_attribute('hair', 'brown')
        elif hair_color == 'blo':
            print("Does the person have blonde hair?")
            if self.do_they_have_this_color_hair(character_to_guess, 'blonde'):
                print("The character does have blonde hair!")
                self.remove_characters_with_non_matching_attribute('hair', 'blonde')
            else:
                print("The character does not have blonde hair!")
                self.remove_characters_with_matching_attribute('hair', 'blonde')
        elif hair_color == 'whi':
            print("Does the person have white hair?")
            if self.do_they_have_this_color_hair(character_to_guess, 'white'):
                print("The character does have white hair!")
                self.remove_characters_with_non_matching_attribute('hair', 'white')
            else:
                print("The character does not have white hair!")
                self.remove_characters_with_matching_attribute('hair', 'white')
        else:
            print(f"Sorry, {hair_color} is not a valid choice, try again.")
            self.attribute_input_check('hai', character_to_guess)

    def do_they_have_this_color_hair(self, character_to_guess, hair_color):
        if self.character_group.get_character_attributes()[character_to_guess]['hair'] == hair_color:
            return True
        return False

    def eye_input_check(self, character_to_guess, eye_color):
        if eye_color == 'gr':
            print("Does the person have green eyes?")
            if self.do_they_have_this_eye_color(character_to_guess, 'green'):
                print("The character does have green eyes!")
                self.remove_characters_with_non_matching_attribute('eyes', 'green')
            else:
                print("The character does not have green eyes!")
                self.remove_characters_with_matching_attribute('eyes', 'green')
        elif eye_color == 'bl':
            print("Does the person have blue eyes?")
            if self.do_they_have_this_eye_color(character_to_guess, 'blue'):
                print("The character does have blue eyes!")
                self.remove_characters_with_non_matching_attribute('eyes', 'blue')
            else:
                print("The character does not have blue eyes!")
                self.remove_characters_with_matching_attribute('eyes', 'blue')
        elif eye_color == 'br':
            print("Does the person have brown eyes?")
            if self.do_they_have_this_eye_color(character_to_guess, 'brown'):
                print("The character does have brown eyes!")
                self.remove_characters_with_non_matching_attribute('eyes', 'brown')
            else:
                print("The character does not have brown eyes!")
                self.remove_characters_with_matching_attribute('eyes', 'brown')
        else:
            print(f"Sorry, {eye_color} is not a valid choice, try again.")
            self.attribute_input_check('eye', character_to_guess)

    def do_they_have_this_eye_color(self, character_to_guess, eye_color):
        if self.character_group.get_character_attributes()[character_to_guess]['eyes'] == eye_color:
            return True
        return False

    def facial_hair_input_check(self, character_to_guess, facial_hair):
        if facial_hair == "be":
            print("Does the person have a beard?")
            if self.do_they_have_facial_hair(character_to_guess, 'beard'):
                print("The character does have a beard!")
                self.remove_characters_with_non_matching_attribute('facial hair', 'beard')
            else:
                print("The character does not have a beard!")
                self.remove_characters_with_matching_attribute('facial hair', 'beard')
        elif facial_hair == "mu":
            print("Does the person have a mustache?")
            if self.do_they_have_facial_hair(character_to_guess, 'mustache'):
                print("The character does have a mustache!")
                self.remove_characters_with_non_matching_attribute('facial hair', 'mustache')
            else:
                print("The character does not have a mustache!")
                self.remove_characters_with_matching_attribute('facial hair', 'mustache')
        elif facial_hair == "bo":
            print("Does the person have both?")
            if self.do_they_have_facial_hair(character_to_guess, 'full'):
                print("The character does have a beard and a mustache!")
                self.remove_characters_with_non_matching_attribute('facial hair', 'full')
            else:
                print("The character does not have a beard and a mustache!")
                self.remove_characters_with_matching_attribute('facial hair', 'full')
        elif facial_hair == "cl":
            print("Is the person clean-shaven?")
            if self.do_they_have_facial_hair(character_to_guess, 'clean-shaven'):
                print("The character is clean-shaven!")
                self.remove_characters_with_non_matching_attribute('facial hair', 'clean_shaven')
            else:
                print("The character is not clean-shaven!")
                self.remove_characters_with_matching_attribute('facial hair', 'clean_shaven')
        else:
            print(f"Sorry, {facial_hair} is not a valid choice, try again.")
            self.attribute_input_check('fac', character_to_guess)

    def do_they_have_facial_hair(self, character_to_guess, facial_hair):
        if self.character_group.get_character_attributes()[character_to_guess]['facial hair'] == facial_hair:
            return True
        return False

    def sex_input_choice(self, character_to_guess, sex):
        if sex == "m":
            print("Is the person a male?")
            if self.are_they_this_gender(character_to_guess, 'male'):
                print("The character is a male!")
                self.remove_characters_with_non_matching_attribute('gender', 'male')
            else:
                print("The character is not a male!")
                self.remove_characters_with_matching_attribute('gender', 'male')
        elif sex == "f":
            print("Is the person a female?")
            if self.are_they_this_gender(character_to_guess, 'female'):
                print("The character is a female!")
                self.remove_characters_with_non_matching_attribute('gender', 'female')
            else:
                print("The character is not a female!")
                self.remove_characters_with_matching_attribute('gender', 'female')
        else:
            print(f"Sorry, {sex} is not a valid choice, try again.")
            self.attribute_input_check('sex', character_to_guess)

    def are_they_this_gender(self, character_to_guess, sex):
        if self.character_group.get_character_attributes()[character_to_guess]['gender'] == sex:
            return True
        return False

    def remove_characters_with_non_matching_attribute(self, attribute, attribute_description):
        new_character_pool = []
        for name in self.get_character_pool():
            if self.character_group.get_character_attributes()[name][attribute] == attribute_description:
                new_character_pool.append(name)
        self.set_character_pool(new_character_pool)

    def remove_characters_with_matching_attribute(self, attribute, attribute_description):
        new_character_pool = []
        for name in self.get_character_pool():
            if self.character_group.get_character_attributes()[name][attribute] != attribute_description:
                new_character_pool.append(name)
        self.set_character_pool(new_character_pool)

    def guess_who(self, character_to_guess):
        player_guess = input("Who is it? ")
        if player_guess.lower() == character_to_guess.lower():
            print(f"Congratulations! It was {character_to_guess}")
            self.game_won()
            self.play_again()
        else:
            print(f"Sorry, it's not {player_guess}")

    def play_again(self):
        player_choice = input("Play again? ")
        if player_choice.lower()[0] == 'y':
            self.set_character_pool(self.character_group.get_characters())
            self.game_running = True
            self.play_game()


if __name__ == '__main__':
    new_game = Game()
    new_game.play_game()
