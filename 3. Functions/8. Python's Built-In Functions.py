# Python 3
# Standard Library

# Modules have to be imported
import math
import os
import pyperclip
import sys
from random import *
import random

print(random.randint(1, 10))

# Modules have to be called
# Many modules can be imported

# * means it imports every random modules

# How to stop program
# sys.exit()

print('Hello')
# sys.exit()
print('Goodbye')  # This will never be reached because of sys.ext()

# Third party modules
# For example pyperclip whit which you can copy and paste text

pyperclip.copy('Hello world')
print(pyperclip.paste())


# Recources
# https://automatetheboringstuff.com/chapter3/
