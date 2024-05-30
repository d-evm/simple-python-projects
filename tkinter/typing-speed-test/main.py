import tkinter as tk
import time
import requests

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = self.fetch_sample_text()
        
        self.start_time = None
        self.end_time = None

        self.instructions_label = tk.Label(root, text=(
            "Instructions:\n"
            "1. Start typing the text below to begin the timer.\n"
            "2. Press 'Enter' once you finish typing to see your results.\n"
            "3. Press 'Reset' to try again with a new text."
        ))
        self.instructions_label.pack(pady=10)

        self.sample_text_label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.sample_text_label.pack(pady=10)

        self.typing_area = tk.Text(root, height=5, width=50)
        self.typing_area.pack(pady=10)
        self.typing_area.bind("<Key>", self.start_timer)
        self.typing_area.bind("<Return>", self.calculate_speed)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset_test)
        self.reset_btn.pack(pady=10)

    def fetch_sample_text(self):
        try:
            response = requests.get("https://api.quotable.io/random?minLength=100&maxLength=200")
            response.raise_for_status()
            data = response.json()
            return data["content"].lower()
        except requests.RequestException as e:
            return "The swift red squirrel scampers up the tall tree. Reading books can broaden your knowledge and vocabulary. Consistency is key to success.".lower()

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.typing_area.unbind("<Key>")
            self.result_label.config(text="Timer started! Press 'Enter' when done.")

    def calculate_speed(self, event):
        if self.start_time is not None:
            self.end_time = time.time()
            typed_text = self.typing_area.get("1.0", tk.END).strip().lower()
            elapsed_time = self.end_time - self.start_time
            word_count = len(typed_text.split())
            wpm = (word_count / elapsed_time) * 60

            # Calculate accuracy
            sample_words = self.sample_text.split()
            typed_words = typed_text.split()
            
            correct_words = 0
            incorrect_words = 0
            missing_words = 0

            for i in range(min(len(sample_words), len(typed_words))):
                if sample_words[i] == typed_words[i]:
                    correct_words += 1
                else:
                    incorrect_words += 1

            if len(typed_words) < len(sample_words):
                missing_words = len(sample_words) - len(typed_words)

            self.result_label.config(text=(
                f"Your typing speed is: {wpm:.2f} WPM\n"
                f"Total words: {len(sample_words)}\n"
                f"Correct words: {correct_words}\n"
                f"Incorrect words: {incorrect_words}\n"
                f"Missing words: {missing_words}"
            ))
            self.typing_area.unbind("<Return>")

    def reset_test(self):
        self.sample_text = self.fetch_sample_text()
        self.sample_text_label.config(text=self.sample_text)
        self.typing_area.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None
        self.typing_area.bind("<Key>", self.start_timer)
        self.typing_area.bind("<Return>", self.calculate_speed)

root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
