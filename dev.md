# Overview

This file will serve as the place where I will store my thought process and ideas as I build out the application.

## Aim

The aim of this script is to create a popup window every 15 minutes to remind a computer user to take a break and stretch themselves.

## Implementation

This project will be built using Python and the TKinter module for the gui (including the popup window).
We will make use of the `threading` module to have the timer run in the background, thereby using a class based approach.

## Design

Project should have a simple design. On first run, program will provide a home menu containing the following attributes:

- Project title
- Brief explanation of project
- Time intervals for notifications (10 - 30 range)
- Custom messsage for the popup to display when timer is up.
- Whether to use Text to Speech or not
- Whether to use male or female tts voice.
- Start and stop buttons to control the application.
- Lockin button to disable timer for 1 hour with a 30 minute cooldown.
- Display with the amount of minutes and seconds until the next break

The popup window should also have a simple UI consisting of the following elements:

- Window title
- Message set for user.
- Ok button to restart the timer.
- "Lock in" button to stop the timer for 1 hour.
- Close button which will automatically restart the timer.