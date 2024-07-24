# Spotify Account Automation

This project contains a script to automate the process of navigating to the Spotify website and clicking the "Create Account" button using Python and `pyautogui`.

## Requirements

- Python 3.x
- `pyautogui` library
- `webbrowser` module (part of the Python standard library)

## Installation

1. Install `pyautogui`:
    ```bash
    pip install pyautogui
    ```

2. Take a screenshot of the "Create Account" button on the Spotify signup page and save it as `create_account_button.png` in the project directory.

## Usage

1. Navigate to the project directory:
    ```bash
    cd SpotifyAccountAutomation
    ```

2. Run the script:
    ```bash
    python main.py  10
    ```

## Notes

- The `confidence` parameter in `locateOnScreen` can be adjusted if the script has difficulty finding the button.
- Ensure your screen resolution and scaling are the same when taking the screenshot and running the script.
- If the button is not found, ensure the image file name and location are correct and that the screenshot accurately captures the button.
