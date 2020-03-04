# Try and Except Statements

# When errors happens, you don't want to program just stop - you want to handle them and continue program


def div42by(dividedBy):
    return 42 / dividedBy


print(div42by(2))
print(div42by(12))
print(div42by(0))  # ZeroDivisionError: division by zero
# This will never be executed because of the error
print(div42by(1))

# Computers don't know how to handle zeroes
print(40 / 0)


# try and except Statement


def div42by_2(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:  # You dont have to specify the except.
        print('Error: You tried to divide by zero.')


print(div42by_2(2))
print(div42by_2(12))
# This time all of the calls be executed even when divided with 0.
# This is because now when the error happens it goes to except claus.
# This makes program to run without failing.
print(div42by_2(0))  # Error: You tried to divide by zero.
# None
print(div42by_2(1))

# Input Validation
print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')

# This program works if you input a number. But what if you input a string?
# If you would insert a string it could give the following error ->
# ValueError: invalid literal for int() with base 10: 'six'
# This is happening because the input waits for a numeric digits.

# Now if a user enters a string it will give a more tidier error -> You did not enter a number. <- and basically the
# program can keep running after that fo example if you would have a while loop.
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')

# Resources
# https://automatetheboringstuff.com/ (pages 72 - 73)
