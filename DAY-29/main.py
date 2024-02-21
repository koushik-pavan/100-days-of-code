from tkinter import *
from tkinter import messagebox
import random
import json
#----------------------------- SEARCH FUNCTIONALITY ----------------------------- #
def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        messagebox.showinfo(title="error", message="Data File Not Found")
    else:
        website = website_entry.get()
        if website in data.keys():
            email = data[website]["email"]
            passkey = data[website]["password"]
            disp = f"email:{email} \n password:{passkey}"
            messagebox.showinfo(title="your details", message=disp)
        else:
            messagebox.showinfo(title="error", message="No such entry found")
    finally:
        website_entry.delete(0, END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list_let = [random.choice(letters) for char in range(nr_letters)]
    password_list_sym = [random.choice(symbols) for char in range(nr_symbols)]
    password_list_num = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_list_num+password_list_sym+password_list_let
    #print(password_list)

    random.shuffle(password_list)
    #print(password_list)
    password = ""
    for char in password_list:
      password += char
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    website = website_entry.get()
    username = email_entry.get()
    pwd = pass_entry.get()
    new_data = {
        website: {
            "email" : username,
            "password" : pwd
        }
    }
    if len(website)!=0 or len(pwd)!=0:
        is_ok = messagebox.askyesno(title="saving entry", message="your entry is being added")
        if is_ok:
            try:
                with open(r"data.json", "r") as f:
                    data = json.load(f)
                    data.update(new_data)
            except:
                with open(r"data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open(r"data.json", "w") as f:
                    json.dump(data, f, indent=4)
                #entry = f"{website} | {username} | {pwd} \n"
                #f.writelines(entry)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
    else:
        messagebox.showinfo(title="error", message="missing entries")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file=r"C:\Users\koush\PycharmProjects\days100code\DAY-29\logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)
#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
#entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width= 40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "koushikvaddadi@gmail.com")
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)
#buttons
generate_button = Button(text="Generate Password", command=pwd_gen)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add", width=36, command=save_pwd)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command = find_password)
search_button.grid(row=1, column=2)
window.mainloop()