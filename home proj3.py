from tkinter import *
root = Tk()
root.title("ascii")
root.geometry("400x400")
root.configure(background = "blue")

EnterWord = Entry(root)
EnterWord.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label = Label(root, text = "ASCII value ", bg = "white", fg = "black")

def AsciiConverter():
    InputWord = EnterWord.get()
    
    for letter in InputWord:
        label["text"] += str(ord(letter)) + ""
        
btn = Button(root, text = "convert to ascii ", command = AsciiConverter, bg = "red", fg = "white")
btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)  

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)  
        
        
        

root.mainloop()