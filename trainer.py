import os
import time
import string
import random
import config


code = {'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--.."}
config.score = 0


def textToCode():
    randchar = random.choice(string.ascii_lowercase)
    morse = randchar
    uInput = input(morse+"\t")
    if (uInput == code[randchar]):
        print("Correct answer!!")
        config.score += 1
    else:
        print("Wrong!")
    time.sleep(0.3)
    os.system('clear')


def codeToText():
    randchar = random.choice(string.ascii_lowercase)
    morse = code[randchar]
    uInput = input(morse+"\t")
    if (uInput == randchar):
        print("Correct answer!!")
        config.score += 1
    else:
        print("Wrong!")
    time.sleep(0.3)
    os.system('clear')


def result(score):
    input("You have scored "+str(score)+" out of 10")
    os.system('clear')
    main()


def main():
    try:
        config.choice = int(input("To train from \"Text to Code\" enter 1 \n From \"Code to Text\" enter 2 \n to Exit enter 0\n"))
    except ValueError:
        return 0
    if (config.choice == 1):
        os.system('clear')
        for i in range(10):
            textToCode()
        result(config.score)
    elif (config.choice == 2):
        os.system('clear')
        for i in range(10):
            codeToText()
        result(config.score)
    else:
        return 0


main()
