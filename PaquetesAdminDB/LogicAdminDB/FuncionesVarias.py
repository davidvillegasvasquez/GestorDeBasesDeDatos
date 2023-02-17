from datetime import datetime
import os
from PaquetesAdminDB.Widgets.DescripciónDeLosWidgets import pathCarpetaDeFotosJpg

def id_x(strCabezera, strCola):
    ahora = datetime.now()
    return f'{strCabezera}-{str(ahora.year)[2:]}{ahora.month}{ahora.day}{ahora.hour}{ahora.minute}{ahora.second}-{strCola}'
    
def cantFotosJpgEnCarpetaFotos():
    cantidad = 0
    with os.scandir(pathCarpetaDeFotosJpg) as carpeta: #Hay que meter ese path en un modulo o clase e importarlo.
        for foto in carpeta:
            if foto.is_file()  and foto.name.endswith('.jpg'):
                cantidad += 1 
    return cantidad
    
def cantFotosJpgEnBD():
    return 4
    
