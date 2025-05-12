import math
import random
import sys
import random as rds
from enum import Enum

from math import pi

# print(pi)
#
# print(math.pi.__sizeof__())
# print(rds.choice('1234'))
# print(dir(rds)) #print all functions in random
# for item in dir(rds):
#     print(item)

import random
from random import choice
birds = 'eagle'
capital = 'mysore'
flower = 'SunFlower'
song = 'Thunder from Imagine Dragons'


def random_funfacts():
    funfacts = [
        "Eagles have incredible eyesight—up to 8 times stronger than humans! They can spot prey from over 2 miles (3.2 km) away",
        "Sunflowers can track the sun! Young sunflowers exhibit a behavior called heliotropism, where they turn their heads to follow the sun from east to west during the day",
        "Mysore is home to one of the most opulent palaces in India—Mysore Palace—which attracts more visitors annually than even the Taj Mahal",
        "Thunder by Imagine Dragons was inspired by the band's journey from rejection to success—it's a celebration of breaking free from the norm and chasing dreams."
    ]

    index = choice("0123")
    print(funfacts[int(index)])


# random_funfacts()


if __name__ == "__main__":
    random_funfacts()
    print(birds)
