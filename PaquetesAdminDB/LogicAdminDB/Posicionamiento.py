from tkinter import messagebox


def nuevaPosicionLuegoDePulsarBoton(accion, posicionActual):
    posicion = posicionActual
    primeraPosicion = 0
    longitud = 5
   
    if accion == "irAprimerRegistro": posicion = primeraPosicion
    
    if accion == "retroceder":
    # Condición validadora de que no estamos en la primera posición (posición=1).
        if posicion > primeraPosicion:
            posicion -= 1
        else:
            pass
            
    if accion == "avanzar":
        if posicion < longitud - 1:
                posicion += 1
        else:
            pass

    if accion == "irAultimoRegistro": posicion = longitud - 1
    
    return posicion
   
def indiceDelElementoEnTupla(elementoBuscado, posicionActual):
    return 2
          