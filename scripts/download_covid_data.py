#!/usr/bin/python

import requests

temp_file = open('data/datos_abiertos_covid19.zip', mode='wb')
chunk_size=128

covid_data_url = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'


response = requests.get(covid_data_url, stream=True)

print('Start COVID-19 data download')

for chunk in response.iter_content(chunk_size=chunk_size):
    temp_file.write(chunk)

temp_file.close()

print('Data downloaded!')
