from tkinter import *
from tkinter import messagebox
import string
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

characters = string.ascii_letters + string.punctuation  + string.digits

def gen_pass():
	passw =  "".join(choice(characters) for _ in range(randint(8, 16)))
	#print(passw)
	
	pyperclip.copy(passw)
	pass_entry.insert(0, passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_inf():

	website = web_entry.get()
	email_username = email_username_entry.get()
	password = pass_entry.get()
	
	new_data = {
		website: {
			"Email": email_username,
			"Password": password
			}
	}
	
	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="OPPS!!!", message="Please make sure you haven't left any field empty.")
	else:
	
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?")
	
		if is_ok:
			try:
				with open("information_file.json", "r") as data_file:
					# Loading the json data file
					data = json.load(data_file)
			except FileNotFoundError:
				# If json data not found it will be created
				with open("information_file.json", "w") as data_file:
					json.dump(new_data, data_file, indent=4)
			else:
				data.update(new_data)
				
				with open("information_file.json", "w") as data_file:
					json.dump(data, data_file, indent=4)
			finally:
				web_entry.delete(0, END)
				email_username_entry.delete(0, END)
				pass_entry.delete(0, END)
				messagebox.showinfo(title="Success", message="Login Credentials Saved Successfully.")

#----------------------- Search Functionality-----------------#

def src_inf():
	website = web_entry.get()
	#print(website)
	try:
		with open("information_file.json", "r") as data_file:
						# Loading the json data file
						data = json.load(data_file)
						#print(data)
	except FileNotFoundError:
		messagebox.showinfo(title="Error!!!", message="No Data File Found.")
	else:
		if website in data:
			email = data[website]["Email"]
			password = data[website]["Password"]
			messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
		else:
			messagebox.showinfo(title="Error!!!", message=f"No Details found for {website}.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'example@email.com')

pass_label = Label(text="Password:", bg="white")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

pass_gen_btn = Button(text="Generate Password", bg="white", width=13, command=gen_pass)
pass_gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add Password", bg="white", command=save_inf)
add_btn.grid(row=4, column=1, columnspan=2)

src_btn = Button(text="Search", bg="white", command=src_inf)
src_btn.grid(row=1, column=2)





window.mainloop()
