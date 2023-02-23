from tkinter import *
from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.Crear import *
from PaquetesAdminDB.LogicAdminDB.Posicionamiento import *
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import BaseDeDatosTipos
from PaquetesAdminDB.LogicAdminDB.ConexionesAbasesDeDatos import conexiónConBD
#from PaquetesAdminDB.LogicAdminDB.FuncionesVarias import *
from tkinter import messagebox

class WidgetMarco:
    def __init__(self, argraiz):
        self.framePadre = argraiz
        self.ir_a = StringVar()
        self.posicion = -1
        #Creamos los widgets en la subdivisión cuerpo superior de self.framePadre, que es a su vez argraiz, al final raiz del módulo entrada.py
        self.widgetSuperior = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_superior)
        self.objectConnect = None
        #Con los nuevos widgets creados en self.framePadre, específicamente en cuerpo superior para este, procedemos a configurarlos:
        self.comboBox_Tablas['state'] = 'readonly' 
        self.comboBox_tipoBD.config(values = BaseDeDatosTipos, state = 'readonly')  #Con el atributo .config(), podemos hacer múltiples configuraciones simultaneamente.
        self.comboBox_tipoBD.bind("<<ComboboxSelected>>", self.metodoX) #No se coloca argumentos en bind.
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
       
        #[widget.destroy() for widget in self.framePadre.cuerpo_superior.grid_slaves()] #Medio palo.
        
        self.objectConnect = conexiónConBD(self.txtBox_PathBD.get(), self.comboBox_tipoBD.get())
        if self.objectConnect.conexión is not None and self.objectConnect is not None:
            self.comboBox_Tablas['values'] = self.objectConnect.listaDeTablasEnLaBaseDeDatosConectada() #Tarea: tratar de meter todo esto en una lambda. 
            
    def metodoX(self, nombreArbitrario, *args): #Si declaro un parámetro formal con un nombre arbitrário en la función enlazada al widget, tomará el valor seleccionado de dicho widget con el atributo método widget.get():              
        messagebox.showwarning(message=f'Selecionó {nombreArbitrario.widget.get()}', title='Selección')
        
        
                   
            
        
                                       