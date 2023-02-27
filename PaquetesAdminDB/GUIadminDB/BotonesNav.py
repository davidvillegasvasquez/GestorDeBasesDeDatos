from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.Crear import *
from PaquetesAdminDB.LogicAdminDB.Posicionamiento import *
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import BaseDeDatosTipos
from PaquetesAdminDB.LogicAdminDB.ConexionesAbasesDeDatos import conexiónConBD
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import descripWidgetsCuerpoSuperior

listaColTablaAnteriorSelec = []

class WidgetMarco:
    def __init__(self, argraiz):
        self.framePadre = argraiz
        self.ir_a = StringVar()
        self.posicion = -1
        self.widgetCuerpoMedio = None
        #Creamos los widgets en la subdivisión cuerpo superior de self.framePadre, que es a su vez argraiz, al final raiz del módulo entrada.py. Note que tenemos que apuntarlo con el identificador self.widgetSuperior, que se pasará así mismo (self) para poder usar la función crearWidgetsYsusVarControlEnBaseAdescrip():
        self.widgetSuperior = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_superior, descripWidgetsCuerpoSuperior)
        self.objectConnect = None
        #Con los nuevos widgets creados en self.framePadre, específicamente en cuerpo superior para este, procedemos a configurarlos:
        self.comboBox_Tablas['state'] = 'readonly' 
        self.comboBox_tipoBD.config(values = BaseDeDatosTipos, state = 'readonly')  #Con el atributo .config(), podemos hacer múltiples configuraciones simultaneamente.
        self.comboBox_Tablas.bind("<<ComboboxSelected>>", self.dibujarWidgetEnCuerpoMedioDeCamposDeTablaSelecionada) #No se coloca argumentos en bind.
        #No he encontrado una manera de definir el atributo command del botón desde Crear.py. Tarea pendiente.
        self.botón_conectarBD['command'] = lambda: self.conectandoABaseDeDatosUbicadaEnPathDado()
        
        #Creamos los botones de navegación:
        self.botonPrimer = ttk.Button(self.framePadre.cuerpo_inferior, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAprimerRegistro", self.posicion)), text="<<", width=3)
        self.botonPrimer.grid(column=0, row=1, sticky=NSEW)
        self.botonRetro = ttk.Button(self.framePadre.cuerpo_inferior, text="<", width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("retroceder", self.posicion)))
        self.botonRetro.grid(column=1, row=1, sticky=NSEW)
        self.botonAvance = ttk.Button(self.framePadre.cuerpo_inferior, width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("avanzar", self.posicion)), text=">")
        self.botonAvance.grid(column=2, row=1, sticky=NSEW)
        self.botonUltimo = ttk.Button(self.framePadre.cuerpo_inferior, text=">>", width=3, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionLuegoDePulsarBoton("irAultimoRegistro", self.posicion)))
        self.botonUltimo.grid(column=3, row=1, sticky=NSEW)
        self.botonIrA = ttk.Button(self.framePadre.cuerpo_inferior, text="Buscar", command=lambda:self.actualizarWidgetsEnNuevaPosicion(indiceDelElementoEnTupla(self.ir_a.get(), self.posicion)))
        self.botonIrA.grid(column=4, row=1, sticky=NSEW)
        ttk.Entry(self.framePadre.cuerpo_inferior, width=7, textvariable=self.ir_a).grid(column=5, row=1) 
       
    def actualizarWidgetsEnNuevaPosicion(self, *args): 
        pass
        """
        self.posicion =  args[0] # Este método también actualiza self.posicion, violando el principio de que este método sólo debe hacer una sola cosa, y lo que dice que hace: actualizarWidgetEnNuevaPosicion. Recuerde que args[0] = nuevaPosicionLuegoDePulsarBoton(literal, self.posicion).
        nroDeCol = 0
        for nombre in self.archivoParent.cabezera:
            self.__dict__[nombre].set(self.archivoParent.obtenerContenido()[self.posicion][nroDeCol])
            nroDeCol += 1      
            self.hojaDeDatos.set_sheet_data(listaDeListasParaTksheetSegunPosicEnPadre(self.posicion)) 
        """
    def conectandoABaseDeDatosUbicadaEnPathDado(self, *args):
        self.comboBox_Tablas.set('')
        self.objectConnect = conexiónConBD(self.txtBox_PathBD.get(), self.comboBox_tipoBD.get())
        if self.objectConnect.conexión is not None and self.objectConnect is not None:  
            [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Borramos todos los widgets que hayan queadado en cuerpo medio con esta comprensión de lista. Medio palo.
            self.comboBox_Tablas['values'] = self.objectConnect.listaDeTablasEnLaBaseDeDatosConectada() #Tarea: tratar de meter todo esto en una lambda. 
            
    def dibujarWidgetEnCuerpoMedioDeCamposDeTablaSelecionada(self, tablaSeleccionada, *args): #Si declaro un parámetro formal con un nombre arbitrario en la función enlazada a una acción sobre un widget por medio de 
    #su atributo .bind (self.comboBox_Tablas.bind("<<ComboboxSelected>>", este método)), tomará el valor seleccionado de dicho widget -una cadena mostrada en el widget- con el atributo método widget.get(), para este caso, tablaSeleccionada.widget.get()
        global listaColTablaAnteriorSelec #Debe ser perdurable para guardar los identificadores de var de control anteriores, por eso la hacemos global.
        self.comboBox_Tablas.selection_clear() #Se debe ejecutar necesariamente si el widget está en estado readonly.          
        [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Sino al cambiar de campo quedarán los widget del anterior.
        print('listaColTablaAnteriorSelec', listaColTablaAnteriorSelec)
        #Ahora procedemos a borrar las variables de control referentes a la tabla anterior, para que no se acumulen:
        #1 Hacer una función con la implementación de 1 a 2.
        if listaColTablaAnteriorSelec != []:
            listaAnteriorParaCorroborBash = listaColTablaAnteriorSelec
            for col in listaColTablaAnteriorSelec:
                delattr(self, col) #Fijese que para la función delattr, se usa sólo self para referirse al widget raíz, es decir, self.framePadre.
        #2
        listaColTablaAnteriorSelec = self.objectConnect.listaDecolumnasDeTabla(tablaSeleccionada.widget.get()) 
        self.widgetCuerpoMedio = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_medio, descripWidgetsSegunColumnasDeLaTabla(listaColTablaAnteriorSelec))
        
        #Corroboramos que se van eliminando las variables de control obsoletas correspondientes a widgets que ya no existen:
        print('self.pathBD =', self.pathBD)
        print('self.pathBD.get() =', self.pathBD.get())
        
        try:
            print(f'self.{listaColTablaAnteriorSelec[0]} = {self.__dict__[listaColTablaAnteriorSelec[0]]}')
            print(f'self.{listaColTablaAnteriorSelec}.get() = {self.__dict__[listaColTablaAnteriorSelec[0]].get}') 
        except:
            print('self.{listaAnteriorParaCorroborBash[0]} no existe...')
        
        try:
            print(f'self.{listaAnteriorParaCorroborBash[1]} = {self.__dict__[listaAnteriorParaCorroborBash[0]]}')
            print(f'self.{listaAnteriorParaCorroborBash[1]}.get() = {self.__dict__[listaAnteriorParaCorroborBash[1]].get}')
        except:
            print('self.{listaAnteriorParaCorroborBash[1]} no existe...')
            
        try:
            print(f'self.{listaAnteriorParaCorroborBash[2]} = {self.__dict__[listaAnteriorParaCorroborBash[0]]}')
            print(f'self.{listaAnteriorParaCorroborBash[2]}.get() = {self.__dict__[listaAnteriorParaCorroborBash[2]].get}')
        except:
            print('self.{listaAnteriorParaCorroborBash[2]} no existe...')
            
        print('---------------------')
                
                
                                                  