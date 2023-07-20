# exercise 2

file = open("teams.txt", "r")
lines = file.read()
file.close()

file = open("teams.txt", "w")
file.write("this is a new line\n")
file.write(lines)
file.close()

file = open("teams.txt", "r")
for line in file:
    print(line.strip())
file.close()

# exercise 1

file = open("teams.txt", "w")

for line in range(0,6):
    file.writelines(f"sports team {line} \n")

file.close()

file = open("teams.txt", "r")

line1 =file.readline()
# print(line1)

lines = file.readlines()


if len(lines) >= 4:
    print(f"The 1st team in the file is: {lines[0].strip()}")
    print(f"The 4th team in the file is: {lines[3].strip()}")
else:
    print("The file does not contain enough teams.")

file.close()

# tutorial

# file = open("filename.txt", "r")

# outfile = ""

# for line in range (1,10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()

# print(outfile)
