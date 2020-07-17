import string
import random


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


def codeToText():
    randchar = random.choice(string.ascii_lowercase)
    morse = code[randchar]
    uInput = input(morse)
    if (uInput == randchar):
        print("Correct answer!!")
    else:
        print("Wrong!")


def main():
    choice = int(input("To train from \"Text to Code\" enter 1 \n From \"Code to Text\" enter 2 \n to Exit enter 0\n"))
    if (choice == 1):
        print("Module under development...")
        main()
    elif (choice == 2):
        for i in range(10):
            codeToText()
        main()
    else:
        return 0


main()
