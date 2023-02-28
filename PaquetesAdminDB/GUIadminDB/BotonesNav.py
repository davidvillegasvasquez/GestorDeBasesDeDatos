from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.Crear import *
from PaquetesAdminDB.LogicAdminDB.Posicionamiento import *
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import BaseDeDatosTipos
from PaquetesAdminDB.LogicAdminDB.ConexionesAbasesDeDatos import conexiónConBD
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import descripWidgetsCuerpoSuperior

listaColTablaAnterior = []

class WidgetMarco:
    def __init__(self, argraiz):
        self.framePadre = argraiz
        self.ir_a = StringVar()
        self.posicionFilaActual = -1
        self.widgetCuerpoMedio = None
        self.registrosEnTablaActual = None #Es llenado por la lista de tuplas de un fetchall().
        self.cantRegistrosTablaActual = 0
        self.columnasDeTablaActual = None #Es la lista de cadenas retornada por listaDecolumnasDeTabla().
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
        self.botonPrimer = ttk.Button(self.framePadre.cuerpo_inferior, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionFilaLuegoDePulsarBoton("irAprimerRegistro", self.posicionFilaActual, self.cantRegistrosTablaActual)), text="<<", width=3)
        self.botonPrimer.grid(column=0, row=1, sticky=NSEW)
        self.botonRetro = ttk.Button(self.framePadre.cuerpo_inferior, text="<", width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionFilaLuegoDePulsarBoton("retroceder", self.posicionFilaActual, self.cantRegistrosTablaActual)))
        self.botonRetro.grid(column=1, row=1, sticky=NSEW)
        self.botonAvance = ttk.Button(self.framePadre.cuerpo_inferior, width=2, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionFilaLuegoDePulsarBoton("avanzar", self.posicionFilaActual, self.cantRegistrosTablaActual)), text=">")
        self.botonAvance.grid(column=2, row=1, sticky=NSEW)
        self.botonUltimo = ttk.Button(self.framePadre.cuerpo_inferior, text=">>", width=3, command=lambda: self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionFilaLuegoDePulsarBoton("irAultimoRegistro", self.posicionFilaActual, self.cantRegistrosTablaActual)))
        self.botonUltimo.grid(column=3, row=1, sticky=NSEW)
        self.botonIrA = ttk.Button(self.framePadre.cuerpo_inferior, text="Buscar", command=lambda:self.actualizarWidgetsEnNuevaPosicion(indiceDelElementoEnTupla(self.ir_a.get(), self.posicionFilaActual)))
        self.botonIrA.grid(column=4, row=1, sticky=NSEW)
        ttk.Entry(self.framePadre.cuerpo_inferior, width=7, textvariable=self.ir_a).grid(column=5, row=1) 
       
    def actualizarWidgetsEnNuevaPosicion(self, *args): 
        #Primero, actualizamos la posiciónd dentro del widget:
        self.posicionFilaActual =  args[0] # Recuerde que args[0] = nuevaPosicionFilaLuegoDePulsarBoton(literal, self.posicionFilaActual).
        nroElemnEnTupla = 0
        for varControl in self.columnasDeTablaActual:
            #Recuerde que el indice de elemento en self.columnasDeTablaActual coincide con nroColEnTupla. 
            self.__dict__[varControl].set(self.registrosEnTablaActual[self.posicionFilaActual][nroElemnEnTupla])
            nroElemnEnTupla += 1     
                
    def conectandoABaseDeDatosUbicadaEnPathDado(self, *args):
        self.comboBox_Tablas.set('')
        self.objectConnect = conexiónConBD(self.txtBox_PathBD.get(), self.comboBox_tipoBD.get())
        if self.objectConnect.conexión is not None and self.objectConnect is not None:  
            [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Borramos todos los widgets que hayan queadado en cuerpo medio con esta comprensión de lista. Medio palo.
            self.comboBox_Tablas['values'] = self.objectConnect.listaDeTablasEnLaBaseDeDatosConectada() #Tarea: tratar de meter todo esto en una lambda. 
            
    def dibujarWidgetEnCuerpoMedioDeCamposDeTablaSelecionada(self, tablaSeleccionada, *args): #En un método disparado por un evento virtual de widget con capacidad para ello, enlazado por medio de 
    #su atributo .bind (self.comboBox_Tablas.bind("<<ComboboxSelected>>", este método)), si declaro un parámetro formal con un nombre arbitrario en dicho método o función enlazado, en dicho parámetro se depositará
    # el valor seleccionado en dicho widget -una cadena mostrada en este- con el atributo método widget.get(), para este caso, tablaSeleccionada.widget.get()
  
        global listaColTablaAnterior #Debe ser perdurable para guardar los identificadores de var de control anteriores, por eso la hacemos global y su definición respectiva en este módulo.
        listaAnteriorParaCorroborBash = ['col1', 'col2', 'col3', 'col4']
        self.comboBox_Tablas.selection_clear() #Se debe ejecutar necesariamente si el widget está en estado readonly.          
        [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Sino al cambiar de campo quedarán los widget del anterior.
        print('listaColTablaAnterior', listaColTablaAnterior)
        self.posición = -1 #Reseteamos a posición de de partida.
        #Ahora procedemos a borrar las variables de control referentes a la tabla anterior, para que no se acumulen:
        #1 Hacer una función con la implementación de 1 a 2.
        if listaColTablaAnterior != []:
            listaAnteriorParaCorroborBash = listaColTablaAnterior
            for col in listaColTablaAnterior:
                delattr(self, col) #Fijese que para la función delattr, se usa sólo self para referirse al widget raíz, es decir, self.framePadre.
        #2
        #Según lo anterior, creo que el enfoque más práctico y eficiente es no usar variables de control, sino tomar el valor del texto mostrado por el widget directmente, por medio de su propiedad .get() y .set().
        listaColTablaAnterior = self.objectConnect.listaDecolumnasDeTabla(tablaSeleccionada.widget.get()) 
        #Ahora si dibujamos los nuevos widgets en cuerpo medio según tabla seleccionada:
        self.widgetCuerpoMedio = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_medio, descripWidgetsSegunColumnasDeLaTabla(listaColTablaAnterior))
        self.columnasDeTablaActual = listaColTablaAnterior #Definit, es mejor get ser directamente sobre widgets.
        #Asignamos valores a atributos self.registrosEnTablaActual y self.cantRegistrosTablaActual:
        self.registrosEnTablaActual = self.objectConnect.consultaSql(f'select * from {tablaSeleccionada.widget.get()}')
        self.cantRegistrosTablaActual = len(self.registrosEnTablaActual)
        #Colocamos los valores de los widgets del primer registro al comenzar:
        #self.actualizarWidgetsEnNuevaPosicion(nuevaPosicionFilaLuegoDePulsarBoton("irAprimerRegistro", self.posicionFilaActual, self.cantRegistrosTablaActual))
        self.botonPrimer.invoke() #Es más consciso invocar método invoke para simular click sobre botón 'irAprimerRegistro'.
        #Corroboramos que se van eliminando las variables de control obsoletas correspondientes a widgets que ya no existen de la tabla anterior:
        print('self.pathBD =', self.pathBD)
        print('self.pathBD.get() =', self.pathBD.get())
        try:
            print(f'self.{listaColTablaAnterior[1]} = {self.__dict__[listaColTablaAnterior[1]]}')
            print(f'self.{listaColTablaAnterior[1]}.get() = {self.__dict__[listaColTablaAnterior[1]].get()}') 
        except:
            print('self.{listaColTablaAnterior[1]} ya no existe...')
        
        try:
            print(f'self.{listaAnteriorParaCorroborBash[1]} = {self.__dict__[listaAnteriorParaCorroborBash[1]]}')
            print(f'self.{listaAnteriorParaCorroborBash[1]}.get() = {self.__dict__[listaAnteriorParaCorroborBash[1]].get()}')
        except:
            print(f'self.{listaAnteriorParaCorroborBash[1]} ya no existe...')
            
        try:
            print(f'self.{listaAnteriorParaCorroborBash[2]} = {self.__dict__[listaAnteriorParaCorroborBash[2]]}')
            print(f'self.{listaAnteriorParaCorroborBash[2]}.get() = {self.__dict__[listaAnteriorParaCorroborBash[2]].get()}')
        except:
            print(f'self.{listaAnteriorParaCorroborBash[2]} ya no existe...')
            
        print('---------------------')
                
                
                                                  