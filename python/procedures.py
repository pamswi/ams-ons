# procedures and functions

# https://www.w3resource.com/python-exercises/python-functions-exercises.php


# Write a Python program to print the even numbers from a given list.
def even_numbers(input):
    result_list = []
    for i in input:
        if i % 2 == 0:
            result_list.append(i)
    return result_list

input = [1,2,3,4,5,6,7,8,9]
print(input)
print(f"{even_numbers(input)}")


# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n < 2:
        return False
    else:
        for x in range(2, n-1):
            if n % x == 0:
                return False
        return True # indentation
    
# example usage:
num = 3
result = is_prime(num)
print(f"{num} is prime: {result}")

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def list_check(l):
    unique_list = []

    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

l= [1,2,3,4,4,5,5,6,6,6,6]
print(l)
print(list_check(l))


# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def analyse_string(input):
    lower=0
    upper=0
    for i in input:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    return lower, upper


input=input("please enter a string: ")
print(f"the number of lowercase characters is: {analyse_string(input)[0]}")
print(f"the number of uppercase characters is: {analyse_string(input)[1]}")



# Write a Python function to check whether a number falls within a given range.
def testrange(number):
    if number in range(1,10):
        print(f"{number} is in the range")
    else:
        print("the number is not in the range")

testrange(100)

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    if (n==1 or n==0):
        return True
    else:
       result= n * factorial(n-1)
    return result

num =5
print(f"factorial of {num} is {factorial(num)}")

# Write a Python program to reverse a string.

def reversestring(string):
    result=string[::-1]
    return result

input=input("please input a string: ")
output=reversestring(input)
print(f"your reversed input is: {output}")

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result

numbers = []

for i in range(5):
    number = int(input("enter a number: "))
    numbers.append(number)
    i = i +1

mult = multiply(numbers)
print(f"the total is: {mult}")


# Write a Python function to sum all the numbers in a list.
def adding(numbers):
    
    numbers=sum(numbers)
    return numbers

numbers=8,2,3,0,7
newsum=adding(numbers)
print(newsum)

# Write a Python function to find the maximum of three numbers.

def maxno(var1,var2,var3):
    biggestno = max(int(var1),int(var2),int(var3))
    return biggestno

var1 = input("please enter a number: ")
var2 = input("please enter a number: ")
var3 = input("please enter a number: ")

biggestnumber = maxno(var1,var2,var3)
print(f"the biggest no is: {biggestnumber}")

# tutorial

def grade(homework, assessment, exam):
    totalscore = int(homework) + int(assessment) + int(exam)
    maxscore = 25 + 50 + 100
    finalgrade = (totalscore / maxscore) * 100

    return finalgrade


name = input("Enter your name: ")
homework = input("Enter your homework score (0-25): ")
assessment = input("Enter your assessment score (0-50): ")
exam = input("Enter your final exam score (0-100): ")

ICTgrade = grade(homework, assessment, exam)
ICTgrade = round(ICTgrade)
print(f"{name}, your final score is: {ICTgrade}%")

# exercise
def add_cal(number1, number2):
    answer = number1 +number2
    return answer

added_number = add_cal(5,5)
print(added_number + 20)

