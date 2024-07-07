import tkinter as tk
import random

Alphabets = list("qwertyuiopasdfghjklzxcvbnm") # Default
Alphabols = list("qwer!t@y#u$i^o&p*a(s)d_fgh[j}k]l{z:x;c.v,b<n>m/?") # Default + Symbols
Alphanumeric = list("qwer4ty7uiop50asdf1g8h6j9klz2xcv9b3nm") # Default + Digits
Alphagitbols = list("qwe12r!t@y#6u$i345^o&p*a(s)d_789fgh[j}k0]l{z:x;c.v,b<n>m/?") # All combine

# Program Window setup 
root = tk.Tk(__name__)

# Both CheckButtons Status ie. True / False
checkSymbols_boolean = tk.BooleanVar()
checkDigits_boolean = tk.BooleanVar()

# Core Geometries
root.geometry("500x300")
root.resizable(width=False,height=False)
root.title("Password Generator by Haseeb")

# All Widgets Definition
Heading = tk.Label(text="Password Generator",font=("Arial" ,18,"bold")) # Main headings
Result = tk.Text(root,width=30 ,height=2,font=("Arial","17","bold")) # Input field for generated Paassword
btn = tk.Button(root,text="Gen",command=lambda:gen(),width=10,height=1) # Button
checkSymbols = tk.Checkbutton(root,variable=checkSymbols_boolean,text="include special characters ($%@#) etc.") # checkbox for symbols selection
checkDigits = tk.Checkbutton(root,variable=checkDigits_boolean,text="include Digits (0-9)")# checkbox for digit selection

# All Widgets Placing
Heading.place(x=150,y=50)
Result.place(x=55,y=100)
btn.place(x=200,y=240)
checkSymbols.place(x=50,y=170)
checkDigits.place(x=50,y=190)


#  Main Logic to Generate Password
def gen():
    pswrd = [] # Generated Password Container 
    for i in range(0,8):
        rand = random.randint(0,25)
        if not checkSymbols_boolean.get() and not checkDigits_boolean.get():
            pswrd.append(Alphabets[rand])
        elif checkSymbols_boolean.get() and checkDigits_boolean.get():
                pswrd.append(Alphagitbols[rand])
        elif checkSymbols_boolean.get():
             pswrd.append(Alphabols[rand])
        else:
             pswrd.append(Alphanumeric[rand])

    Result.delete(1.0,tk.END) # Updating Input Field to delete previous residue 
    Result.insert(1.0,f'{"".join(pswrd)}') # Updating Input Field to insert new generated password 

# Prograam Window Session Controler
if __name__ == "__main__":
    root.mainloop()