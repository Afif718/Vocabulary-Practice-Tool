import tkinter as tk
from tkinter import ttk
import pyttsx3
import threading
import time
import requests

# ========= TTS Engine =========
engine = pyttsx3.init()
engine.setProperty("rate", 130)

# ========= Global Variables =========
current_word_list = []
current_index = 0
practicing = False
correct_count = 0
incorrect_count = 0

# ========= Text-to-Speech Function =========
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ========= UI Stats Update =========
def update_stats():
    """Update Correct / Incorrect / Remaining labels."""
    total = len(current_word_list)
    remaining = max(total - current_index, 0)
    correct_label.config(text=f"✅ Correct: {correct_count}")
    incorrect_label.config(text=f"❌ Incorrect: {incorrect_count}")
    remaining_label.config(text=f"🔁 Remaining: {remaining}")

# ========= Helper: sleep with interrupt =========
def wait_with_interrupt(seconds):
    """Wait for 'seconds' seconds but exit early if practicing is False."""
    for _ in range(int(seconds * 10)):
        if not practicing:
            return False
        time.sleep(0.1)
    return True

# ========= Main Practice Loop =========
def practice_loop():
    global current_index, practicing, correct_count, incorrect_count

    practicing = True
    while current_index < len(current_word_list) and practicing:
        word = current_word_list[current_index]
        result_label.config(text=f"🗣️ Listen... ({len(current_word_list) - current_index} left)")
        update_stats()

        speak(word)

        result_label.config(text="✍️ Write or type the spelling...")
        spelling_entry.delete(0, tk.END)
        spelling_entry.focus()

        # wait for 5 seconds (or until stop)
        if not wait_with_interrupt(5):
            break

        user_input = spelling_entry.get().strip().lower()
        correct = word.lower()

        if user_input == correct:
            correct_count += 1
            result_label.config(text=f"✅ Correct! {word}")
        elif user_input != "":
            if word not in incorrect_words_box.get(0, tk.END):
                incorrect_words_box.insert(tk.END, word)
                incorrect_count += 1
            result_label.config(text=f"❌ Incorrect! You wrote '{user_input}'. Correct: {word}")
        else:
            correct_count += 1
            result_label.config(text=f"✅ Correct spelling: {word} (write it on paper?)")

        spelled = ' '.join(list(word.upper()))
        speak(f"The correct spelling is {spelled}")

        current_index += 1
        update_stats()

        # wait 3 seconds before next word
        if not wait_with_interrupt(3):
            break

    practicing = False
    if current_index >= len(current_word_list):
        result_label.config(text="🎉 All words done!")
    else:
        result_label.config(text="⏹️ Practice stopped.")
    update_stats()

# ========= Start Practice =========
def start_practice():
    global current_word_list, current_index, practicing, correct_count, incorrect_count
    topic = topic_entry.get().strip()
    if not topic:
        result_label.config(text="❗ Please enter a topic or word.")
        return

    # Fetch related words from Datamuse API
    try:
        response = requests.get(f"https://api.datamuse.com/words?ml={topic}&max=20")
        words_data = response.json()
        current_word_list = [w['word'] for w in words_data]
    except Exception as e:
        result_label.config(text=f"❗ Error fetching words: {e}")
        return

    if not current_word_list:
        result_label.config(text="❗ No words found for this topic.")
        return

    current_index = 0
    correct_count = 0
    incorrect_count = 0
    incorrect_words_box.delete(0, tk.END)
    update_stats()

    threading.Thread(target=practice_loop, daemon=True).start()

# ========= Stop Practice =========
def stop_practice():
    global practicing
    practicing = False
    result_label.config(text="⏹️ Practice stopped.")
    update_stats()

# ========= GUI =========
root = tk.Tk()
root.title("Vocabulary Practice Tool")
root.geometry("900x520")
root.configure(bg="#f8f8f8")

main_frame = tk.Frame(root, bg="#f8f8f8")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left side
left_frame = tk.Frame(main_frame, bg="#f8f8f8")
left_frame.pack(side="left", fill="both", expand=True)

tk.Label(left_frame, text="📝 Enter a Topic or Word:", font=("Arial", 14), bg="#f8f8f8").pack(pady=5)
topic_entry = tk.Entry(left_frame, font=("Arial", 12), width=40)
topic_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(left_frame, bg="#f8f8f8")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="▶️ Start", command=start_practice, font=("Arial", 12), bg="green", fg="white").pack(side="left", padx=10)
tk.Button(btn_frame, text="⏹️ Stop", command=stop_practice, font=("Arial", 12), bg="red", fg="white").pack(side="left", padx=10)

# Stats frame
stats_frame = tk.Frame(left_frame, bg="#f8f8f8")
stats_frame.pack(pady=(8, 10), fill="x")

correct_label = tk.Label(stats_frame, text="✅ Correct: 0", font=("Arial", 12), bg="#f8f8f8", anchor="w", width=18)
correct_label.pack(side="left", padx=(0,10))
incorrect_label = tk.Label(stats_frame, text="❌ Incorrect: 0", font=("Arial", 12), bg="#f8f8f8", anchor="w", width=18)
incorrect_label.pack(side="left", padx=(0,10))
remaining_label = tk.Label(stats_frame, text="🔁 Remaining: 0", font=("Arial", 12), bg="#f8f8f8", anchor="w", width=18)
remaining_label.pack(side="left")

# Entry field for spelling
spelling_entry = tk.Entry(left_frame, font=("Arial", 14), width=40)
spelling_entry.pack(pady=10)

# Feedback label
result_label = tk.Label(left_frame, text="", font=("Arial", 14), bg="#f8f8f8", wraplength=500, justify="center")
result_label.pack(pady=10)

# Right side – Misspelled words
right_frame = tk.Frame(main_frame, bg="#f0f0f0", relief="groove", bd=2)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

tk.Label(right_frame, text="❗ Misspelled Words", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
incorrect_words_box = tk.Listbox(right_frame, font=("Arial", 12), width=25, height=20)
incorrect_words_box.pack(pady=5)

# Run the GUI loop
update_stats()
root.mainloop()
