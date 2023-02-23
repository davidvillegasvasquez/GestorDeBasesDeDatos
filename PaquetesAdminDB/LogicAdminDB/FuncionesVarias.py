

def id_x(strCabezera, strCola):
    ahora = datetime.now()
    return f'{strCabezera}-{str(ahora.year)[2:]}{ahora.month}{ahora.day}{ahora.hour}{ahora.minute}{ahora.second}-{strCola}'
    
