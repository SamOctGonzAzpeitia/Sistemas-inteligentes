#Samuel Octavio gonzález Azpeitia
#A01704696
import random
import time
import os

def welcome():
    print("*********** Bienvenido al juego *******")
    print()
    print()
    print("***************** Palillos ************")
    print()
    print()
    print("*********  1.-Fácil / 2.-Difícil  *****")
    print()
    print()
    print("***************************************")
    print()
    nivel=int(input("Elige el nivel de dificultad: "))
    if nivel != 1 and nivel != 2:
        print("Elige una opción válida")
        welcome()
    else:
        return nivel


def valores():
    palillos = random.randint(20, 25)
    quitar = random.randint(2, 5)

    return palillos, quitar

def juego(palillos, quitar):
    print("**************************************")
    print("****** Quedan estos palillos: ********")
    print("Elige entre 1 y {}".format(quitar))
    print()
    
    for fila in range (4):
        print(end=" ")
        for p in range(1, palillos+1):
            print("|", end=" ")
            if p % quitar == 0:
                print(end= " ")
        
        print()
    
    print()
    print()

def player_movement(palillos, quitar):

    aux = int(input("¿Cuántos palillos quieres quitar? "))
    print(quitar)
    flag = False
    while flag==False:
        if aux > quitar:
            print("Elige entre 1 y {}".format(quitar))
            aux = int(input())
        elif aux > palillos:
            aux = input("Sólo quedan {} palillos".format(palillos))
        else:
            palillos_quitar = aux
            flag=True

    return palillos_quitar

def computer_movement(palillos, quitar):
    
    if palillos % quitar == 0:
        palillos_quitar = random.randint(1, quitar)
    else:
        palillos_quitar = palillos % quitar

    print("El ordenador ha quitado " + str(palillos_quitar) + " palillos")

    return palillos_quitar

def inteligence_movement(palillos, quitar):
   
   palillos_quitar=0

   while palillos_quitar == 0 or palillos_quitar > palillos:
        if palillos <= quitar:
            palillos_quitar = palillos
        elif palillos % (quitar + 1) == 5:
            palillos_quitar = 5
        elif palillos % (quitar + 1) == 4:
            palillos_quitar = 4
        elif palillos % (quitar + 1) == 3:
            palillos_quitar = 3
        elif palillos % (quitar + 1) == 2:
            palillos_quitar = 2
        elif palillos % (quitar + 1) == 1:
            palillos_quitar = 1
        elif palillos % (quitar + 1) == 0:
            palillos_quitar = random.randint(1, 2)
    
        print(palillos_quitar, palillos)
        return palillos_quitar

def winner(turno):
    if turno == 1:
        print("¡Has perdido!")
    elif turno == 2:
        print("¡Has ganado!")


turno = 2
palillos, quitar = valores()

os.system("cls")
nivel = welcome()

os.system("cls")
juego(palillos, quitar)

jugando = True

while jugando:

    os.system("cls")
    juego(palillos, quitar)

    if turno == 1:
        palillos_quitar = player_movement(palillos, quitar)
        palillos -= palillos_quitar
        turno = 2
    elif turno == 2:
        print("Ordenador pensando")
        time.sleep(4)
        if nivel == 1:
            palillos_quitar = computer_movement(palillos, quitar)
        elif nivel == 2:
            palillos_quitar = inteligence_movement(palillos, quitar)
        palillos -= palillos_quitar
        turno = 1
    
    if palillos == 0:
        os.system("cls")
        winner(turno)
        jugando = False