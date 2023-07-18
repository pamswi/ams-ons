mark = input("enter the mark: ")

# not using elif
if float(mark) > 85:
    print("distinction")

if float(mark) > 65 and float(mark) <= 85:
    print("pass")

if float(mark) <= 65:
    print("fail")



# using elif
if float(mark) > 85:
    print("distinction")
elif float(mark) > 65 and float(mark) <= 85:
    print("pass")

else:
    print("fail")