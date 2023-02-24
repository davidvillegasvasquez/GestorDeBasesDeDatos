from tkinter import messagebox
from  PaquetesAdminDB.LogicAdminDB.moduloConfiguración import configuración
import psycopg2
import sqlite3
from psycopg2 import sql
import os

class conexiónConBD:
    """Para postgresql, ubicación es el path de su respectivo archivo .ini."""
    def __init__(self, ubicación, tipo):
        self.tipo = tipo
        self.path = ubicación
        self.conexión = None
        if self.tipo !='' and self.path !='':
            if os.path.exists(self.path):
                try:
                    if self.tipo == 'postgresql': self.conexión = psycopg2.connect(**configuración(self.path))
                    if self.tipo == 'sqlite' : self.conexión = sqlite3.connect(self.path) 
                except:
                    messagebox.showerror(message='Ocurrió un error al tratar de hacer conexión con base de datos. Revise también si coincide el tipo de base de datos seleccionado.', title='Error') 
                    self.conexión = None
            else:
                messagebox.showwarning(message='Sersiorese de que la base de datos exista y haya dado el path correcto.', title='Atención!!!')     
        else:            
            messagebox.showwarning(message='Sersiorese que proporcionó ambos, path y tipo de base de datos.', title='Atención!!!') 
            
    def consultaSql(self, argsql, *args): 
        resultado = ()
        try:
            cursor = self.conexión.cursor()
            cursor.execute(argsql)
            resultado = cursor.fetchall()
            cursor.close()
        except:
                messagebox.showerror(message='No coincide el tipo de base de datos, u otro error de consulta. Revise.', title='Error')
        finally:
            return resultado
              
    #@consultaSql  ...debo implementar un decorador en el resto de los métodos para eliminar el código repetido. Tarea pendiente.   
    def listaDecolumnasDeTabla(self, tabla, *args):
        cursor = self.conexión.cursor()
        cursor.execute(sql.SQL('SELECT * FROM {} LIMIT 0').format(sql.SQL(tabla))) #SQL string composition.
        listaDeColumnas = [col[0] for col in cursor.description]  #No sirve tupla.                                
        cursor.close()
        return listaDeColumnas
        
    def listaDeTablasEnLaBaseDeDatosConectada(self, *args):
        if self.tipo == 'postgresql': argsql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
        if self.tipo == 'sqlite': argsql = 'SELECT name FROM sqlite_master WHERE type ="table" AND name NOT LIKE "sqlite_%"'
        return self.consultaSql(argsql)     
                
                                     