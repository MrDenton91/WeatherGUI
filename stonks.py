import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import font

#e727ce63fb9997d47742794bd1bfed8e api key
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

HEIGHT = 700
WIDTH =800

def format_response(weather):
    try:

        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature: %s' %(name,desc,temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def get_stonks(city):
    weather_key = 'e727ce63fb9997d47742794bd1bfed8e'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)
    

root = tk.Tk()

#window dimmesions
canvas = tk.Canvas(root, height = HEIGHT , width =WIDTH)
canvas.pack()

# needed
background_image = tk.PhotoImage(file= /'background.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg ='#422E94', bd =5)
frame.place(relx = .5, rely = .1, relwidth=.75, relheight=.1, anchor = 'n')

entry = tk.Entry(frame, bg ='white', font =40)
entry.place(relwidth =.65, relheight= 1)

button =tk.Button(frame, text = 'Get Stonks', font = 40, command=lambda : get_stonks(entry.get()))
button.place(relx = 0.7, relwidth=.3, relheight =1)

lower_frame = tk.Frame(root, bg ='#422E94', bd =7)
lower_frame.place(relx=.5,rely =.25, relwidth=0.75, relheight=.6, anchor ='n')



label = tk.Label(lower_frame, font =('Modern', 20), anchor = 'nw', justify ='left', bd=4)
label.place(relwidth =1, relheight=1)


root.mainloop()