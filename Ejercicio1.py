# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:43:32 2021

@author: IBM GAMER
"""
# La media es el valor promedio de un conjunto de datos numéricos, 
# calculada como la suma del conjunto de valores dividida entre el número total de valores.
def media(matriz,nombres):
    sum=[0]*21
    cont=0
    for i in matriz:
        cont+=1
        for k in range (len(i)):
            sum[k]+=i[k]
    for j in range (len(sum)):
        print('La media de',nombres[j],'es:',sum[j]/cont)
# La desviación estándar es la medida de dispersión más común, 
# que indica qué tan dispersos están los datos con respecto a la media. 
# Mientras mayor sea la desviación estándar, mayor será la dispersión de los datos.
# Respecto a los datos se saco la desviacion estandar de cada uno de los atributos del dataset,
# para ver cuan dispersos estan los datos.
def desviacion(matriz,nombres):
    sum=[0]*21
    cont=0
    for i in matriz:
        cont+=1
        for k in range (len(i)):
            sum[k]+=i[k]
    desv=[0]*21
    sumas2=[0]*21
    for i in matriz:
        for k in range (len(i)):
            sumas2[k]+=(i[k]-(sum[k]/cont))**2
            
    for j in range (len(sumas2)):
        print('La desviacion estandar de',nombres[j],'es:',(sumas2[j]/cont)**0.5)
# La moda es el valor que aparece más dentro de un conglomerado. 
# En un grupo puede haber dos modas y se conoce como bimodal, 
# y más de dos modas o multimodal cuando se repiten más de dos valores; 
# se llama amodal cuando en un conglomerado no se repiten los valores.
# En el dataset se vio que algunos de los conjuntos de atributos son multimodales.
def moda(matriz,nombres):
    
    for i in range (len(matriz[1])):
        valores=[]
        contador=[]
        for j in range (len(matriz)):
            if matriz[j][i] in valores:
                index=valores.index(matriz[j][i])
                contador[index]+=1
            else:
                valores.append(matriz[j][i])
                contador.append(1)
        pos=0
        may=0
        for k in range(len(contador)):
            if may<contador[k]:
                may=contador[k]
                pos=k
        for k in range(len(contador)):
            if may==contador[k]:
                print("La moda de",nombres[i],'es:',valores[k])


    
file=open("train.csv",'r')
matriz=[]
nombres=file.readline().split(",")


for i in file:
    fila=i.replace('\n','')
    fila=list(map(float,fila.split(",")))
    matriz.append(fila)
file.close()

media(matriz, nombres)
moda(matriz, nombres)
desviacion(matriz, nombres)