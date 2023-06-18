#section_1_choose_meal
#Luan Nguyen
#06/11/2023

#in this section, the place will choose the meal, Player want to prepare
#option 1. Pizza
#option 2. Ramen
import main_character

class Meal:
    def __init__(self, main_character):

        self.main_character = main_character

    def start(self):

        print("Meal Selection")
        print("Choose the meal to cook for monster:")
        print("1.Pizza")
        print("2.Burger")

        meal = input("Monster hungry, enter your choose 1-2: ")

        if meal == "1":
            print("You chose to cook Pizza for monster.")
            self.main_character.meal = "Pizza"
            self.main_character.category = "History"
        elif meal == "2":
            print("You chose to cook Burger for monster.")
            self.main_character.meal = "Burger"
            self.main_character.category = "Geography"
        else:
            print("Opp, this is not meal Monster want. Please try again")
        return self.main_character.meal, self.main_character.category
game = Meal()
game.start()







