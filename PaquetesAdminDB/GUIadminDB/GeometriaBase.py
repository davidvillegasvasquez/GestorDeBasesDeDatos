from tkinter import * 
from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import descripWidgetsCuerpoSup
from os.path import exists
from tkinter import messagebox

class Geometria:
    def __init__(self, argRaiz):   
        self.raizTk = argRaiz
        self.raizTk.title("GESTOR DE BASE DE DATOS")
        # Cuerpo superior(lo colocamos en row = 1 para dejarnos margén de maniobra para una eventual necesidad de agregar):
        self.cuerpo_superior = ttk.Frame(self.raizTk)
        self.cuerpo_superior.grid(column=1, row=1, sticky=(N, W, E, S))
        
        self.cuerpo_medio = ttk.Frame(self.raizTk)
        self.cuerpo_medio.grid(column=1, row=2, sticky ='nsew')
        
        self.cuerpo_inferior = ttk.Frame(self.raizTk)
        # En la columna 0 y fila 1 de argroot (mitad vertical).
        self.cuerpo_inferior.grid(column=1, row=3)
        
        self.barraMenú = Menu(self.raizTk)
        # Con la opción de configuración menu del widget dónde irá el menú (que la interfaz raíz), visibilizamos el menú: es remotamente equivalente al grid.
        # La propiedad menu del widget, en este caso la interfaz raíz, tendrá como valor el menú que instanciamos sobre el, y que apuntamos con el identificador barraMenú.
        self.raizTk['menu'] = self.barraMenú

        # Para aspecto moderno y no desacoplable de los menú, antes de crear cualquiera de ellos, colocamos esta proposición:
        self.raizTk.option_add('*tearOff', FALSE)
        
        # Creamos el primer menú contenido en barraMenú, apuntado por el identificador menu1:
        self.menu1 = Menu(self.barraMenú)
        # Creamos otro menú que ya veremos que le agregamos. Puede ser versión, ayuda, acerca de, etc.
        self.menu2 = Menu(self.barraMenú)
        # Agregamos los menú creado en la barra de menú barraMenú.
        self.barraMenú.add_cascade(label="MENÚ 1", menu=self.menu1)
        self.barraMenú.add_cascade(label="MENÚ 2", menu=self.menu2)
        
        # Agregamos los comandos a los menús:
        self.menu1.add_command(label="Comando1 en Menú 1", command = '')
        self.menu1.add_command(label="Comando2 en Menú 1", command="")
        self.menu2.add_command(command="", label="Coman1 en menu2")
        self.menu2.add_command(label="Coman2 en menu2")
        
    def ingresarFotosByteaEnPostgre(self, *args):
        self.top = Toplevel(height = 200, width = 100)
        self.top.title('Ingreso de Fotos')
        self.ubicacionFoto = StringVar()
        #crearWidgetsYsusVarControlEnBaseAdescrip(self, self.top) #self.framePadre.cuerpo_superior)
        ttk.Label(self.top, text='Ubicación de la foto:').grid(row=1, column=1)
        self.txtBoxUbicacionFoto = ttk.Entry(self.top, width= 20, textvariable = self.ubicacionFoto)
        self.txtBoxUbicacionFoto.grid(row=1, column=2)
        ttk.Button(self.top, width= 7, text = 'Ingresar', command = self.ingresarFotoAbaseDeDatosPostgre).grid(row=1, column=3)
        self.top.grab_set()

    def ingresarFotoAbaseDeDatosPostgre(self, *args):
        pass
        """
        archivoFoto = self.ubicacionFoto.get()
        if exists(archivoFoto): 
            fotoIngreso = FotoToolsPostgreSQL()
            fotoIngreso.ingresarFotoAPostgre(ubicaciónFoto = archivoFoto)
        else:
            messagebox.showerror(message='No se encontró foto: verifique que path y nombre de foto estén correctos. Recuerde incluir extensión .jpg en nombre.', title='Error')
        """         
              
