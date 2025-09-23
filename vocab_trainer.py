import tkinter as tk
from tkinter import ttk
import pyttsx3
import threading
import time
import json
import os
import requests  # for dictionary API

# ========== TTS Engine ==========
engine = pyttsx3.init()
engine.setProperty("rate", 130)

# ========== Load Vocabulary from JSON ==========
vocab_file = "vocab_words.json"
if not os.path.exists(vocab_file):
    raise FileNotFoundError(f"{vocab_file} not found. Make sure it's in the same folder.")
with open(vocab_file, "r", encoding="utf-8") as f:
    word_lists = json.load(f)

# ========= Generate dropdown values with word count ==========
display_to_key = {}
combo_values = []
for key, words in word_lists.items():
    count = len(words)
    display_name = f"{key} ({count} words)"
    combo_values.append(display_name)
    display_to_key[display_name] = key

# ========= Global Variables ==========
current_word_list = []
current_index = 0
practicing = False

# Stats
correct_count = 0
incorrect_count = 0

# ========= Text-to-Speech Function ==========
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ========= Dictionary API ==========
def get_definition(word):
    """Fetch word definition from free API"""
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            return meaning
        else:
            return "Definition not found."
    except Exception:
        return "Error fetching definition."

# ========= UI Stats Update ==========
def update_stats():
    total = len(current_word_list)
    remaining = max(total - current_index, 0)
    correct_label.config(text=f"✅ Correct: {correct_count}")
    incorrect_label.config(text=f"❌ Incorrect: {incorrect_count}")
    remaining_label.config(text=f"🔁 Remaining: {remaining}")

# ========= Main Practice Loop ==========
def practice_loop():
    global current_index, practicing, correct_count, incorrect_count
    practicing = True

    while current_index < len(current_word_list) and practicing:
        word = current_word_list[current_index]
        remaining = len(current_word_list) - current_index
        result_label.config(text=f"🗣️ Listen... ({remaining} left)")
        update_stats()

        speak(word)

        # fetch definition
        definition = get_definition(word)
        definition_label.config(text=f"📖 Definition: {definition}")

        result_label.config(text="✍️ Write or type the spelling...")
        spelling_entry.delete(0, tk.END)
        spelling_entry.focus()

        # pause to allow user to type
        time.sleep(5)

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
        time.sleep(3)

    result_label.config(text="🎉 All words done!")
    practicing = False
    update_stats()
    definition_label.config(text="")  # clear definition after finishing

# ========= Start Practice ==========
def start_practice():
    global current_word_list, current_index, practicing, correct_count, incorrect_count
    selected_display = combo.get()
    selected_sublist = display_to_key.get(selected_display, "")
    if not selected_sublist:
        result_label.config(text="❗ Please select a sublist.")
        return
    current_word_list = word_lists[selected_sublist]
    current_index = 0
    correct_count = 0
    incorrect_count = 0
    incorrect_words_box.delete(0, tk.END)
    update_stats()
    threading.Thread(target=practice_loop, daemon=True).start()

# ========= Stop Practice ==========
def stop_practice():
    global practicing
    practicing = False
    result_label.config(text="⏹️ Practice stopped.")
    update_stats()
    definition_label.config(text="")

# ========= GUI ==========
root = tk.Tk()
root.title("Vocabulary Practice Tool")
root.geometry("950x580")
root.configure(bg="#f8f8f8")

main_frame = tk.Frame(root, bg="#f8f8f8")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left side
left_frame = tk.Frame(main_frame, bg="#f8f8f8")
left_frame.pack(side="left", fill="both", expand=True)

tk.Label(left_frame, text="📚 Choose a Sublist:", font=("Arial", 14), bg="#f8f8f8").pack(pady=10)
combo = ttk.Combobox(left_frame, values=combo_values, font=("Arial", 12), width=40)
combo.pack()

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

# Entry field
spelling_entry = tk.Entry(left_frame, font=("Arial", 14), width=40)
spelling_entry.pack(pady=10)

# Feedback label
result_label = tk.Label(left_frame, text="", font=("Arial", 14), bg="#f8f8f8", wraplength=500, justify="center")
result_label.pack(pady=10)

# Definition label
definition_label = tk.Label(left_frame, text="", font=("Arial", 12), bg="#f8f8f8", wraplength=500, justify="left", fg="blue")
definition_label.pack(pady=5)

# Right side – Misspelled words
right_frame = tk.Frame(main_frame, bg="#f0f0f0", relief="groove", bd=2)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

tk.Label(right_frame, text="❗ Misspelled Words", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
incorrect_words_box = tk.Listbox(right_frame, font=("Arial", 12), width=25, height=20)
incorrect_words_box.pack(pady=5)

# Run the GUI loop
update_stats()
root.mainloop()
