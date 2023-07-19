# debugging exercises

import pdb
pdb.set_trace()

#  exercise 1

user_funds = 10.31
price = {
    "Burger": 5.99,
    "Fries": 2.49,
    "Drink": 1.99
}
item_price = price["Burger"] # price??

if item_price < user_funds:
    print("You have enough money!") # should be "print"
if item_price == user_funds: # should be ==
    print("You have the precise amount of money")
if item_price > user_funds: # conflicts first if statement, should be ">"
    print("Sorry you don't have enough money") # string should be in ""

# exercise 2

def product(numbers): # previously single input
    total = 1 # single " ="
    for i in numbers: # wrong iteration
        total *= i
    return total # indentation

print(product([4, 4, 5]))

# exercise 3

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True # indentation
    
# Example usage:
num = 15
result = is_prime(num)
print(f"{num} is prime: {result}")



