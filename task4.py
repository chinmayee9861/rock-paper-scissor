from tkinter import *
from random import randint

choices = ["Rock", "Paper", "Scissor"]
total_rounds = 5
ROUND = total_rounds

game_is_on = True


def ai_score():
    final = int(computer_score['text'])
    final += 1
    computer_score['text'] = str(final)


def your_score():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


def check_winner(player_choice, computer_choice):
    global ROUND

    if player_choice == computer_choice:
        result_check.config(text="Again!")
    elif (player_choice == "Rock" and computer_choice == "Scissor") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissor" and computer_choice == "Paper"):
        your_score()
        result_check.config(text="You win this round!")
    else:
        ai_score()
        result_check.config(text="AI wins this round!")

    ROUND -= 1
    round_check.config(text=f"Rounds left: {ROUND}")

    if ROUND == 0:
        determine_final_winner()


def determine_final_winner():
    player_final = int(player_score['text'])
    computer_final = int(computer_score['text'])

    if player_final > computer_final:
        round_check.config(text="")
        winner_check.config(text="You  Win!")

    elif player_final < computer_final:
        round_check.config(text="")
        winner_check.config(text="Winner is AI!")
    else:
        round_check.config(text="")
        winner_check.config(text="Tie!")

    disable_buttons()


def disable_buttons():
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)


def enable_buttons():
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissor_button.config(state=NORMAL)


def click(player_choice):
    if ROUND > 0:
        computer_choice = choices[randint(0, 2)]
        if computer_choice == "Rock":
            computer_choice_img.config(image=rock2_img)
        elif computer_choice == "Paper":
            computer_choice_img.config(image=paper2_img)
        else:
            computer_choice_img.config(image=scissor2_img)

        if player_choice == "Rock":
            player_choice_img.config(image=rock1_img)
        elif player_choice == "Paper":
            player_choice_img.config(image=paper1_img)
        else:
            player_choice_img.config(image=scissor1_img)

        check_winner(player_choice, computer_choice)


def reset():
    global ROUND
    ROUND = total_rounds
    result_check.config(text="")
    player_score.config(text="0")
    computer_score.config(text="0")
    round_check.config(text=f"Rounds left: {ROUND}")
    winner_check.config(text="")
    enable_buttons()


window = Tk()
window.title("Rock Paper & Scissor")
window.config(padx=20, pady=40, bg="Black")

# images
rock1_img = PhotoImage(file="stone_1.png")
rock2_img = PhotoImage(file="stone_2.png")
paper1_img = PhotoImage(file="paper_1.png")
paper2_img = PhotoImage(file="paper_2.png")
scissor1_img = PhotoImage(file="scissor_1.png")
scissor2_img = PhotoImage(file="scissor_2.png")
tittle_img = PhotoImage(file="sps.png")

tittle_frame = Label(image=tittle_img)
tittle_frame.grid(row=0, column=2)

player_choice_img = Label(image=rock1_img)
player_choice_img.grid(row=2, column=0)

computer_choice_img = Label(image=rock2_img)
computer_choice_img.grid(row=2, column=4)

player_label = Label(text="You", font=("Courier", 20, "bold"), bg="Black", fg="white")
player_label.grid(row=1, column=1)

computer_label = Label(text="AI", font=("Courier", 20, "bold"), bg="Black", fg="White")
computer_label.grid(row=1, column=3)

player_score = Label(text="0", font=("Courier", 20, "bold"), bg="Black", fg="White")
player_score.grid(row=2, column=1)

computer_score = Label(text="0", font=("Courier", 20, "bold"), bg="Black", fg="White")
computer_score.grid(row=2, column=3)

result_check = Label(text="", font=("Lucid", 20, "bold"), bg="Black", fg="White")
result_check.grid(row=4, column=2)

winner_check = Label(text="", font=("Lucid", 20, "bold"), bg="Black", fg="White")
winner_check.grid(row=2, column=2,columnspan=1)

round_check = Label(text=f"Rounds left: {ROUND}", font=("Lucid", 20, "bold"), bg="Black", fg="White")
round_check.grid(row=2, column=2)

rock_button = Button(text="ROCK", width=10, height=3, font=("Lucid", 10, "bold"), bg="Red", fg="Black",
                     command=lambda: click("Rock"))
rock_button.grid(row=3, column=1)

paper_button = Button(text="PAPER", width=10, height=3, font=("Lucid", 10, "bold"), bg="Red", fg="Black",
                      command=lambda: click("Paper"))
paper_button.grid(row=3, column=2)

scissor_button = Button(text="SCISSOR", width=10, height=3, font=("Lucid", 10, "bold"), bg="Red", fg="Black",
                        command=lambda: click("Scissor"))
scissor_button.grid(row=3, column=3)

reset_button = Button(text="RESET", width=15, font=("Courier", 15, "bold"), bg="Yellow", command=reset)
reset_button.grid(row=5, column=2)

window.mainloop()