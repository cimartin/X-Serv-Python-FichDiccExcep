#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejercicio 13.5

fd = open('/etc/passwd', 'r')
num_usuarios=fd.readlines()
dicc = {}

for user in num_usuarios:
    conf = user.split(":");
    username = conf[0]
    shell = conf[-1][:-1]
    dicc[username] = shell
    #print ("El usuario: *" + username + "* utiliza la shell: " + shell)

print ("Comprobamos la clave y el valor de root")
print ("root", dicc["root"])
print ("Ahora evitamos la excepcion que nos da imaginario al no estar en nuestro diccionario")
try:
    print ("*imaginario*", dicc["imaginario"])
except KeyError:
    print ("no se encuentra la clave en el diccionario")
fd.close()
