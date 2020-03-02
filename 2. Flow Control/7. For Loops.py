# For Loops
# For loop iterates for a specific number of times

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

'''My name is
Jimmy Five Times 0
Jimmy Five Times 1
Jimmy Five Times 2
Jimmy Five Times 3
Jimmy Five Times 4'''
# The code is run 5 times.

# Carl Friendrich Gauss
total = 0
for num in range(101):
    total = total + num
print(total)  # 5050

# while Loop Equivalent of a for Loop
print('My name is')
while i < 5:
    # for i in range(5):
    print('Jimmy Five Times ' + str(i))
    i = i + 1

# For is a bid shorter to write

print('My name is')
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

# Range with two arguments = it will start from the first argument and the second is where it ends. Three arguments are also possible, then the last is a 'step argument' it is how much the argument will increase on every iteration.

print('My name is')
for i in range(0, 10, 2):
    print('Jimmy Five Times ' + str(i))

# Range third argument can also be negative - then it will count down.
print('My name is')
for i in range(10, -1, -1):
    print('Jimmy Five Times ' + str(i))

# for loops are used when you want to loop a specific number of times.

# Resources
# https://automatetheboringstuff.com/
# http://pythontutor.com/
