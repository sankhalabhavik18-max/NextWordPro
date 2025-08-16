from tensorflow.keras.models import load_model
import numpy as np
import pickle
import tkinter as tk
from tkinter import ttk

# Load the model and tokenizer
model = load_model('nextword1.h5')
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

def predict_next_words(model, tokenizer, text):
    sequence = tokenizer.texts_to_sequences([text])[0]
    sequence = np.array(sequence)
    preds = model.predict(sequence)
    preds_array = np.array(preds)
    max_indices = np.argsort(preds_array)[0, ::-1]
    predictions = []
    for index in max_indices[:3]:
        for key, value in tokenizer.word_index.items():
            if value == index:
                predictions.append(key)
                break
    return predictions

def update_suggestions(event):
    try:
        text = entry.get("1.0", tk.END).strip()
        last_word = text.split()[-1]
        if len(last_word) > 0:
            suggestions = predict_next_words(model, tokenizer, last_word)
            suggestion_dropdown["values"] = suggestions
            suggestion_dropdown.current(0)
        else:
            suggestion_dropdown["values"] = []
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        pass

def on_select(event):
    selected_text = suggestion_dropdown.get()
    entry.insert(tk.END, " " + selected_text)

# Create the GUI window
window = tk.Tk()
window.title("Next Word Predictor")
window.geometry("500x400")
window.minsize(400, 400)
window.maxsize(800, 400)

# Create the heading
heading_label = tk.Label(window, text="Next Word Predictor", font=("Arial", 20, "bold"), fg="blue")
heading_label.pack(pady=10)

# Create the description label
description_label = tk.Label(
    window,
    text="Enter text and choose a suggestion for the next word:",
    font=("Arial", 14),
    wraplength=450,
    justify="center",
    fg="black"
)
description_label.pack()

# Create the input text entry
entry = tk.Text(window, font=("Arial", 12), height=5)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_suggestions)

# Create the suggestion dropdown
suggestion_dropdown = ttk.Combobox(window, font=("Arial", 12), width=30, state="readonly")
suggestion_dropdown.pack(pady=5)
suggestion_dropdown.bind("<<ComboboxSelected>>", on_select)

def clear_entry():
    entry.delete('1.0', tk.END)

# Create the button to clear the text entry
clear_button = tk.Button(window, text="Clear", font=("Arial", 12), command=clear_entry, bg="red", fg="white")
clear_button.pack(pady=5)

# Create the footer
footer_label = tk.Label(window, text="Created by SANKHALA BHAVIK SHANTILAL ©", font=("Arial", 10), fg="gray")
footer_label.pack(side="bottom", pady=10)

window.mainloop()
