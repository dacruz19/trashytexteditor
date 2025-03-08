import customtkinter as ctk
from customtkinter import filedialog
import tkinter
from tkinter import messagebox

class TextEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Dacruz Text Editor")
        self.create()
    
    def create_txt(self,text):
        create = filedialog.asksaveasfile(defaultextension=".txt")
        create.write(str(text))
        create.close()
        messagebox.Message("Created File")
    
    def open_txt(self):
        filze = filedialog.askopenfilename()
        filzez = open(filze, "r")
        z = filzez.read()
        self.entry.delete("0.0","end")
        self.entry.insert(ctk.END,text=z)
        filzez.close()
        messagebox.Message("Opened File")

    def create(self):
        z = ctk.CTkFont (family="Helvetica",size=20)
        self.entry = ctk.CTkTextbox(master=self, fg_color='black', text_color='white', font=z)
        self.frame = ctk.CTkFrame(master= self, fg_color='black', height=40)
        self.button = ctk.CTkButton(master= self.frame, command=lambda: self.create_txt(self.entry.get("0.0", "end")), text="Save As", fg_color='dark blue')
        self.button2 = ctk.CTkButton(master= self.frame, command=lambda: self.open_txt(), text="Open File",fg_color='dark blue')
        
        self.button.pack(side='left',)
        self.button2.pack(side='left')
        self.entry.pack(side='bottom',fill='both',padx= 10,pady = 10, expand = True)
        self.frame.pack(side='top', fill='x', padx=10,pady=10)
    
cd = TextEditor()
cd.configure(fg_color="dark blue") 
cd.mainloop()
