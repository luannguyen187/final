# main game
# Luan Nguyen
# 06/11/2023
import main_character
# this is file will controll the whole game

# introduce the game
# Game name is Monster Kitchen
# Player find themself in a terrible situation after being kidnapped by a ravenous monster with an insatiable appetite
# The only chance to surviral is become personal chef
# this game include 4 task: choose meal,
# find ingredient. In this section, you play quiz game with answer 5 question about history or geography to find the ingredient in garden
# cooking. In this section, you play math game to have time for cooking.
# Player will have 2 lives
# Failure to do so will result in becoming the monster's meal.
from main_character import Character
from section1 import Meal
from section2 import Quizgame
from section3 import Mathquiz


# from section2 import quizgame

def main():
    print("Welcome to Monster's Kitchen!!!\nYou become a personal chef for a ravenous monster with an insatiable appetite after kidnapping.\nTo survial, you have to choose the meal, find ingredient, how to cook for Monster's dinner.\nRemember, one false move, and you'll become the monster's next meal!")
    print("Let's begin to Death Kitchen!")


# input the user name

    # import the main character
    # player = main_character(user_name)
    # player.print.status()
    user_name = input("Enter your name: ")
    main_character = Character(user_name)

    print("Hello chef", user_name)
    print("Let's start")

    section1 = Meal(main_character)
    meal, category = section1.start()

    section2 = Quizgame(main_character)
    section2.start(meal, category)

    section3 = Mathquiz(main_character)
    section3.start()



if __name__ == "__main__":
    main()
