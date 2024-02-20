import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz
import schedule
import threading
import time

def save_reminder():
    reminder_date = date_entry.get()
    reminder_time = time_entry.get()
    reminder_text = text_entry.get("1.0", "end-1c")
    with open("reminders.txt", "a") as file:
        file.write(f"{reminder_date} {reminder_time}: {reminder_text}\n")
    messagebox.showinfo("Reminder", "Reminder saved successfully!")

def clear_fields():
    date_entry.delete(0, "end")
    time_entry.delete(0, "end")
    text_entry.delete("1.0", "end")

def check_reminders():
    now = datetime.now(pytz.timezone('Europe/Kiev'))
    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    with open("reminders.txt", "r") as file:
        reminders = file.readlines()
        for reminder in reminders:
            reminder_date_time, reminder_text = reminder.strip().split(": ")
            reminder_date, reminder_time = reminder_date_time.split()
            if reminder_date == today and reminder_time == current_time:
                messagebox.showinfo("Reminder", reminder_text)

def start_scheduler():
    schedule.every().minute.do(check_reminders)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Create main window
root = tk.Tk()
root.title("Daily Reminder")

# Date Entry
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=10, pady=5)
date_entry = tk.Entry(root, width=20)
date_entry.grid(row=0, column=1, padx=10, pady=5)

# Time Entry
time_label = tk.Label(root, text="Time (HH:MM):")
time_label.grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(root, width=20)
time_entry.grid(row=1, column=1, padx=10, pady=5)

# Text Entry
text_label = tk.Label(root, text="Reminder:")
text_label.grid(row=2, column=0, padx=10, pady=5)
text_entry = tk.Text(root, width=30, height=5)
text_entry.grid(row=2, column=1, padx=10, pady=5)

# Save Button
save_button = tk.Button(root, text="Save Reminder", command=save_reminder)
save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Clear Button
clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

# Start Scheduler
scheduler_thread = threading.Thread(target=start_scheduler)
scheduler_thread.start()

# Run the main loop
root.mainloop()
