from tkinter import *
from tkinter import font
import tkinter.messagebox as box
import matplotlib.pyplot as plt
import pandas as pd
import time

window = Tk()

window.title('Covid Project')
window.geometry("500x200")
window.config(bg="white")
label_font = font.Font(family="Roboto Mono", size=12)
label = Label(window, text="Enter A Country Your Interested In", font=label_font)
frame = Frame(window)
entry = Entry(frame)


# Submit Button Clicked
def get_country_button_click():
    url_dataset = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
    df1 = pd.read_csv(url_dataset)
    if len(entry.get()) == 0:
        error_label = Label(window, text="Input cannot be empty")
        error_label.pack()
    else:
        df_country = df1[df1['Country'] == entry.get()]
        values = df_country.tail(1)
        country_name = Label(window, text=entry.get())
        query_output_label = Label(window, text=values, font=label_font)
        country_name.pack()
        query_output_label.pack()


# Using keyboard
def keyboard_enter_button_clicked(event):
    url_dataset = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
    df1 = pd.read_csv(url_dataset)
    if len(entry.get()) == 0:
        error_label = Label(window, text="Input cannot be empty")
        error_label.pack()
    else:
        df_country = df1[df1['Country'] == entry.get()]
        values = df_country.tail(1)
        country_name = Label(window, text="Country Requested: " + entry.get())
        query_output_label = Label(window, text=values)
        country_name.pack()
        query_output_label.pack()


submit_btn = Button(frame, text="Submit", command=get_country_button_click)
label.pack(side=TOP, padx=10)
submit_btn.pack(side=RIGHT, padx=5)
entry.pack(side=LEFT)
frame.pack(padx=20, pady=20)

window.bind('<Return>', keyboard_enter_button_clicked)
window.mainloop()
