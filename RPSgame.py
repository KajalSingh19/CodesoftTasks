import random
from tkinter import *
import tkinter as tk

#Dictionary and variables
schema = { "rock":{"rock":1 , "paper":0 , "scissors":2},
          "paper":{"rock":2 , "paper":1 , "scissors":0},
           "scissors":{"rock":0 , "paper":2 , "scissors":1} }
comp_score = 0
player_score = 0
max_score = 6
#functions
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["rock" , "paper", "scissors"]
    random_number = random.randint(0,2)
    computer_choice = outcomes[random_number]
    result    = schema[user_choice][computer_choice]

    player_choice_label.config(fg="red" , text = "Player Choice : "+str(user_choice))
    computer_choice_label.config(fg="green" , text = "Computer Choice : "+str(computer_choice))

    if result == 2:
        player_score = player_score + 1
        player_score_label.config( text = "Player : "+str(player_score))
        outcome_label.config(fg="blue", text="Outcome : Player won")
    elif result == 1:
        player_score = player_score + 0
        comp_score = comp_score + 0

        player_score_label.config( text = "Player : "+str(player_score))
        computer_score_label.config( text = "Computer : "+str(comp_score))
        outcome_label.config(fg="blue", text="Outcome : Draw")
    elif result == 0:
        comp_score = comp_score + 1
        computer_score_label.config( text = "Computer : "+str(comp_score))
        outcome_label.config(fg="blue", text="Outcome : Computer won ")

    if player_score >= max_score or comp_score >= max_score:
        end_game()


def reset_game():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text= f"Player: {player_score}")

    outcome_label.config(text="")
    
def end_game():
    if player_score > comp_score:
        outcome_label.config(text="Congratulations! You win the game!")
    elif comp_score > player_score:
        outcome_label.config(text="Computer wins the game.\nBetter luck next time!")
    else:
      outcome_label.config(text="It's a tie game!")
    
    reset_game
    #play_again_button.config(state=tk.NORMAL)
    #rock_button.config(state=tk.DISABLED)
    #paper_button.config(state=tk.DISABLED)
    #scissor_button.config(state=tk.DISABLED)
   
   #main screen
master = Tk()
master.title("RockPapperScissors")

master.resizable(0,0)
#label
Label(master , text = "Rock, Paper, Scissors" , font = ('arial 14 bold')).grid( row= 0, sticky= N, padx=200, pady= 10)
Label(master , text = "Total Rounds : 6" , font = ('arial 10 ')).grid( row= 1, sticky= N)

player_score_label =Label(master , text = "Player : 0" , font = ('arial 12 bold'))
player_score_label =Label(master , text = "Player : 0" , font = ('arial 12 bold'))
player_score_label.grid( row= 2, sticky= W)

computer_score_label =Label(master , text = "Computer : 0" , font = ('arial 12 bold'))
computer_score_label.grid( row= 2, sticky= E)


player_choice_label=Label(master , font = ('arial 12 bold'))
player_choice_label.grid( row= 3, sticky= W)

computer_choice_label=Label(master , font = ('arial 12 bold'))
computer_choice_label.grid( row= 3, sticky= E)

outcome_label = Label(master,font = ("aerial 12"))
outcome_label.grid( row= 2, sticky= N)


#BUTTONS
rock_button =Button(master, text = "ROCK",width=15,command=lambda: outcome_handler('rock') ).grid(row=4,sticky=W, padx=5 , pady=5)
paper_button =Button(master, text = "PAPER",width=15,command=lambda: outcome_handler('paper') ).grid(row=4,sticky=N , pady=5)
scissor_button =Button(master, text = "SCISSORS",width=15,command=lambda: outcome_handler('scissors') ).grid(row=4,sticky=E, padx=5, pady=5)
play_again_button = Button(master, text="Play Again",width=14, command=reset_game, font=("Arial", 12)).grid(row = 5, sticky =S)

Label(master).grid(padx=5)
master.mainloop()