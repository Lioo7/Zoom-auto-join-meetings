import subprocess  # using to open the Zoom app
import pyautogui  # using to automate mouse movement and typing
import time  # using to get the time between the steps
import pandas as pd  # using to extract the data form the csv file to the python program
from datetime import datetime  # using to get the current date and time

def sign_in(meeting_ID, meeting_password):
    # opens up the Zoom app (MacOS)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(1)

    # clicks the Join button
    join_btn = pyautogui.locateCenterOnScreen("join_button_logo.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(1)

    # typing the Meeting ID
    pyautogui.write(meeting_ID)

    # disables both the camera and the microphone
    check_box_btn = pyautogui.locateAllOnScreen("check_box_logo.png")
    for btn in check_box_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(0.5)

    # pressing the Enter button 
    pyautogui.press('enter')
    time.sleep(1)

    # typing the Meeting Password 
    pyautogui.write(meeting_password)
    pyautogui.press('enter')


def main():
    # reading the csv file
    csv_data_frame = pd.read_csv("Meetings Scheduler.csv")

    while(1):
        # getting the current time 
        current_time = datetime.now().strftime("%H:%M")

        # checking if the current time exists in the csv file
        if current_time in str(csv_data_frame['meetingTime']):
            row = csv_data_frame.loc[csv_data_frame['meetingTime'] == current_time]
            # extracts the meeting details   
            meeting_ID = str(row.iloc[0,1])
            print("meeting ID: " + meeting_ID)
            meeting_password = str(row.iloc[0,2])
            print("meeting password: " + meeting_password)

            print("joining the zoom meeting")
            sign_in(meeting_ID, meeting_password)
            time.sleep(120)

if __name__ == "__main__":
    main()


