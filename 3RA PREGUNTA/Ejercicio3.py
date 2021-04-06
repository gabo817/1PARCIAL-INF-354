# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:29:31 2021

@author: IBM GAMER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn import preprocessing

datos=pd.read_csv(r'train.csv')

X_inicial= datos.to_numpy()



imp = SimpleImputer(missing_values=np.NaN, strategy='mean')
X_salida=imp.fit_transform(X_inicial)

print(X_salida)

Aprepro = preprocessing.normalize(X_inicial)
print(Aprepro)



Aprepro = preprocessing.scale(X_inicial)
print(Aprepro)