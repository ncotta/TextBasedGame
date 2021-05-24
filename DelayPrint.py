import sys
import time


def delay_print(s, delay):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


def enum_delay(enumList):
    for i, j in enumerate(enumList):
        print(f"[{i + 1}]", j)
        time.sleep(0.25)


def checkChoice(options, func):
    choice = input(">> ")
    try:
        choice = int(choice)
        if not (1 <= choice <= len(options)):
            print("Invalid option. Please try again.")
            func()

    except ValueError:
        print("Invalid option. Please try again.")
        func()

    return choice
