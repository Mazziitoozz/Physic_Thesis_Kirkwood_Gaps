# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:30:39 2019

@author: Mazziitoozz
"""
'''
Metodo de Euler 
No usar para movimientos periodicos, introduce energia al sistema.
Funcion que nos vale para calcular la posicion y la velocidad de un objeto acelerado en funcion del tiempo. Metodo de Euler
 Input:
         a=     aceleracion que sufre el cuerpo
         r0=    vector que contenga posicion inicial
         v0=    vector que contenga la velocidad inicial
         dt=    paso de tiempo
         tend=  tiempo final
     
    Output:
        x_vector, y_vector, z_vector =      Vectores que contienen las posiciones del cuerpo durante el intervalo de tiempo elegido
        vx_vector, vy_vector, vz_vector =   Vectores que contienen las velocidades del cuerpo durante el intervalo de tiempo elegido
        t_vector =                          Vector que contiene los tiempos

Ejemplo de funcion
 def a(x,y,z):
    ax= -G*M*x/(x**2+y**2+z**2)**(3/2)
    ay= -G*M*y/(x**2+y**2+z**2)**(3/2)
    az= -G*M*z/(x**2+y**2+z**2)**(3/2)
    return [ax,ay,az]
'''

def Euler(a,r0,v0,dt,tend):
    
#Creamos vectores de las posiciones, tiempo y velocidades

    x_vector = []
    y_vector = []
    z_vector = []
    
    t_vector = []
    
    vx_vector = []
    vy_vector = []
    vz_vector = []
    
#Condiciones iniciales

    x = r0[0]
    y = r0[1]
    z = r0[2]
    t = 0                 #Tiempo a partir del cual empezamos a contar
    vx = v0[0]
    vy = v0[1]
    vz = v0[2]
    
#Decimos que el primer elemento de nuestros vectores sea:
    
    x_vector.append(x)
    y_vector.append(y)
    z_vector.append(z)
    
    vx_vector.append(vx)
    vy_vector.append(vy)
    vz_vector.append(vz)
    
    t_vector.append(t)
    n=int(tend/dt)      #Numero de elementos que contendran nuestros vectores

    for i in range (0,n):                                                                # _next significa del paso siguiente y si no lleva nada significa que es el actual   
 
        [ax, ay, az] = a(x, y,z)                                                             #Decimos que esos valores son los de la funcion aceleracion previamente creada
                                                                                         #Si quiseramos que nuestra aceleracion dependiera de la masapondriamos a(x,y,z,M) 
        x_next = x + vx * dt                                                                # La posicion del paso siguiente = a la posicion del paso actual 
        y_next = y + vy * dt                                                                # + la velocidad actual
        z_next = z + vz * dt 
        
        vx_next = vx + ax * dt
        vy_next = vy + ay * dt
        vz_next = vz + az * dt
        
        x_vector.append(x_next)                                                          # Guardamos los valores en nuestros vectores
        y_vector.append(y_next)
        z_vector.append(z_next)
    
        vx_vector.append(vx_next)
        vy_vector.append(vy_next)
        vz_vector.append(vz_next)
#        
        t_next = t + dt
#        
        t_vector.append(t_next)
    
        x = x_next                                                                          # Actualizamos los valores  para realizar de nuevo el bucle
        y = y_next
        z = z_next
        
        t=t_next
        
        vx = vx_next
        vy = vy_next
        vz = vz_next
        
    return t_vector, x_vector, y_vector, z_vector, vx_vector, vy_vector, vz_vector
