import os
import urllib.request

dia = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
noche = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/wn/'
img_dir = './img/'
if not os.path.exists(img_dir):
	os.makedirs(img_dir)

# Obtener los iconos del dia
for name in day:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

# Obtener los iconos de la noche
for name in night:
	file_name = img_dir+name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

