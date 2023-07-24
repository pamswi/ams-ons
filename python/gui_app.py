# Task: Create a simple file reader which displays file contents in a gui window using TKinter

# import tkinter module
import tkinter

# function to open and read files
def read_file():
  thepath = thepath_entry.get()
  f = open(thepath, "r")
  lines = f.read()

  # create a new window to display the file contents
  display_window = tkinter.Toplevel(root)
  display_window.title("File Contents")

  # Create a text widget inside the new window to show the file contents
  text_widget = tkinter.Text(display_window)
  text_widget.insert(tkinter.END, lines)
  text_widget.pack()


# initialises window
root = tkinter.Tk()

label = tkinter.Label(root, text= "enter the file path: ")
thepath_entry = tkinter.Entry(root)
thepath_entry.grid(row=1,column=1)

submit = tkinter.Button(root, text="print text", command=read_file)
submit.grid(row=1, column=2)

# displays window
if __name__ == '__main__':
    root.mainloop()

    ##check 


