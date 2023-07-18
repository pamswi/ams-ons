# iteration exercise
i = 0
names = []

while i < 5:
    name = str(input("name: "))
    names.append(name)
    i += 1

i = 0
while i < 5:
    print(names[i] + " is awesome")
    i += 1

# work out what this for loop does:
for i in range(10, 21, 2):
    print(i)
# the loop prints values between 10 and 21 that are even (dividable by 2)



# while loop
count = 4

name = str(input("what's your name?: "))

while count < 5:
    print(name, "is awesome")
    count += 1


# for loop
for i in range(5,11):
    print(i)