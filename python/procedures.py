# procedures and functions

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

# def fourcandles(noofcandles):
#     candlelist= []
#     for i in range(noofcandles):
#         candlelist.append("candle")
#     return candlelist


# noofcandles=int(input("provide a number: "))
# returnlist=fourcandles(noofcandles)
# print(returnlist)