from tkinter import *
from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.Crear import *
from PaquetesAdminDB.LogicAdminDB.Posicionamiento import *
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import BaseDeDatosTipos
from PaquetesAdminDB.LogicAdminDB.ConexionesAbasesDeDatos import conexiónConBD
#from PaquetesAdminDB.LogicAdminDB.FuncionesVarias import *

class WidgetMarco:
    def __init__(self, argraiz):
        self.framePadre = argraiz
        self.ir_a = StringVar()
        self.posicion = -1
        #Creamos los widgets en la subdivisión cuerpo superior de self.framePadre, que es a su vez argraiz, al final raiz del módulo entrada.py
        self.widgetSuperior = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_superior)
        self.comboBox_tipoBD['values'] = BaseDeDatosTipos
         #Y de dónde salieron los atributos nuevos, self.comboBox_tipoBD y self.botón_conectarBD: claramente acaban de ser creados arriba con self.widgetSuperior = crearWidgetsYsusVarControlEnBaseAdescrip()
        self.comboBox_Tablas['values'] = ('ventas', 'articulos', 'etc') #Origen (función, método objeto, etc.)
        #self.botón_conectarBD['command'] = lambda: [widget.destroy() for widget in self.framePadre.cuerpo_superior.grid_slaves()] #Así sería si no necesitaramos más proposiciones. Sólo barrer todos los widgets para el cuerpo en cuestión.
        self.botón_conectarBD['command'] = lambda: self.widgetsParaCuerpoMedioSegunBaseDeDatosConectada()
        self.botonPrimer = ttk.Button(self.framePadre.cuerpo_inferior, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAprimerRegistro", self.posicion)), text="<<", width=3)
        self.botonPrimer.grid(column=0, row=1, sticky=NSEW)
        self.botonRetro = ttk.Button(self.framePadre.cuerpo_inferior, text="<", width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("retroceder", self.posicion)))
        self.botonRetro.grid(column=1, row=1, sticky=NSEW)
        self.botonAvance = ttk.Button(self.framePadre.cuerpo_inferior, width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("avanzar", self.posicion)), text=">")
        self.botonAvance.grid(column=2, row=1, sticky=NSEW)
        self.botonUltimo = ttk.Button(self.framePadre.cuerpo_inferior, text=">>", command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAultimoRegistro", self.posicion)), width=3)
        self.botonUltimo.grid(column=3, row=1, sticky=NSEW)
        self.botonIrA = ttk.Button(self.framePadre.cuerpo_inferior, text="Buscar", command=lambda:self.actualizarWidgetsEnNuevaPosicion(indiceDelElementoEnTupla(self.ir_a.get(), self.posicion)))
        self.botonIrA.grid(column=4, row=1, sticky=NSEW)
        ttk.Entry(self.framePadre.cuerpo_inferior, width=7, textvariable=self.ir_a).grid(column=5, row=1) 
       
    def actualizarWidgetsEnNuevaPosicion(self, *args): 
        pass
        """
        self.posicion =  args[0]
        self.etiqImagenFoto['image'] = self.fotosPIL[self.posicion]
        """
    def widgetsParaCuerpoMedioSegunBaseDeDatosConectada(self, *args):
        #Dos formas de acceder a los contenidos de un widget tipo entry o combobox: por su variable de control o su propiedad.
        #Note que aquí no es necesario especificar la localización global del widget (self.framePadre.cuerpo_superior), sólo self.comboBox a secas:
        print('self.comboBox_tipoBD.get() =', self.comboBox_tipoBD.get())
        print('self.pathBD.get() =', self.pathBD.get())
     
        [widget.destroy() for widget in self.framePadre.cuerpo_superior.grid_slaves()] #Medio palo.
        #print('self.txtBox_PathBD.get() =', self.txtBox_PathBD.get()) # Después de borrar el widget, ya no podemos acceder a él: invalid command name ".!frame.!entry"
        
        
                                       