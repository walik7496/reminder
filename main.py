import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz
import schedule
import threading
import time

running = True  # Flag for the scheduler thread
TIMEZONE = pytz.timezone('Europe/Kiev')  # Set your timezone here


def save_reminder():
    reminder_date = date_entry.get().strip()
    reminder_time = time_entry.get().strip()
    reminder_text = text_entry.get("1.0", "end-1c").strip()

    # Automatic time formatting
    try:
        formatted_time = datetime.strptime(reminder_time, "%H%M").strftime("%H:%M") \
            if reminder_time.isdigit() and len(reminder_time) == 4 \
            else datetime.strptime(reminder_time, "%H:%M").strftime("%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Use HHMM or HH:MM")
        return

    with open("reminders.txt", "a", encoding="utf-8") as file:
        file.write(f"{reminder_date} {formatted_time}: {reminder_text}\n")

    messagebox.showinfo("Reminder", "Reminder saved successfully!")


def clear_fields():
    date_entry.delete(0, "end")
    time_entry.delete(0, "end")
    text_entry.delete("1.0", "end")


def check_reminders():
    now = datetime.now(TIMEZONE)

    try:
        with open("reminders.txt", "r", encoding="utf-8") as file:
            reminders = file.readlines()
    except FileNotFoundError:
        return

    new_reminders = []

    for reminder in reminders:
        parts = reminder.strip().split(": ", 1)
        if len(parts) < 2:
            continue

        try:
            reminder_date_time, reminder_text = parts
            reminder_date, reminder_time = reminder_date_time.split()
        except ValueError:
            continue

        # Convert to datetime and localize to the same timezone
        try:
            reminder_dt = datetime.strptime(f"{reminder_date} {reminder_time}", "%Y-%m-%d %H:%M")
            reminder_dt = TIMEZONE.localize(reminder_dt)
        except ValueError:
            continue

        if reminder_dt <= now:
            # Trigger reminder if the time has passed
            try:
                messagebox.showinfo("Reminder", reminder_text)
            except tk.TclError:
                pass
        else:
            # Keep future reminders
            new_reminders.append(reminder)

    # Rewrite the file without triggered or past reminders
    with open("reminders.txt", "w", encoding="utf-8") as file:
        file.writelines(new_reminders)


def start_scheduler():
    schedule.every().minute.do(check_reminders)
    while running:
        schedule.run_pending()
        time.sleep(1)


def on_close():
    global running
    running = False
    root.destroy()


# Create main window
root = tk.Tk()
root.title("Daily Reminder")
root.resizable(False, False) 

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_close)

# Date Entry
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=10, pady=5)
date_entry = tk.Entry(root, width=20)
date_entry.grid(row=0, column=1, padx=10, pady=5)

# Time Entry
time_label = tk.Label(root, text="Time (HH:MM or HHMM):")
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
scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
scheduler_thread.start()

# Immediately clean past reminders at startup
check_reminders()

# Run the main loop
root.mainloop()
