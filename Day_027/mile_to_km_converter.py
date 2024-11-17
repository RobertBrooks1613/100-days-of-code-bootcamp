from tkinter import *

window = Tk()
window.minsize(width=300,height=100)
window.configure(padx=50,pady=20)



def calc_mile_to_km():
    get_miles = input_txt.get()
    label_km_result.config(text=round(eval(f"{get_miles} * 1.60934"),2))

#text input
input_txt = Entry(width=15)
input_txt.grid(column=1,row=0)

# Labels
label_is_equal = Label(text="Is equal to",font=("Arial",12,"bold"))
label_is_equal.grid(column=0,row=1)
label_km_result = Label(text="0",font=("Arial",12,"bold"))
label_km_result.grid(column=1,row=1)
label_miles = Label(text="Miles",font=("Arial",12,"bold"))
label_miles.grid(column=2,row=0)
label_km = Label(text="Km",font=("Arial",12,"bold"))
label_km.grid(column=2,row=1)

#Button
calc_button = Button(text="Calculate",width=10,font=("Arial",12,"bold"), command=calc_mile_to_km)
calc_button.grid(column=1,row=2)



window.mainloop()