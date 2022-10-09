'''
This is a manual(non visual) game developed to play rock, paper and scissors.
This has been developed in python, Hope you enjoy this..
'''

import random
from typing_extensions import Self
import sys

class Rps:
    '''
    implemented a class for the rock, paper and scissors game which would contain the following;
    
    Parameters & Attributes
    _______________________

    rps_choice : list
    List of choices in this game.

    winner: list
    List of possible winners of this game

    CPU_choice: list
    CPU_choice from list of possible choices

    user_choice: list
    user_choice from list of possible choices

    Methods:
    --------
    get_computer_choice()
      This method would get a random choice among rps to compete with user
    get_user_choice()
      Thsi method would get a choice from the user to play rps.

    '''  
    rps_choice = []
    winner = ["Computer", "User", "Draw"]
    CPU_choice = rps_choice
    user_choice = rps_choice

    def get_computer_choice(self):
        CPU_choice = random.choice(self.rps_choice)
        return CPU_choice

    def get_user_choice(self):
        self.user_choice = input('Enter rock, paper or scissors ')
        if(self.user_choice not in self.rps_choice):
            print(" that was an Invalid input, please enter either rock, paper or scissors\n")
            sys.exit()
        else:
            print("Your chose ", self.user_choice)
            return self.user_choice

    def get_result(self):
        print("\n CPU chose ", self.CPU_choice)
        if (self.CPU_choice =="rock" and self.user_choice == "scissors") or (self.CPU_choice == "scissors" and self.user_choice == "paper") or (self.CPU_choice == "paper" and self.user_choice == "rock"): 
            print("Computer wins, better luck next time\n")
            return self.winner[0]
        elif (self.CPU_choice == "rock" and self.user_choice == "paper") or (self.CPU_choice == "scissors" and self.user_choice == "rock") or (self.CPU_choice == "paper" and self.user_choice == "scissors"):
            print("wooh You won, Congrats!!\n")
            return self.winner[1]
        else:
            print("Oops that was a draw \n")
            return self.winner[2]
    
def play(self):
    self.CPU_choice = self.get_computer_choice()
    self.user_choice = self.get_user_choice()
    self.get_result()

if __name__ == '__main__':
    game = Rps()
    game.rps_choice = ["rock", "paper", "scissors"]
    play(game)


       

