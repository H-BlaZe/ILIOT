import time
import keyboard
import pyfiglet
import random


def main():
    while True:
        answer = input('\nPaste the answer:- ')
        answer = answer.lower()

        speedIn = int(input('[1] Constant Speed(0.1)\n[2] Random Speed\n[3] Exit\n>>>'))
        if speedIn == 1:
            print('OK')
        elif speedIn == 2:
            speedList = [0.1, 0.2, 0.0, 0.4]
        elif speedIn == 3:
            exit()
        else:
            print("Invalid Option")
            main()

        print("Click to the intended textbox in 3 seconds:")
        time.sleep(3)
        for letter in answer:
            str_letter = str(letter)
            special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']
            if letter in special:
                keyboard.press('shift')
            keyboard.press(letter)
            keyboard.release('shift')
            if speedIn == 1:
                time.sleep(float(0.1))
            elif speedIn == 2:
                n = random.randint(0, 2)
                time.sleep(float(speedList[n]))


def launch():
    print(pyfiglet.figlet_format("ILIOT", font="standard"))
    print("created by: H_BlaZe")
    print("Github: https://github.com/H-Blaze")
    print("▬▬ι═══════ﺤ    -═══════ι▬▬")
    print('Got OK from system.')
    time.sleep(0.2)
    print('Launching INTERFACE.')
    main()




launch()
