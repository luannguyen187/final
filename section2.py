# section2
# Luan Nguyen
# 06/11/2023
import main_character
#import meal

# Section 2 is quiz game
# find ingredient
# In this section, you play quiz game with answer 5 question about history or geography to find the ingredient in garden
#from section1 import Meal


class Quizgame:
    #def __init__(self, category):

        #self.lives = 2

    def start(self, meal, category):

        #print(main_character.me.name)
        print(" Section 2")
        print("Now you have to answer 5 True/False to get a hint to find the ingredient to cook for Monster")

        #questions = {
            #"History":
        hisquestions = [
                "Question 1: Christopher Columbus discovered America.",  # true
                "Question 2: George Washington was the first president of the United States.",  # true
                "Question 3: Andrew Jackson appears on the United States ten-dollar bill.",  # false 20
                "Question 4: Abraham Lincoln was a member of the Democrat party",  # false
                "Question 5: Buzz Aldrin was is the second man in the moon",  # true
            ]

            #"Geograph":
        geoquestions = [
                "Question 1:The Amazon Rainforest is located in Africa",  # false(south africa)
                "Question 2: The capital of Canada is Toronto.",  # false(ottawa)
                "Question 3: The Nile River is the longest river in the world.",  # true
                "Question 4: New Hampshire is the tate to border exactly one other American state",  # false (maine)
                "Question 5: Texas is the largest state in the US"  # false Alaska
            ]
        #}

        answers = {"History": [False, False, True, False, False],
                   "Geography": [True, True, False, False, True]}
        hisanswers = ["true", "true", "false", "false", "true"]
        geoanswers = ["true", "false", "true", "false", "false"]



        correct_answers = 0
        #for category in ["History", "Geography"]:
        if category == "History":
            answerlist = hisanswers
            questionlist = hisquestions
        else:
            answerlist = geoanswers
            questionlist = geoquestions
        for i in range(5):
            print(questionlist[i])
            answers = input("Enter your answer (True/False):").lower()
            if (answers == answerlist[i]):
                correct_answers += 1
                print("Correct")
            else:
                main_character.me.lives -= 1
                print("Wrong!")
        if main_character.me.lives == 0:
            print("Oops! You don't have enough lives. You will become the monster's meal.")
        if correct_answers >= 3:
            print("Congratulations! You got the hint to find the ingredient in garden.")
        else:
            main_character.me.lose_life()
            print("Incorrect answers. Be careful, you dont have enough time. You will be Monster's meal")


game = Quizgame()
game.start("Pizza", "History")
game.start("Burger", "Geography")
