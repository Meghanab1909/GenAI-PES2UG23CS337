import tkinter as tk
from tkinter import font
from transformers import pipeline

# Load model once
generator = pipeline("text-generation", model="distilgpt2")

def generate_horoscope():
    sign = entry.get().capitalize()
    prompt = f"Check and return daily/today's horoscope for zodiac sign {sign}."
    result = generator(
        prompt,
        max_new_tokens=60,
        temperature=0.9,
        do_sample=True,
        top_p=0.95,
        num_return_sequences=1,
        truncation=False
    )
    text = result[0]["generated_text"]
    horoscope = text.replace(prompt, "").strip()

    # Basic filter for bad output
    if "true-to" in horoscope or len(horoscope.split()) < 5:
        horoscope = "The stars are quiet today, but trust your instincts and stay open to small surprises."

    output_label.config(
        text=f"{sign} Horoscope:\n\n{horoscope}",
        fg="#333333"
    )

# UI setup
root = tk.Tk()
root.title("✨ Horoscope Generator ✨")
root.geometry("400x300")
root.configure(bg="#f0f0f5")

# Fonts
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

# Title
title_label = tk.Label(root, text="Daily Horoscope", font=title_font, bg="#f0f0f5", fg="#4b0082")
title_label.pack(pady=10)

# Input frame
frame = tk.Frame(root, bg="#f0f0f5")
frame.pack(pady=10)

tk.Label(frame, text="Enter Zodiac Sign:", font=label_font, bg="#f0f0f5").grid(row=0, column=0, padx=5)
entry = tk.Entry(frame, font=label_font, width=15, justify="center")
entry.grid(row=0, column=1, padx=5)

# Button
generate_btn = tk.Button(root, text="🔮 Generate Horoscope", font=label_font, bg="#4b0082", fg="white",
                         command=generate_horoscope)
generate_btn.pack(pady=10)

# Output
output_label = tk.Label(root, text="", wraplength=350, justify="left", font=label_font, bg="#f0f0f5")
output_label.pack(pady=15)

root.mainloop()