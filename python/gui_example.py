import tkinter

def strip_vowels():
	global label
	label.destroy()
	string = input1.get()
	label = tkinter.Label(root, text = ''.join(char for char in string if char not in 'aeiouAEIOU'))
	label.grid(row=2,column=1)


# initialises window
root = tkinter.Tk()

label = tkinter.Label(root, text = "Hello World!")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1) # or label.pack()

submit = tkinter.Button(root, text = "strip vowels", command=strip_vowels)
submit.grid(row=1, column=2)

# displays window
if __name__ == '__main__':
	root.mainloop()