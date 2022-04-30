from tkinter import *
from tkinter import filedialog
lis=[]
def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File",filetypes=(("Text files",".txt"),("all files",".")))
    l1 = Label(window, text = "File path: " + file_path).pack()
    lis.append(file_path)

window = Tk()
window.geometry('250x250')
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2 = Button(window, text = "Open File", command = get_file_path).pack()
window.mainloop()
print(lis)


