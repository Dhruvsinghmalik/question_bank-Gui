import tkinter as tk
from tkinter import messagebox, ttk

# Question data: each question has a text, options, and the correct answer
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript",
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
    },
    {
        "question": "Who developed Python?",
        "options": [
            "Dennis Ritchie",
            "Guido van Rossum",
            "James Gosling",
            "Bjarne Stroustrup",
        ],
        "answer": "Guido van Rossum",
    },
]

# Global variables
current_question_index = 0
score = 0
answers_summary = []


def load_question():
    """Load the current question and options into the GUI."""
    global current_question_index

    # Clear previous selection
    selected_answer.set(None)

    # Get the current question
    question_data = questions[current_question_index]

    # Update question text
    question_label.config(text=question_data["question"])

    # Update options
    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(text=option, value=option)


def submit_answer():
    """Check the selected answer and proceed to the next question."""
    global current_question_index, score, answers_summary

    selected = selected_answer.get()

    if not selected:
        messagebox.showwarning("No Answer", "Please select an answer.")
        return

    # Record the user's answer and update the score
    correct_answer = questions[current_question_index]["answer"]
    is_correct = selected == correct_answer
    if is_correct:
        score += 1

    answers_summary.append(
        f"Q: {questions[current_question_index]['question']}\n"
        f"Your Answer: {selected}\n"
        f"Correct Answer: {correct_answer}\n{'✔️' if is_correct else '❌'}\n"
    )

    # Move to the next question or show the final result
    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        show_final_result()


def show_final_result():
    """Display the final result and summary of answers."""
    global score, answers_summary

    # Hide the quiz frame
    quiz_frame.pack_forget()

    # Create the result frame
    result_frame = tk.Frame(root, bg="#f0f8ff", pady=20)
    result_frame.pack(fill="both", expand=True)

    result_label = tk.Label(
        result_frame,
        text=f"Quiz Completed!\nYour Score: {score}/{len(questions)}",
        font=("Arial", 18, "bold"),
        bg="#f0f8ff",
        fg="#1e3d59",
    )
    result_label.pack(pady=20)

    summary_label = tk.Label(
        result_frame,
        text="Answer Summary:",
        font=("Arial", 14, "bold"),
        bg="#f0f8ff",
        fg="#1e3d59",
    )
    summary_label.pack(pady=10)

    # Scrollable text widget for the answer summary
    text_area = tk.Text(
        result_frame, wrap="word", font=("Arial", 12), bg="#f0f8ff", fg="#333333"
    )
    text_area.pack(padx=20, pady=10, fill="both", expand=True)
    text_area.insert("1.0", "\n\n".join(answers_summary))
    text_area.config(state="disabled")  # Make it read-only

    # Exit button
    exit_button = tk.Button(
        result_frame,
        text="Exit",
        command=root.destroy,
        font=("Arial", 12, "bold"),
        bg="#4caf50",
        fg="white",
        relief="flat",
    )
    exit_button.pack(pady=20)


# Initialize the main GUI window
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Selected answer variable
selected_answer = tk.StringVar(value=None)

# Quiz Frame
quiz_frame = tk.Frame(root, bg="#f0f8ff", pady=20)
quiz_frame.pack(fill="both", expand=True)

# Question label
question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 16, "bold"),
    wraplength=450,
    bg="#f0f8ff",
    fg="#1e3d59",
)
question_label.pack(pady=20)

# Option buttons (radio buttons)
option_buttons = []
for i in range(4):
    button = ttk.Radiobutton(
        quiz_frame,
        text="",
        variable=selected_answer,
        value="",
        style="TRadiobutton",
    )
    button.pack(anchor="w", padx=50, pady=5)
    option_buttons.append(button)

# Submit button
submit_button = tk.Button(
    quiz_frame,
    text="Submit",
    command=submit_answer,
    font=("Arial", 12, "bold"),
    bg="#0073e6",
    fg="white",
    relief="flat",
)
submit_button.pack(pady=20)

# Load the first question
load_question()

# Start the main loop
root.mainloop()
