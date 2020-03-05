# The List Data Type

# List contains many values

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
# With indexes you can pull the data out from a list
# https://automatetheboringstuff.com/eval/13-1.html
# https://automatetheboringstuff.com/eval/13-2.html
print(spam[0])  # cat
print(spam[1])  # bat
print(spam[2])  # rat
print(spam[3])  # elephant

# Lists can contain Lists
# https://automatetheboringstuff.com/eval/13-3.html
# https://automatetheboringstuff.com/eval/13-4.html
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# prints first list
print(spam[0])  # ['cat', 'bat']
# with second value it prints value from a lists list
print(spam[0][1])  # bat
# this gets the second list from the spam list
print(spam[1][4])  # 50

# Negative integers
# Negatives count from the end - backwards
# -1 last index, -2 second to last
spam = ['cat', 'bat', 'rat', 'elephant']
# prints the last value
print(spam[-1])  # elephant
# prints the second last value 
print(spam[-2])  # rat
# lists can be used in string concatination
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')  # The elephant is afraid of the bat.
# Slice can get many values
# This start from value 1 and goes up to 3 but does not include the value at index 3
print(spam[1:3])  # ['bat', 'rat']

# Changing a List's items
# An item in a list can be changed
spam = [10, 20, 30]  # [10, 20, 30]
# Specifying the index and a new value - the value will be changed in that list
spam[1] = 'Hello'
print(spam)  # [10, 'Hello', 30]
# This can also be done with slicing
# Now it will take the indexes from 1 to 3 and change then with new values
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)  # [10, 'CAT', 'DOG', 'MOUSE']
# Slicing
spam = ['cat', 'bat', 'rat', 'elephant']
# Start from beginning and go until next the specific index
print(spam[:2])  # ['cat', 'bat']
# Now it start from index 1 and continues until the end
print(spam[1:])  # ['bat', 'rat', 'elephant']

# del Statement
spam = ['cat', 'bat', 'rat', 'elephant']
# del will delete the specific index value
del spam[2]
print(spam)  # ['cat', 'bat', 'elephant']
# del wont leave a gap after deletion
del spam[2]
print(spam)  # ['cat', 'bat']

# String and List Similarities
# with len() it will show lenght of a list just like with string
print(len('Hello'))  # 5
print(len([1, 2, 3]))  # 3
# Lists can also be contatinated 
print('Hello ' + 'world')  # Hello world
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
# list replication
print('Hello' * 3)  # HelloHelloHello
print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Many things can be done with string can almost also be done with lists

# The list() function
print(list('Hello'))  # ['H', 'e', 'l', 'l', 'o']

# in and not in Operators
# With these operators a value can be checked that is it in a list or not
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])  # True
print(42 in ['hello', 'hi', 'howdy', 'heyas'])  # False
print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])  # False

# Resources
# https://automatetheboringstuff.com/ (pages 79-87)
