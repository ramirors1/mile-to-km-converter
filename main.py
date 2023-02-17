from tkinter import *  # import every class within tkinter

window = Tk()  # used when importing all classes from tkinter
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    miles = input.get()
    my_label.config(km)

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609344)
    km_result.config(text=f"{km}")

# Entry component
input = Entry(width=7)
input.grid(column=1, row=0)


# Label
miles_label = Label(text="Miles", font=("Arial", 15, "italic"))  #used when importing all classes of tkinter
miles_label.grid(column=2, row=0)  # uses grid format to place items

equal = Label(text="is equal to", font=("Arial", 15, "italic"))
equal.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 15, "italic"))
km_label.grid(column=2, row=1)

# Buttons
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()  # keeps the window on the screen