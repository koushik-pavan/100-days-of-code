from tkinter import *

window = Tk()
#window.minsize(width=300, height=300)
window.title("Mile to Km Converter")
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)
mile_entry = Entry()
mile_entry.grid(column=1, row=0)
label_answer = Label(text="0")
label_answer.grid(column=1, row=1)
label_km = Label(text="Km").grid(row=1, column=2)
def calci():
    miles = mile_entry.get()
    kilometres = int(miles)*1.6094
    label_answer.config(text=kilometres)
button = Button(text="Calculate", command=calci).grid(row=2, column=1)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

window.mainloop()

