from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("elements")
root.geometry("500x500")
root.configure(background="green")

class create_elements:
    def __init__(self):
        print("This is create elements class")
        
    def new_label(self):
        label=Label(root,text="Label created using class")
        label.pack()
    
    def new_button(self):
        btn=Button(root,text="button created using class",command=self.message)
        btn.pack()
        
    def message(self):
        messagebox.showinfo("Message","Click button creating using class")
        
        
obj1=create_elements()
btn2=Button(root,text="Click to create label", command=obj1.new_label)
btn2.place(relx=0.2,rely=0.9,anchor=CENTER)

obj2=create_elements()
btn3=Button(root,text="click to create button",command=obj2.new_button)
btn3.place(relx=0.8,rely=0.9,anchor=CENTER)
root.mainloop()


