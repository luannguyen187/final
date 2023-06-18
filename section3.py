#section3
#Luan Nguyen
#06/11/2023



#Section3  is math quiz
import random
import main_character
class Mathquiz:
    def __init__(self):
        self.main_character = main_character.me
        self.lives = 2
        self.score = 0
        print("Section 3: Math Quiz")
        print("You need time to cook the food for Monster")

    def start(self):
        while self.lives > 0:
            num1 = random.randint(10, 20)
            num2 = random.randint(1, 10)

            operator = random.choice(['+', '-', '*'])
            if operator == "+":
                answer = num1 + num2
            elif operator == "-":
                answer = num1 - num2
            else:
                answer = num1 * num2

            question = f"{num1} {operator} {num2}: "
            player_answer = input(question)


            if int(player_answer) == answer:
                print("Correct")
                self.score += 1

            else:
                self.lives -= 1
                print("Wrong")

            if self.lives == 0:
                 print("opps!!!You loose the lives. You become Monster's meal ")
            #print("GAME OVER")

            if self.score == 5:
                print("Congratulation! Monster love your food. You're free")

                print("Game Over")
                break

