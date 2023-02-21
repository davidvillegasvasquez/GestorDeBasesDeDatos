#1ero definimos los subdicts por tipo de widgets:
variableDeControl = {'pathBD':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'tipoBD':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'tabla':{'tipoWidget':'controlvar', 'tipoVar':'texto'}} #,...y así para el resto de variables de control. 

infoEntrysCuerpoSup = {'txtBox_PathBD':{'tipoWidget':'entry', 'ancho':9, 'varcontrol':'pathBD', 'col':2, 'fila':1, 'sticky':''}}

infoComboboxCuerpoSup = { 'comboBox_tipoBD':{'tipoWidget':'combobox', 'ancho':7, 'col':4, 'fila':1, 'varcontrol':'tipoBD','sticky':''}, 'comboBox_Tablas':{'tipoWidget':'combobox', 'ancho':7, 'col':2, 'fila':2, 'varcontrol':'tabla','sticky':''}}

infoLabelsCuerpoSup = {'etiqPathBD':{'tipoWidget':'label', 'texto':'PathBaseDeDatos', 'col':1, 'fila':1, 'sticky':''}, 'etiqTipoBD':{'tipoWidget':'label', 'texto':'TipoBaseDeDatos', 'col':3, 'fila':1, 'sticky':''}, 'etiqTablas':{'tipoWidget':'label', 'texto':'Tablas', 'col':1, 'fila':2, 'sticky':'e'}}

infoButtonCuerpoSup = { 'botón_conectarBD':{'tipoWidget':'botón', 'ancho':7, 'col':3, 'fila':2, 'sticky':'nsew'}} 

descripWidgetsCuerpoSup = {**variableDeControl, **infoEntrysCuerpoSup, **infoLabelsCuerpoSup, **infoComboboxCuerpoSup, **infoButtonCuerpoSup} #Y así se concatenan los diccionario de diccionarios para decrip de widgets contenidos en cuerpo superior. 
#Ojo, el orden importa: primero **variableDeControl, puesto que los textvariable no dependen de la existencia de los entrys, más no así el caso contrario.

#descripWidgetsCuerpoMedio = {'nombreWidget':{'tipoWidget':'hojaPorEj', 'ancho':9, 'col':0, 'fila':0, 'sticky':'NSWE'}}

#Como el cuerpo inferior generalmente se usa para los widgets de botones, su información está contenida directamente en el módulo WidgetContenedorYBotonesNav.py.

#Información para los widgets de los menús:

#Otros datos constantes:
BaseDeDatosTipos = ('postgresql', 'sqlite')
