# Creating own Functions

# Functions = mini-program in the program. It executes code when a program is runed
# Function main point is to get rid of duplicate code!


def hello():  # Defining function
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


hello()  # Only now the function us runned
hello()  # Only now the function us runned
hello()  # Only now the function us runned


# Function makes code be reusable - without functions the code would probably be messing and repeatable.
# De-duplicating - getting rid of duplicated or copied code


def hello(name):  # Now using parameter
    print('Hello ' + name)


# Now we can pass values (arguments) to variable (parameter).
hello('Alice')  # Hello Alice
hello('Bob')  # Hello Bob

print('Hello has ' + str(len('hello')) + ' letters in it.')


# https://automatetheboringstuff.com/eval/9-1.html <- step by step the above code.

# Return value return the specific value it does inside the function. In the below function it gets the value from
# variable and adds 1 to it and returns the "sum" of it.


def plusOne(number):
    return number + 1


newNumber = plusOne(5)
print(newNumber)  # 6

# Non value
'Hello'  # 'Hello'
print('Hello')  # Hello

spam = print()
spam
spam == None
print(spam)  # True
# Every function call has a return value!


# Keyword arguments
print('Hello', end='')  # removes newline
print('World')

# cat dog mouse <- adds a space character automatically
print('cat', 'dog', 'mouse')

# Now it will add ABC in between the words
print('cat', 'dog', 'mouse', sep='ABC')  # catABCdogABCmouse

# Resources
# https://automatetheboringstuff.com/ (pages 61-66)
# https://automatetheboringstuff.com/eval/9-1.html
