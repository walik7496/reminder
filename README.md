# Daily Reminder Application

This is a simple reminder application built with Python using the `tkinter` library for the graphical user interface (GUI) and `schedule` for scheduling reminders. It allows users to set reminders for a specific date and time. The application will show a reminder alert when the set time arrives.

## Features
- Set daily reminders with a date, time, and text.
- Saves reminders to a text file (`reminders.txt`).
- Reminders are checked every minute, and alerts are shown when the time matches the current time.
- Provides a GUI for easy interaction.

## Requirements
- Python 3.x
- tkinter (usually comes pre-installed with Python)
- schedule (`pip install schedule`)
- pytz (`pip install pytz`)

## Installation

1. Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
   
2. Install the required packages:
   ```bash
   pip install schedule pytz
   ```

3. Clone or download the project files.

## How to Use

1. Run the script:

```bash
python reminder_app.py
```

2. The application window will appear with fields to enter:

- Date (YYYY-MM-DD)
- Time (HH:MM)
- Reminder Text

3. Click the "Save Reminder" button to save the reminder.

- The reminder will be saved to a file called reminders.txt in the format: YYYY-MM-DD HH:MM: reminder_text.

4. The application will continuously check for reminders that are scheduled for the current date and time.

- If a reminder matches the current date and time, a pop-up will display the reminder text.

5. You can also click "Clear Fields" to reset the input fields.

## How It Works

1. Saving a Reminder:

- The user enters a date, time, and reminder text and clicks "Save Reminder."
- The reminder is stored in a file called reminders.txt.

2. Reminder Check:

- Every minute, the application checks for reminders scheduled for the current date and time.
- If there is a match, it shows a message box with the reminder text.

3. Reminder File:

- The reminders are saved in the file reminders.txt with each line formatted as:
  ```bash
  YYYY-MM-DD HH:MM: reminder_text
  ```

4. Scheduler:

- The application uses the schedule library to run the reminder check every minute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
