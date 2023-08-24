import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_choice):
        return user_choice == self.correct_choice

class Quizgame:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        self.root.configure(bg="#FFD700")  # Set background color

        self.label = tk.Label(root, text="", wraplength=4000,font=("callbri", 16), bg="#FFD700")
        self.label.pack(pady=10)

        self.radio_buttons = []
        self.radio_var = tk.StringVar()

        for i in range(len(self.questions[self.current_question_index].choices)):
            choice = self.questions[self.current_question_index].choices[i]
            radio_button = tk.Radiobutton(root, text=choice, variable=self.radio_var, value=chr(65 + i),font=("callbri", 16), bg="#FFD700")
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(root, text="Next",font=("callbri", 12), command=self.next_question, bg="#FF6347", fg="white")
        self.next_button.pack(pady=10)

        self.show_question(self.current_question_index)

    def show_question(self, index):
        question = self.questions[index]
        self.label.config(text=question.question)
        for i, choice in enumerate(question.choices):
            self.radio_buttons[i].config(text=choice,font=("callbri", 16), bg="#FFD700", fg="black")
        self.radio_var.set(None)

    def next_question(self):
        if self.radio_var.get() is None:
            messagebox.showerror("Error", "Please select an answer.")
            return

        if self.questions[self.current_question_index].check_answer(self.radio_var.get()):
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question(self.current_question_index)
        else:
            self.show_final_result()

    def show_final_result(self):
        result_text = f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}"
        result_label = tk.Label(self.root, text=result_text, font=("callbri", 23), bg="#FFD700")
        result_label.pack(pady=20)

        play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, bg="#32CD32", fg="white")
        play_again_button.pack(pady=10)

    def play_again(self):
        self.current_question_index = 0
        self.score = 0
        self.show_question(self.current_question_index)

def main():
    questions = [
        Question("What is the capital of France?", ["A. London", "B. Paris", "C. Madrid", "D. Rome"], "B"),
        Question("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
        Question("What is the largest mammal?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"], "B"),
        Question("Which gas do plants use for photosynthesis?", ["A. Carbon Monoxide", "B. Oxygen", "C. Nitrogen", "D. Carbon Dioxide"], "D"),
        Question("What is the tallest mountain in the world?", ["A. K2", "B. Mount Everest", "C. Kanchenjunga", "D. Lhotse"], "B"),
        Question("Which element has the chemical symbol 'H'?", ["A. Helium", "B. Hydrogen", "C. Helix", "D. Hafnium"], "B"),
        Question("What is the smallest prime number?", ["A. 1", "B. 2", "C. 3", "D. 5"], "B"),
        Question("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"], "B"),
        Question("Which country is known as the 'Land of the Rising Sun'?", ["A. China", "B. Japan", "C. South Korea", "D. Thailand"], "B"),
        Question("What is the chemical symbol for gold?", ["A. G", "B. Au", "C. Go", "D. Gl"], "B")
    ]

    root = tk.Tk()
    root.title("Quiz Game")
    app = Quizgame(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
