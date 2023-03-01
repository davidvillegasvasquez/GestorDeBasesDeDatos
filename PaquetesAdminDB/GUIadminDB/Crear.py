from tkinter import ttk
from tkinter import *

#Función triádica, cantidad de parámetros inaceptables:
def crearWidgetsYsusVarControlEnBaseAdescrip(widget, widgetPadre, descripWidgets):
    for nombreWidget, val in descripWidgets.items():
        #1ero, creamos las variables de control tkinter. Note como la función setattr, al no encontrar el objeto a setear su atributo-propiedad, lo crea, tal "with open(ruta, mode='r+') as archivo" crea el archivo al no encontrarlo:
        tipo = descripWidgets[nombreWidget]['tipoWidget']
        #nombreWidget es el identificador apuntador del objeto creado con setattr().
      
        if tipo == "label":
            setattr(widget, nombreWidget, ttk.Label(widgetPadre, text=val['texto']))
        if tipo == "entry":
            setattr(widget, nombreWidget, ttk.Entry(widgetPadre, width=val['ancho']))    
        if tipo == "combobox":
            setattr(widget, nombreWidget, ttk.Combobox(widgetPadre, width=val['ancho']))    
        if tipo == "botón":
            setattr(widget, nombreWidget, ttk.Button(widgetPadre, width=val['ancho'], text = val['texto']))             
                                      
        #Y así sucesivamente para el resto de otros GUIadminDB (botones, frame, etc.)
        
        #Finalmente dibujamos los widgets recién creados arrriba. Note que ahora no necesitamos filtrar si el tipo de 
        #propiedad es una variable de control, pues no las usamos en este enfoque (usamos get y set directamente sobre el widget.
        widget.__dict__[nombreWidget].grid(column=val['col'], row=val['fila'], sticky=val['sticky'], columnspan = val['columnspan'])
          
def descripWidgetsSegunColumnasDeLaTabla(columnasDeTabla):
    dictDescripEtiquetas = {}
    dictDescripTxtBoxs = {}
    fila = 1
    for columna in columnasDeTabla:
        nombreEtiqueta = 'etiqueta_' + columna
        dictDescripEtiquetas[nombreEtiqueta] = {'tipoWidget':"label", 'texto':columna +':', 'col':1, 'fila':fila, 'sticky':'w', 'columnspan':1, 'ancho':12}
        nombreTxtBox = 'txtBox_' + columna
        dictDescripTxtBoxs[nombreTxtBox] = {'tipoWidget':'entry', 'ancho':'2', 'col':2, 'fila':fila, 'sticky':'w', 'columnspan':1, 'ancho':12} 
        fila +=1
        
    return  {**dictDescripTxtBoxs, **dictDescripEtiquetas}  
                   