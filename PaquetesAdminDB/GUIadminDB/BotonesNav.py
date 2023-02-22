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
        
        #Con los nuevos widgets creados en self.framePadre, específicamente en cuerpo superior para este, procedemos a configurarlos:
        self.comboBox_Tablas['state'] = 'readonly' 
        self.comboBox_tipoBD.config(values = BaseDeDatosTipos, state = 'readonly')  #Con el atributo .config(), podemos hacer múltiples configuraciones simultaneamente.
        #No he encontrado una manera de definir el atributo command del botón desde Crear.py. Tarea pendiente:
        self.botón_conectarBD['command'] = lambda: self.widgetsParaCuerpoMedioSegunBaseDeDatosConectada()
        
        #Creamos los botones de navegación:
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
        #Dos formas de acceder a los contenidos de un widget tipo entry o combobox: por su variable de control o su atributo-método, .get().
        #Note que aquí no es necesario especificar la localización global del widget (self.framePadre.cuerpo_superior), sólo self.comboBox a secas:
        #print('self.comboBox_tipoBD.get() =', self.comboBox_tipoBD.get())
        #print('self.pathBD.get() =', self.pathBD.get())
        #self.conect.close()
        #[widget.destroy() for widget in self.framePadre.cuerpo_superior.grid_slaves()] #Medio palo.
        
        if self.comboBox_tipoBD.get() is not None:
            self.conect = conexiónConBD(self.txtBox_PathBD.get(), self.comboBox_tipoBD.get())
            self.comboBox_Tablas['values'] = self.conect.listaDeTablasEnLaBaseDeDatosConectada()      
        else:
            messagebox.showwarning(message='Debe elegir el tipo de base de datos!', title='Se le olvidó el tipo de base de datos!') 
            #Algunos path para probar:
            # /home/david/Documentos/bancoPsql.ini
            # /home/david/Documentos/Informática/sqlite/primera.db o ventas.db o bd1.db
        
                                       