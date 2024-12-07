from tkinter import *
import requests
kanye_quote = ''
BG_COLOR = "white"

def get_quote():
    global kanye_quote,quote_text
    try:
        quotes = requests.get(url="https://api.kanye.rest/")
    except Exception as error:
        kanye_quote = f"We ran into a problem. : {error}"
    else:
        data = quotes.json()
        kanye_quote = data["quote"]
        canvas.itemconfig(quote_text,text= kanye_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50,bg=BG_COLOR)

canvas = Canvas(width=300, height=414,bg=BG_COLOR,borderwidth=0,highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 22, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,borderwidth=0,bg=BG_COLOR)
kanye_button.grid(row=1, column=0)



window.mainloop()