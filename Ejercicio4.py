# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:46:58 2021

@author: IBM GAMER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn import preprocessing

datos=pd.read_csv(r'train.csv')

X_inicial= datos.to_numpy()


#Preprocesamiento
imp = SimpleImputer(missing_values=np.NaN, strategy='mean')
X_salida=imp.fit_transform(X_inicial)
Aprepro = preprocessing.normalize(X_salida)
Aprepro = preprocessing.scale(Aprepro)
aux1=Aprepro
#print(Aprepro)
X=np.delete(aux1, 20, axis=1)
#print(len(X[1]))
#y=np.delete(Aprepro, np.arange(20), axis=1)
y=np.delete(X_inicial,np.arange(20), axis=1)
#print(len(y[1]))
#print(y)

from sklearn import tree
clasificador = tree.DecisionTreeClassifier(criterion='entropy')
clasificador.fit(X, y)

#Datos prueba
#yp=pd.read_csv(r'test.csv')
#yp=datos.to_numpy()
#yp=np.delete(yp, 0, axis=1)

#print(len(yp[1]))
from sklearn import model_selection 
from sklearn.metrics import confusion_matrix

X_train, X_test, y_train, y_test = model_selection.train_test_split( X, y, test_size=0.33)

clasificador.fit(X_train, y_train)
print(len(X_train),len(X_test))
prediccion = clasificador.predict(X_test)
print(prediccion)
print()
print(confusion_matrix( y_test, prediccion))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('\nExactitud: {:.2f}\n'.format(accuracy_score(y_test, prediccion)))

#Realizamos 10 veces las pruebas


from sklearn.metrics import classification_report
print ( ' \n Informe de clasificación \n ' )
print ( classification_report ( y_test , prediccion , target_names = [ 'Clase 0','Clase 1' , 'Clase 2' , 'Clase 3' ]))


