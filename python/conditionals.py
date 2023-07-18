mark = input("enter the mark: ")

# not using elif
if float(mark) > 85:
    print("distinction")

if float(mark) > 65 and float(mark) <= 85:
    print("pass")

if float(mark) <= 65:
    print("fail")


# not using elif but nested
if float(mark) > 65:
    if float(mark) < 85:
        print ("pass")
    else:
        print ("distinction")
else:
    print ("fail")



# using elif
if float(mark) > 85:
    print("distinction")
elif float(mark) > 65 and float(mark) <= 85:
    print("pass")

else:
    print("fail")