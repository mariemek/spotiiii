
import pyautogui
import webbrowser
import time

def  create_spotify_account(email, password):

    webbrowser.open('https://www.spotify.com/ca-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F&flow_ctx=5ce688fa-b110-4093-a8fd-1e043a15a034%3A1721121452')
    time.sleep(2)


        
    # Navigate to the email field and type the email
    pyautogui.press('tab')

    pyautogui.typewrite(email)

    time.sleep(1)
    
#     # Navigate to the password field and type the password
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    time.sleep(1)
    
#     # Fill in other required fields
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('enter')
    # time.sleep(1)
    pyautogui.press('space')
    # time.sleep(1)
    pyautogui.typewrite("streaming")
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.typewrite("10")
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.typewrite("June")
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.typewrite("2002")
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('space')
    # time.sleep(1)
    pyautogui.press('tab')
    # time.sleep(1)
    pyautogui.press('enter')
    # time.sleep(1)


    
#     # Move through other fields to complete the signup
#     current_mouse_position = pyautogui.position()
#     click_x, click_y = current_mouse_position
#     pyautogui.moveTo(click_x, click_y)
#     pyautogui.click()
#     time.sleep(1)


    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('space')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('tab')
    # # time.sleep(1)
    # pyautogui.press('enter')
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('space')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('space')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('enter')

# # Read email and password pairs from the text file
with open('file.txt', 'r') as file:
    for line in file:
        email, password = line.strip().split(',')
        create_spotify_account(email.strip(), password.strip())