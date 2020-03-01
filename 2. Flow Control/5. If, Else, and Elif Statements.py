# if statement
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')
# Hi Alice
# Done
# if name is other than Alice than the output will beDone

# else statement
password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')
# If password is swordfish then output is Access granted but if not then the output is Wrong password

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
# Unlike you, Alice is not an undead, immortal vampire.

# Truthy and Falsey Values
print('Enter a name.')
name = input()
if name:  # better option would be to use name != ''
    print('Thank you for entering a name.')
else:
    print('You did not enter a name')
# Blank string is falsey all others are truthy
# for int 0 and 0.0 are falsey, all others are truthy

print(bool(0))  # False
print(bool(42))  # True
print(bool('Hello'))  # True
print(bool(''))  # False

# Resources
# https://automatetheboringstuff.com/chapter2/
# http://pythontutor.com/
