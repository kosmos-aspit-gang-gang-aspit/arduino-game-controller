import serial
import time
import keyboard

Arduino = serial.Serial("com3", 9600)
pressedButtons = []


def controller(data):
    global pressedButtons

    if "w" in data and "w" not in pressedButtons:
        keyboard.press("w")
        pressedButtons.insert(0, "w")
    elif "w" not in data and "w" in pressedButtons:
        keyboard.release("w")
        try:
            pressedButtons.remove("w")
        except ValueError as e:
            pass

    if "s" in data and "s" not in pressedButtons:
        keyboard.press("s")
        pressedButtons.insert(0, "s")
    elif "s" not in data and "s" in pressedButtons:
        keyboard.release("s")
        try:
            pressedButtons.remove("s")
        except ValueError:
            pass

    if "a" in data and "a" not in pressedButtons:
        keyboard.press("a")
        pressedButtons.insert(0, "a")
    elif "a" not in data and "a" in pressedButtons:
        keyboard.release("a")
        try:
            pressedButtons.remove("a")
        except ValueError:
            pass

    if "d" in data and "d" not in pressedButtons:
        keyboard.press("d")
        pressedButtons.insert(0, "d")
    elif "d" not in data and "d" in pressedButtons:
        keyboard.release("d")
        try:
            pressedButtons.remove("d")
        except ValueError:
            pass

    print("pressed buttons: ", pressedButtons)

# wsadwsadaaaaaaaaaaaaaaaaaaaawssddaaawsadaaaaaaaaaaaddwsawsdawsdaswdawsaddaaaaaaddaadaadaddaaddaaaddaaaadddadaadadadadawsadsadwwawwwadaadawsw

while True:
    data = str(Arduino.readline().decode("ascii")).lower()
    # data = "w"
    print("data: ", data)
    controller(data)

