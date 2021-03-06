import tkinter as tk
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import datetime
import json
import pycountry_convert as pc
import keyboard

app = tk.Tk()   #Para que todo este en una sola ventana

app.title('Aplicación del Clima')

alto = 500
ancho = 600

cuadro_mensaje = tk.messagebox.askquestion ('Ayuda','¿Querés ver el cuadro de ayuda?',icon = 'warning')
if cuadro_mensaje == 'yes':
    tk.messagebox.showinfo('Ayuda','Bienvenido a ClimaApp, aplicación desarrollada por Juan Ignacio Leiva.\n\nEn esta aplicación podes obtener los datos del clima actual de cualquier ciudad del mundo junto con una comparación entre la temperatura actual y la temperatura promedio de la estación actual del continente donde dicha ciudad está ubicada.\n\nLos datos de solicitud se pueden ingresar de dos maneras:\n1) Nombre ciudad, código de país de 2 dígitos (ISO 3166).\n2) Código postal de una ciudad, código de país de 2 dígitos (ISO 3166).')
else:
    tk.messagebox.showinfo('Regreso','Ahora volverás a la aplicación')

def format_response(weather_json):
    try:
        ciudad = weather_json['name']                                   #
        condiciones = weather_json['weather'][0]['description']         #
        temperatura = weather_json['main']['temp']                      #
        temperatura_max = weather_json['main']['temp_max']              #
        temperatura_min = weather_json['main']['temp_min']              #   
        presion = weather_json['main']['pressure']                      #   Obtención de los datos de la API
        humedad = weather_json['main']['humidity']                      #
        velocidad_viento = weather_json['wind']['speed']                #
        direccion_viento = weather_json['wind']['deg']                  #
        latitud = weather_json['coord']['lat']                          #
        longitud = weather_json['coord']['lon']                         #
    
        final_str = 'Ciudad: %s \nCondiciones: %s \nTemperatura: %sºC \nTemperatura máxima: %sºC \nTemperatura mínima: %sºC \nPresión atmosférica (hPa): %s \nHumedad: %s%% \nVelocidad del viento: %sm/s \nDirección del viento: %sº \nLatitud: %s \nLongitud: %s' % (ciudad, condiciones, temperatura, temperatura_max, temperatura_min, presion, humedad, velocidad_viento, direccion_viento, latitud, longitud)
    except:
        final_str = 'Los datos ingresados son incorrectos'
    return final_str

def obtenerDatos(city=None, zip_code=None):
    api_key1 = '6019371bb8ea6411b0b32d26b57d0670'
    api_url1 = 'https://api.openweathermap.org/data/2.5/weather'

    parametros = {'APPID': api_key1, 'q':city, 'zip':zip_code, 'units':'metric', 'lang':'es'}

    respuesta = requests.get(api_url1, parametros)
    print(respuesta.json())
    weather_json = respuesta.json()

    results['text'] = format_response(respuesta.json())

    nombre_icono = weather_json['weather'][0]['icon']
    abrirImagen(nombre_icono)

    temperatura = weather_json['main']['temp']
    presion = weather_json['main']['pressure']
    humedad = weather_json['main']['humidity']
    latitud = weather_json['coord']['lat']
    longitud = weather_json['coord']['lon']
    ciudad = weather_json['name']
    codigo_pais = weather_json['sys']['country']

def abrirImagen(icon):
    size = int(lower_frame.winfo_height()*0.35)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(1,0, anchor='nw', image=img)
    weather_icon.image = img

C = tk.Canvas(app, height=alto, width=ancho)    # Se define la ventana
background_image= tk.PhotoImage(file='./wallpaper.png')     #
background_label = tk.Label(app, image=background_image)    # Se define el fondo de la ventana
background_label.place(x=0, y=0, relwidth=1, relheight=1)   #

C.pack()

frame = tk.Frame(app,  bg='#eba80c', bd=5)                                  # Contorno del textbox
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')   #

textbox = tk.Entry(frame, font=('Bahnschrift', 15))     # Textbox
textbox.place(relwidth=0.65, relheight=1)               #

submit = tk.Button(frame, text='Ver clima', font=('Baloo Da 2', 15), command=lambda: obtenerDatos(textbox.get()))  # Botón de submit
submit.place(relx=0.7, relheight=1, relwidth=0.3)


app.bind("<Return>", lambda x: obtenerDatos(textbox.get()))  # Bind a la tecla Enter para que sirva como alternativa de clickear el botón Submit
                                                      

lower_frame = tk.Frame(app, bg='#eba80c', bd=10)                                    # Contorno del rectángulo inferior donde irá la información del clima
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')    #

bg_color = 'white'      # Color de fondo del textbox y el cuadro de información
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)  #
results.config(bg=bg_color, font=('Bahnschrift', 15))               # Fuente y formato de la información del clima
results.place(relwidth=1, relheight=1)                              #

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0) # Configuración del ícono del clima
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)            #





app.mainloop()  #Fin del código