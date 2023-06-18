#main_character
#Luan Nguyen
#06/11/2023


class Character:
     def __init__(self, name):
        self.name = name
        self.lives = 2
        self.score = 0

     def is_alive(self):
        return self.lives > 0


     def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            print("Monster is so hungry. You become his meal")
global me
me = Character("You")