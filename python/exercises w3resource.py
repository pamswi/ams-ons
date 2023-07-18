import random

# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

numbers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(i)

print(numbers)

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

temp = int(input("Enter temperature: "))
fc = input("Fahrenheit or Celsius: ")

if fc == "Fahrenheit":
    newtemp = (temp - 32) * 5/9
    print(f"{temp}°F is {newtemp}°C")
elif fc == "Celsius":
    newtemp = (temp * 9/5) + 32
    print(f"{temp}°C is {newtemp}°F")

# 3. Write a Python program to guess a number between 1 and 9.
 
randomnumber = random.randrange(1, 10)

while True:
    guess = input("enter a random number between 1 and 9: ")
    print(randomnumber)
    if int(guess) == randomnumber:
        print("Well guessed!")
        break
    else:
        print("Try again!")


