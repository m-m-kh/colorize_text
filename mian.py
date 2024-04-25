import os
from string import printable
from time import sleep
import random


colors = [
    '\033[31m',  # Red
    '\033[32m',  # Green
    '\033[33m',  # Yellow
    '\033[34m',  # Blue
    '\033[35m',  # Purple
    '\033[36m',  # Cyan
    '\033[91m',  # Light Red
    '\033[92m',  # Light Green
    '\033[93m',  # Light Yellow
    '\033[94m',  # Light Blue
    '\033[95m',  # Light Purple
    '\033[96m',  # Light Cyan
]


def colorize(txt):
    t = ''
    for i in txt:
        for j in printable:
            if txt == t:
                break
            
            os.system('cls')
            color = random.choice(colors)
            print(t+j+ color)
            # sleep(.05)
            if i == j:
                t += i+color


colorize('h3ll0 w0rld :)')