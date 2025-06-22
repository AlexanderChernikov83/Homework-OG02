import tkinter as tk
from tkinter import messagebox

# Вопросы и ответы
questions = [
    ("Это можно открыть, но нельзя закрыть. Что это?", "рот"),
    ("Сидит дед, во сто шуб одет, кто его раздевает — слёзы проливает.", "лук"),
    ("Не лает, не кусает, а в дом не пускает.", "замок"),
    ("Без языка, а правду скажет.", "зеркало"),
    ("Её бьют, а она только крепче становится.", "закалка")
]

current_question = 0
score = 0

def check_answer():
    global current_question, score
    user_input = answer_entry.get().strip().lower()
    correct_answer = questions[current_question][1]

    if user_input == correct_answer:
        score += 1
        messagebox.showinfo("Правильно!", "✅ Отлично! Ты угадал.")
    else:
        messagebox.showinfo("Неправильно", f"❌ Увы. Правильный ответ: {correct_answer}")

    current_question += 1
    answer_entry.delete(0, tk.END)

    if current_question < len(questions):
        question_label.config(text=questions[current_question][0])
    else:
        messagebox.showinfo("Игра окончена", f"Ты отгадал {score} из {len(questions)} загадок.")
        root.destroy()

# Интерфейс
root = tk.Tk()
root.title("Викторина: Угадай слово")
root.geometry("500x200")
root.configure(bg="lightyellow")

question_label = tk.Label(root, text=questions[0][0], font=("Arial", 12), bg="lightyellow", wraplength=480)
question_label.pack(pady=20)

answer_entry = tk.Entry(root, width=40)
answer_entry.pack(pady=5)

submit_button = tk.Button(root, text="Ответить", command=check_answer)
submit_button.pack(pady=10)

root.mainloop()
