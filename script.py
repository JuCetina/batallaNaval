import random

tablero = []

#Crea 5 listas de 5 elementos O en tablero
for x in range(0,5):
  tablero.append(["O"] * 5)

#Muestra el tablero sin comas ni corchetes
def print_tablero(tablero):
  for fila in tablero:
    print " ".join(fila)

print "Juguemos Batalla Naval!"
print "Tienes 4 intentos:"
print_tablero(tablero)

#Crea un indice aleatorio para la fila
def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

#Crea un indice aleatorio para la columna
def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_columna = columna_aleatoria(tablero)

#Controla los 4 intentos
for turno in range(4):
    
    #Para que el usuario ingrese la fila y la columna
    adivina_fila = input("Adivina fila: ")
    adivina_columna = input("Adivina columna: ")
    
    #Si adivina la fila y la columna
    if adivina_fila == barco_fila and adivina_columna == barco_columna:
        print "Felicitaciones! Hundiste mi barco!"
        break
    
    #Si los indices que ingreso el usuario estan fuera del tablero
    elif (adivina_fila < 0 or adivina_fila > 4) or (adivina_columna < 0 or adivina_columna > 4):
        print "Uy, eso ni siquiera esta en el oceano."
    
    #Si repite indices de fila y columna    
    elif(tablero[adivina_fila][adivina_columna] == "X"):
        print "Ya dijiste esa."
    
    #Si no adivina fila y columna y no ha repetido indices   
    else:
  	    print "No tocaste mi barco!"
  	    tablero[adivina_fila][adivina_columna] = "X"
  	    print_tablero(tablero)
    
    #Muestra los turnos
    print "Turno: %s" % (turno + 1)
    
    #Muestra fin del juego
    if turno == 3:
        print "Fin del juego."