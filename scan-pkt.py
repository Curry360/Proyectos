import subprocess


subprocess.call('clear')

logo='''
=========================================================================
██████╗░██╗░░██╗████████╗░█████╗░░░░░░░░██████╗░█████╗░░█████╗░███╗░░██╗
██╔══██╗██║░██╔╝╚══██╔══╝██╔══██╗░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║
██████╔╝█████═╝░░░░██║░░░██║░░██║█████╗╚█████╗░██║░░╚═╝███████║██╔██╗██║
██╔═══╝░██╔═██╗░░░░██║░░░██║░░██║╚════╝░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░░░░░██║░╚██╗░░░██║░░░╚█████╔╝░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
=========================================================================
'''
print(logo)

sitioweb = (input('Introduce sitio web para escanear: '))


def menu():
    print('''\nQue herramienta quieres usar?
    |===========================================================|
    | [1]Nmap (Escanear los puertos de una IP o Sitio Web )     |
    | [2]WhatWeb (Identifica el Sitio Web)                      |
    | [3]GoBuster (Enumerar directorio ocultos en un Sitio Web) |
    | [4]Todas las herramientas                                 |
    | [5]Salir                                                  |
    |===========================================================|

    ''')

menu()

def opcion1():
    print('\nEjecutando NMAP...')
    resultado = subprocess.call(['nmap','-sS','-sV','-sC', sitioweb])
    print(resultado)


def opcion2():
    print('\nEjecutando WhatWeb...')
    resultado = subprocess.call(['whatweb', sitioweb])
    print(resultado)

def opcion3():
    print('\nEjecutando GoBuster...')
    urlgobuster=input(('''Introduce el sitio web con http:// o https:// \n--Nota: añada una / al final para que GoBuster busque a partir de ahí: '''))
    resultado = subprocess.call(['gobuster','dir','-u',urlgobuster,'-w','/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt'])


opcion = (input('Elige una opción: '))


#Validar datos numéricos 
'''De esta forma lo que hacemos es controlar el error nosotros y poder hacerselo entender al usuario 
    diciendole que lo que ha introducido no es un número, ahorrariamos código si al input de opción le ponemos el int delante pero claro
    si el usuario introduce una letra o algo que no sea numerico va a ser python el que arroje el fallo y ahora ponte a entenderlo
'''
#Mientras no sea digito, me ejecuto
while not opcion.isdigit(): 
    opcion = input("Por favor, introduce un número válido: ")

opcion = int(opcion) #Aqui estamos pasando el número por ejemplo 7 de cadena de caracteres a NÚMERO ENTERO


while opcion !=5:

    if opcion == 1:
        opcion1()

    elif opcion == 2:
        opcion2()

    elif opcion == 3:
        opcion3()

    elif opcion == 4:
        opcion1()
        opcion2()
        opcion3()

    else:
        print('Por favor debe introducir un número correcto')

    menu()
    opcion = int(input('Elige una opción: '))

print('Adios!')



