# Python collections exercise
author_name = input("Enter author name: ")

book_dict = {
    "Marijn Haverbeke": ["Eloquent JavaScript, Third Edition", "Practical Modern JavaScript", "Understanding ECMAScript 6"]
}

if author_name in book_dict:
    book_list = book_dict[author_name]
    book_string = ', '.join(book_list)
    print(book_string)
else:
    print("Author not found in the database.")




# collections tutorial

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaiden's Tale"])
# print(books["Margaret Atwood"])


# collections

list = ["meat", "veg", "fruit"]
tuple = ("fruit","veg")
dictitems= {"name":"Pam", "cool": True}


# integers and floats
number1 = input("enter whole number: ")
number2 = input("enter decimal number: ")

integer_number = int(number1)
float_number= float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# boolean
name="Pep Guardogiola"
age=3
bark=True
tweet=False

print("My pet is called", name, ", He is", age, "years old.")
print("statement:", name, "barks.", bark)
print("statement:", name, "tweets.", tweet)