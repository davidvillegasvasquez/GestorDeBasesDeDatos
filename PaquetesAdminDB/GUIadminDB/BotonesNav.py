from tkinter import ttk
from PaquetesAdminDB.GUIadminDB.Crear import *
from PaquetesAdminDB.LogicAdminDB.Posicionamiento import *
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import BaseDeDatosTipos
from PaquetesAdminDB.LogicAdminDB.ConexionesAbasesDeDatos import conexiónConBD
from PaquetesAdminDB.GUIadminDB.DescripciónDeLosWidgets import descripWidgetsCuerpoSuperior

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
        nroColEnTablaActual = 0
        for columna in self.columnasDeTablaActual:
            #Recuerde que el indice de elemento en la lista self.columnasDeTablaActual es nroColEnTablaActual. 
            #Reintegramos el nombre de los widgets según columna:
            nombreTxtBox = 'txtBox_' + columna
            #Y así colocamos texto en un ttk.entry, sin usar variable de contro:
            self.__dict__[nombreTxtBox]['state'] = 'normal' #o 'enabled'. Para poder insertar y borrar debemos habilitarlo.
            self.__dict__[nombreTxtBox].delete(0, 'end') #Debemos borrar manualmente lo que había antes en el widget. El end sólo en minúsculas.
            if self.registrosEnTablaActual != []:
                self.__dict__[nombreTxtBox].insert('end', str(self.registrosEnTablaActual[self.posicionFilaActual][nroColEnTablaActual]))
                self.__dict__[nombreTxtBox]['state'] = 'readonly' #O 'disabled'.
                nroColEnTablaActual += 1 
            else:
                messagebox.showinfo(f'Tabla {self.comboBox_Tablas.get()}', f'No hay registros en la tabla {self.comboBox_Tablas.get()}.')    
                break
    def conectandoABaseDeDatosUbicadaEnPathDado(self, *args):
        self.comboBox_Tablas.set('')
        self.objectConnect = conexiónConBD(self.txtBox_PathBD.get(), self.comboBox_tipoBD.get())
        if self.objectConnect.conexión is not None and self.objectConnect is not None:  
            [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Borramos todos los widgets que hayan quedado en cuerpo medio con esta comprensión de lista. Medio palo.
            self.comboBox_Tablas['values'] = self.objectConnect.listaDeTablasEnLaBaseDeDatosConectada() #Tarea: tratar de meter todo esto en una lambda. 
            
    def dibujarWidgetEnCuerpoMedioDeCamposDeTablaSelecionada(self, tablaSeleccionada, *args): #En un método disparado por un evento virtual de widget con capacidad para ello, enlazado por medio de 
    #su atributo .bind (self.comboBox_Tablas.bind("<<ComboboxSelected>>", este método)), si declaro un parámetro formal con un nombre arbitrario en dicho método o función enlazado, en dicho parámetro se depositará
    # el valor seleccionado en dicho widget -una cadena mostrada en este- con el atributo método widget.get(), para este caso, tablaSeleccionada.widget.get()
  
        self.comboBox_Tablas.selection_clear() #Se debe ejecutar necesariamente si el widget está en estado readonly.          
        [widget.destroy() for widget in self.framePadre.cuerpo_medio.grid_slaves()] #Sino al cambiar de campo quedarán los widget del anterior.
        self.posición = -1 #Reseteamos a posición de de partida. 
        #Ahora si dibujamos los nuevos widgets en cuerpo medio según tabla seleccionada:
        self.columnasDeTablaActual = self.objectConnect.listaDecolumnasDeTabla(tablaSeleccionada.widget.get())
        self.widgetCuerpoMedio = crearWidgetsYsusVarControlEnBaseAdescrip(self, self.framePadre.cuerpo_medio, descripWidgetsSegunColumnasDeLaTabla(self.columnasDeTablaActual))
        #Asignamos valores a atributos self.registrosEnTablaActual y self.cantRegistrosTablaActual:
        self.registrosEnTablaActual = self.objectConnect.consultaSql(f'select * from {tablaSeleccionada.widget.get()}')
        self.cantRegistrosTablaActual = len(self.registrosEnTablaActual)
        self.botonPrimer.invoke() 
        
                
                
                                                  