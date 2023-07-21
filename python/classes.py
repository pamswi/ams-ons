# tutorial and exercise
class Student:

    def __init__(self, name, age, class_name="student"):
        self.name = name
        self.age = age
        self.class_name = class_name

    def avg_score(self, score1,score2,score3):
        avgs=(score1+score2+score3)/3
        return avgs


Pam = Student("Pam",  "28")

Sam = Student("Sam", "22")
print(Pam.avg_score(50,50,70))


#print(getattr(Sam, "age"))
# print(Pam.class_name)
