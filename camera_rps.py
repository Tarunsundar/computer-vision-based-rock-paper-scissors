'''
This is a python program written to add computer vision intelligence,
into this Rock, paper and scissors game by replacing the use of inbuilt random function with 
visual inputs from images.
implemented a class for the computer vision schema

Method
______

count_down()
this function waits for the user's
visual input for some time to capture 
the player's hand movements

get_prediction()
this function returns the pre-built method for the rock, 
paper and scissors game.

'''
import random
import sys
import time
from xml.etree.ElementPath import prepare_predicate
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rps:
   
    def __init__(self):
        self.winner_Index = 0
        self.winner = ["Computer", "User", "Draw"]
        self.computer_wins = 0
        self.player_wins = 0
        self.rps_choice = ["rock", "paper", "scissors", "nothing"]
        self.prediction = [0]
        self.user_choice = "nothing"
        self.CPU_choice = "nothing"

    def get_computer_choice(self):
        CPU_choice = random.choice(self.rps_choice[0:3])
        return CPU_choice

    def get_user_choice(self):
        self.prediction = self.get_prediction()
        index = np.argmax(self.prediction[0])
        print("index =", index)
        if(index == 0):
            self.user_choice = "rock"
        if(index == 1):
            self.user_choice = "paper"
        if(index == 2):
            self.user_choice = "scissors"
        if(index == 3):
            self.user_choice = "nothing"
        print("Your chose ", self.user_choice)
        return self.user_choice

    def get_prediction(self):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)        
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        return prediction

    def countdown(self):
        stime = time.time()
        ctime = 0.0
        print("please decide your move within next 5 seconds")
        while(ctime <= stime + 2):
            ctime = time.time()
            self.get_prediction()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print("Time's up, show your move now")
        print("Prediction will be as following, 1st Rock, 2nd Paper. 3rd Scissors and 4th nothing \n")
        print("prediction is ", self.prediction)
        return self.get_prediction()

    def get_result(self):
        print("\n CPU chose ", self.CPU_choice)
        if (self.CPU_choice =="rock" and self.user_choice == "scissors") or (self.CPU_choice == "scissors" and self.user_choice == "paper") or (self.CPU_choice == "paper" and self.user_choice == "rock"): 
            print("Computer wins, better luck next time\n")
            computer_wins += 1
            self.winner_Index = 0
        elif (self.CPU_choice == "rock" and self.user_choice == "paper") or (self.CPU_choice == "scissors" and self.user_choice == "rock") or (self.CPU_choice == "paper" and self.user_choice == "scissors"):
            print("wooh You won, Congrats!!\n")
            player_wins += 1
            self.winner_Index = 1
        elif (self.user_choice == "nothing"):
            print("sorry, we couldn't recogonize your move. show your move properly")
            self.winner_Index = 2
        else:
            print("Oops that was a draw \n")
            self.winner_Index = 2
        print("player wins =", self.player_wins)
        print("\ncomputer wins =", self.computer_wins)
        time.sleep(5)
        print("\n")
        return self.winner_Index

    def play(self):
        while(self.player_wins < 3 and self.computer_wins < 3):
            self.CPU_choice = self.get_computer_choice()
            self.countdown()
            self.user_choice = self.get_user_choice()
            if(self.user_choice == "nothing"):
                self.user_choice = self.get_user_choice()
            self.get_result()
        print("Tournament won by ", self.winner[self.winner_Index])
        print("\n")

if __name__ == '__main__':
    game = Rps()
    game.play()
    game.winner