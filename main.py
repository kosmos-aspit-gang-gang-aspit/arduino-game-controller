import serial
import time
import keyboard

Arduino = serial.Serial("com3", 9600)
pressedButtons = []


def controller(keystrokes):
    global pressedButtons
    if "w" in data and "w" not in pressedButtons:
        keyboard.press("w")
        pressedButtons.append("w")
    elif "w" not in data and "w" in pressedButtons:
        keyboard.release("w")
        try:
            pressedButtons.remove("w")
        except ValueError as e:
            pass

    if "s" in data and "s" not in pressedButtons:
        keyboard.press("s")
        pressedButtons.append("s")
    elif "s" not in data and "s" in pressedButtons:
        keyboard.release("s")
        try:
            pressedButtons.remove("s")
        except ValueError:
            pass
    print("pressed buttons: ", pressedButtons)


while True:
    data = str(Arduino.readline().decode("ascii")).lower()
    # data = "w"
    print("data: ", data)
    controller(data)
w
