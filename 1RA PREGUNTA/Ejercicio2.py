# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:20:09 2021

@author: IBM GAMER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos=pd.read_csv(r'train.csv')
#matriz=datos.to_numpy()
media=datos.mean()
mediana=datos.median()
moda=datos.mode()
desviacion=datos.std(ddof=0)
print (media,'\n')
print (mediana,'\n')
print (moda,'\n')
print(desviacion)

df = pd.DataFrame(datos, columns= ['price_range ','battery_power'])

#GRAFICAR LOS DATOS (CONTEO)
x_values = datos['battery_power'].unique()
y_values = datos['battery_power'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.show()
plt.title('Capacidad de bateria')
plt.close('all')

x_values = datos['blue'].unique()
y_values = datos['blue'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('bluetho')
plt.show()
plt.close('all')

x_values = datos['clock_speed'].unique()
y_values = datos['clock_speed'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('velocidad de procesamiento')
plt.show()
plt.close('all')

x_values = datos['int_memory'].unique()
y_values = datos['int_memory'].value_counts().tolist()
plt.bar(x_values, y_values)
plt.title('Memoria del dispositivo')
plt.show()
plt.close('all')

# En los anteriores graficos vistos se ve como barras el conteo de 4 atributos del data set



x_values = datos['ram']
y_values = datos['int_memory']
plt.plot(x_values, y_values,'x')
plt.title('ram vs memoria interna')
plt.show()
plt.close('all')


x_values = datos['n_cores']
y_values = datos['ram']
plt.plot(x_values, y_values,'x')
plt.title('numero de nucleos vs ram')
plt.show()
plt.close('all')

x_values = datos['ram']
y_values = datos['pc']
plt.plot(x_values, y_values,'x')
plt.title('ram vs megapixeles')
plt.show()
plt.close('all')
