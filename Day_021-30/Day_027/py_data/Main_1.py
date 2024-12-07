# import tkinter
# import random
# from tkinter import Entry
#
# window = tkinter.Tk()
# image = tkinter.PhotoImage(file="thumb-1920-736461.png")
#
# bg_color = "lightgrey"
# funny_lines = [
#     "Why don't scientists trust atoms? \nBecause they make up everything!",
#     "I told my computer I needed a break, \nand now it won't stop sending me Kit-Kats.",
#     "Why do programmers prefer dark mode? \nBecause light attracts bugs!",
#     "Why was the math book sad? \nIt had too many problems.",
#     "Why do Java developers wear glasses? \nBecause they don't C#.",
#     "Why did the scarecrow become a successful software engineer? \nBecause he was outstanding in his field!",
#     "Why do fish never do well in school? \nBecause they're always swimming below 'C' level.",
#     "Why did the computer go to the doctor? \nBecause it had a virus!",
#     "Why was the cell phone wearing glasses? \nIt lost its contacts.",
#     "Why did the programmer quit his job? \nBecause he didn't get arrays."
# ]
#
# window.title("My First GUI Project")
# window.minsize(width=800,height=500)
# window.configure(background=bg_color)
#
#
#
# def on_click():
#     my_label.config(text=random.choice(funny_lines))
# def text_input():
#     my_label2.config(text=txt_input.get())
#
# # Frame
# frame = tkinter.Frame(bg=bg_color)
# frame.grid(row=0,column=0)
# frame2 = tkinter.Frame(bg=bg_color)
# frame2.grid(column=1,row=0)
#
# #Label
# my_label = tkinter.Label(frame, text="Hi im a label!!",font=("Arial",12,"bold"),bg=bg_color,fg="black",height=5,width=40)
# my_label.pack()
# # Label 2
# my_label2 = tkinter.Label(frame2, text="Label 2", font=("Arial", 16, "bold"), bg=bg_color,height=5,width=20,wraplength=250)
# my_label2.pack()
#
#
# # Button
# button = tkinter.Button(frame,text="Tell me a Joke!",bg=bg_color, command=on_click,font=("Arial",16,"bold"),fg="black")
# button.pack(side="left")
# button2 = tkinter.Button(frame, text="Not Funny..", bg=bg_color,font=("Arial",16,"bold"),fg="black",command=on_click)
# button2.pack(side="right")
#
# # txt input
# txt_input = tkinter.Entry(frame2, width=20)
# txt_input.bind("<Return>", lambda event:[text_input(),txt_input.delete(0,"end")])
# txt_input.pack()
#
# # Text multi lines
# text_box = tkinter.Text(height=5,width=30)
# text_box.focus()
# text_box.insert("end","Example of multi-line \ntext entry : ")
#
# # spin box
# spin_box = tkinter.Spinbox(frame2,from_=0,to=10,width=5)
# spin_box.pack()
#
# #scale
# scale = tkinter.Scale(from_=0, to=100,width=10,length=300,bg=bg_color)
# scale.grid(column=3,row=0)
#
#
#
print(f"")
#
#
#
# window.mainloop()
