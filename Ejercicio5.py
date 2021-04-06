# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:31:49 2021

@author: IBM GAMER
"""
from kanren import run, eq, var
x = var()
y = var()
z = var()


from kanren import Relation, facts,conde ,lall,lany
padre = Relation()

facts(padre, ('francisco','pablo'),
('francisco','rene'),
('francisco','rosa'),
('francisco','barbara'),
('manuela','pablo'),
('manuela','rene'),
('manuela','rosa'),
('manuela','barbara'),
('felipe','elias'),
('felipe','ramiro'),
('felipe','fabiana'),
('felipe','lucy'),
('tomasa','elias'),
('tomasa','ramiro'),
('tomasa','fabiana'),
('tomasa','lucy'),
('rene','freddy'),
('rene','adriana'),
('fernanda','freddy'),
('fernanda','adriana'),
('juan','yolanda'),
('juan','yolanda'),
('rosa','rosmery'),
('rosa','rosmery'),
('elias','nayra'),
('elias','maria'),
('elias','gabi'),
('elias','gabriel'),
('barbara','nayra'),
('barbara','maria'),
('barbara','gabi'),
('barbara','gabriel'),
('ramiro','rocio'),
('ramiro','miguel'),
('alejandra','rocio'),
('alejandra','miguel')
)

print(run(4,x, padre("gabriel",x)))
#print(run(4,x, padre("gabriel",y,x)) )
#print(run(2,x, padre("rosa",x,x)))
#print(run(2,x, mujer(x,y)))


def abuelos(x, z):
    y = var()
    return conde((padre(x,y), padre(y,z) ))

def tios(x, z):
    y = var()
    w = var()
    lista=set(run(16, x, conde((padre(y,x), padre(y,w), padre(w,z)))))
    p=list(run(8, x, padre(x, z)))
    for i in p:
        lista.discard(i)
    return lista
    
def hermanos(x,w):
    lista=set(run(8, x, conde((padre(y,x), padre(y,w) ))))
    lista.discard(w)
    return lista

def hijos(x,w):
    return (padre(x,w))

def primos(x,w):
    y = var()
    t = var()
    u = var()
    e = var()
    
    lista=set(run(40, x, conde((padre(y,x), padre(t,w), padre(u,y),padre(u,t)))))
    herm=hermanos(e,w)
    for i in herm:
        lista.discard(i)
    lista.discard(w)
    return lista

print(run(8, x, abuelos(x, 'gabriel')))
print(tios(x, 'gabriel'))
print(hermanos(x, 'elias'))
print(run(8, x, hijos('elias',x)))
print(primos(x,'gabriel'))



