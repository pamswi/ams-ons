# procedures and functions
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
# def add_cal(number1, number2):
#     answer = number1 +number2
#     return answer

# added_number = add_cal(5,5)
# print(added_number + 20)

# def fourcandles(noofcandles):
#     candlelist= []
#     for i in range(noofcandles):
#         candlelist.append("candle")
#     return candlelist


# noofcandles=int(input("provide a number: "))
# returnlist=fourcandles(noofcandles)
# print(returnlist)