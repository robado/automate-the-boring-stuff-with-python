# This Program sasy hello and asks for my name

print('Hello World')

print('What is your name?')  # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The lenght of your name is:')
print(len(myName))

print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

#
#
#
#

print(len('Al'))  # 2
print(len('albert'))  # 6
print(len('Al') * 10)  # 20
print(str(26))  # 26
print(int('1234'))  # 1234
print(float(1))  # 1.0
# input function always returns string value
print(int('26') + 1)  # 27
# print(27 + ' years old') # gives error

# Recourse
# https://automatetheboringstuff.com/eval/3-1.html
# https://automatetheboringstuff.com/eval/3-2.html
# https://automatetheboringstuff.com/eval/3-3.html
# https://automatetheboringstuff.com/eval/3-4.html
