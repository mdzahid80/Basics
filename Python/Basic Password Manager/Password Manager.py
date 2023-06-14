from tkinter import *
from tkinter import messagebox
import random
import json
# # ---------------------------- Password Search ------------------------------- #
def find_pswd():
    website=wbsite_dt.get()
    try:
        with open("data_pass_mngr.json", mode="r") as data_file:
            data=json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message= f"no data file found")
        
    else:
        if website in data:    
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="Your Credentials",message= f"{email}\n {password}")
        else:
            messagebox.showinfo(title="Your Credentials Not Available",message= f"NO details for the following website")
                
    



# # ---------------------------- Password generator ------------------------------- #

def gen_pass():
    pswrd_dt.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list=password_letter+password_numbers+password_symbols
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char  #alternate:-

    password="".join(password_list)

    pswrd_dt.insert(0, password)
# ---------------------------- Saving Data in a File ------------------------------- #

def save_data():

    website = wbsite_dt.get()
    email = usrnm_dt.get()
    password = pswrd_dt.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Empty field",message=" Fields can't be empty")
    else:
        try:
            with open("data_pass_mngr.json", "r") as data_file:
            #    read old data
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data_pass_mngr.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
                
        else:
            #update new data
            data.update(new_data)

            with open("data_pass_mngr.json", "w") as data_file:
            #    save updated data
                json.dump(data, data_file,indent=4)

        
    wbsite_dt.delete(0, END)
    usrnm_dt.delete(0, END)
    pswrd_dt.delete(0, END)

    


# ---------------------------- UI SETUP ------------------------------- #
Window=Tk()
Window.title("Password Manager")
Window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(row=0,column=1)

wbsite=Label(text="Website")
wbsite.grid(row=1,column=0)

usrnm=Label(text="Email/Username")
usrnm.grid(row=2,column=0)

pswrd=Label(text="Password")
pswrd.grid(row=3,column=0)


wbsite_dt=Entry(width=21)
wbsite_dt.grid(row=1,column=1,columnspan=1,sticky = 'w')

usrnm_dt=Entry(width=35)
usrnm_dt.grid(row=2,column=1,columnspan=2,sticky = 'w')

pswrd_dt=Entry(width=21)
pswrd_dt.grid(row=3,column=1,sticky = 'w')


srch=Button(text="Search",command=find_pswd)
srch.grid(row=1,column=2,sticky = 'w')

gnrt_pswd=Button(text="Generate Password",command=gen_pass)
gnrt_pswd.grid(row=3,column=2,sticky = 'w')

add=Button(text="Add",command=save_data, highlightthickness=0,width=36)
add.grid(row=4,column=0,columnspan=2)


Window.mainloop()