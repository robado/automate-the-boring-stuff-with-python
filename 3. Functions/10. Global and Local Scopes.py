# Global and Local Scopes

# Global scopes are all outside functions
spam = 42  # Global variable


# Parameters and variables inside a functions are called local scope
def eggs():
    spam = 42  # local variableF


# Variable cant be both local and global


print('Some code here.')
print('Some more code')


# 1. Code in global - cannot use any local variables
# 2. Code in a local - can use global variables
# 3. Code in function's local scope cannot use variables in another local scope
# 4. Same name can be used - as long as the variable is not in the same scope

# 1
def spam1():
    eggs = 99


spam1()
# Print tries to call a variable from another scope
print(eggs)  # NameError: name 'eggs' is not defined


# 2
def spam2():
    # The program checks if there is no local variable then it checks if there is a global variable.
    # But is it a local or a global?
    # If there is an assigment statement eggs2 = 'Hello' - now it will print the local variable
    global eggs2  # Even if there is a local variable with global it will refer to a global variable
    eggs2 = 'Hello'
    print(eggs2)  # 42 | with local variable it prints 'Hello


eggs2 = 42
spam2()
print(eggs2)  # 42 <- this is a global variable


# 4
def spam4():
    eggs4 = 99
    bacon()
    # This will print spam()'s eggs and not bacon()'s eggs. 
    # Local scopes cannot use another's local scopes variables
    print(eggs)  # 99


def bacon():
    ham = 101
    eggs4 = 0


spam4()
print(eggs4)

# Resources
# https://automatetheboringstuff.com/ (pages - 67 -71)
