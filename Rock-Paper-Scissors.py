from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
comp_score = 0

result_label = Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 14))
result_label.pack(pady=20)

user_choice_label = Label(root, text="", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = Label(root, text="", font=("Arial", 12))
comp_choice_label.pack()

score_label = Label(root, text="You: 0  Computer: 0", font=("Arial", 14))
score_label.pack(pady=20)

def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)

    user_choice_label.config(text=f"You chose: {user_choice}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"

    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
            (user_choice == "Scissors" and comp_choice == "Paper") or \
            (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1

    else:
        result = "Computer Wins! 🤖"
        comp_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}  Computer: {comp_score}")

btn_frame = Frame(root)
btn_frame.pack(pady=20)

Button(btn_frame, text="Rock 🪨", width=10, height=2,
       command=lambda: play("Rock")).grid(row=0, column=0, padx=10)

Button(btn_frame, text="Paper 📄", width=10, height=2,
       command=lambda: play("Paper")).grid(row=0, column=1, padx=10)

Button(btn_frame, text="Scissors ✂️", width=10, height=2,
       command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)


def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_label.config(text="You: 0  Computer: 0")
    result_label.config(text="Choose Rock, Paper or Scissors")
    user_choice_label.config(text="")
    comp_choice_label.config(text="")



Button(root, text="Reset Game 🔄", command=reset, bg="lightcoral",
       font=("Arial", 12)).pack(pady=20)

root.mainloop()