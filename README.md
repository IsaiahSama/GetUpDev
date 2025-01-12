# GetUpDev

This will be my take on a simple timer based application designed to remind users to stretch and take a break every 15 minutes whilst using their device.

## Using the App

### Building it yourself!

1. Ensure you have at least Python 3.10 installed.
1. Clone the repository
1. Run `pip install -r requirements.txt` to install the required libraries (Use a virtualenv if you want to.)
1. Run `python main.py` to run the app.
1. (Optional) If you are on Linux and want to use the Text to Speech, you will need to also run: `sudo apt update && sudo apt install espeak ffmpeg libespeak1`

### Using the Exe (Deprecated)!

1. Download the `dist/main.exe` file.
1. Open and run it like any other exe file
1. Profit.

Note: When using the EXE, it WILL be flagged as suspicious software, and there's a high chance that if you have an antivirus it may quarantine the file. If this happens, just google how to whitelist the file.

Update: Removed EXE due to security complications. If you want exe, you'll have to build it yourself.

## Features

Project will have a simple design. On first run, program will provide a home menu containing the following items:

- Project title
- Brief explanation of project
- Time intervals for notifications (10 - 30 range)
- Custom messsage for the popup to display when timer is up.
- Whether to use Text to Speech or not
- Whether to use male or female tts voice.
- Start and stop buttons to control the application.
- Display with the amount of minutes and seconds until the next break

The popup window should also have a simple UI consisting of the following elements:

- Window title
- Message set for user.
- Ok button to restart the timer.
- "Lock in" button to stop the timer for 1 hour.
- Close button which will automatically restart the timer.

## Options

Interval Time
: Determines the time for breaks, with values ranging from 10 to 30 minutes. The time you set will be the duration of the timer before you're reminded to take a break.

Notification Message
: This is the message displayed / Voiced (If using TTS) when the timer is up.

Use TTS
: This determines whether the app should use Text to Speech or not.

Read out Message Notifications
: The app will display notifications based on actions such as starting and stopping a timer manually. This option will determine whether these notifcations be spoken as well or not (I recommend leaving it off)

Select Voice
: If you are using TTS, this will determine whether the voice is male or female.

Lock In
: Lock in pauses the timer for up to 1 hour. This is for if you need to temporarily enter a meeting or the like, where you don't want to be distracted.

## Conclusion!

Have fun, stay healthy, and take care of your eyes and bones!