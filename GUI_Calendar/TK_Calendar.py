from tkinter import *
from tkcalendar import *
from datetime import datetime

#Today's Information
t_date = datetime.now()
year = t_date.year
month_str = t_date.strftime("%B")
month = t_date.month
day = t_date.day
w_day = t_date.strftime("%A")

print(f"{year} {month} {day} {w_day}")

window = Tk()
window.geometry("400x300")
window.title(f"{w_day} - {day} - {month} - {year}")

cldr = Calendar(window, year=year, month=month, day=day)
cldr.pack(pady=30)

window.mainloop()
