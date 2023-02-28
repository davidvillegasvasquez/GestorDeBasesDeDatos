from tkinter import messagebox

#Otra función triádica que no se puede evitar: se ve que tanto más dinámica las implementaciones, más parámetros exigen.
def nuevaPosicionFilaLuegoDePulsarBoton(accion, posicionActual, argLongitud):
    posicion = posicionActual
    primeraPosicion = 0
    longitud = argLongitud
   
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
          