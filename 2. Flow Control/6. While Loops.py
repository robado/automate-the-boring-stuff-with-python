# While loops
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1

# Will loop as long as the statement is false

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you')

# Continue asking your input as long as you give 'you name'.

# Infinite Loops
while True:
    print('Hello')

# This will go infinite

# break Statement breaks the program
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')

# Same as before but ends loop with a break

# continue Statement
# Jumps back jumps back to the loop and re-evaluate

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Spam is ' + str(spam))

# Spam is 1
# Spam is 2
# Spam is 4
# Spam is 5
# Spam is 3 is missing because when it comes to 3 it jumps to the beginning of the program and start again.

# Resources
# https://automatetheboringstuff.com/
# http://pythontutor.com/
