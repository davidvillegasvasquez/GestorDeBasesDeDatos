from tkinter import messagebox
from  PaquetesAdminDB.LogicAdminDB.moduloConfiguración import configuración
import psycopg2
import sqlite3
from psycopg2 import sql

class conexiónConBD:
    """Para postgresql, ubicación es el path de su respectivo archivo .ini. Se debe cerrar la conexión desde el sitio de instanciación, desde el cliente usuaria de la clase. Tarea: ver si se puede hacer un decorador para los métodos y no repetir tanto el código parecido."""
    def __init__(self, ubicación, tipo):
        self.conexión = None
        self.path = ubicación
        self.tipo = tipo
        try:
            if self.tipo == 'postgre': self.conexión = psycopg2.connect(**configuración(self.path))
            if self.tipo == 'sqlite' : self.conexión = sqlite3.connect(self.path)  
            
        except:
                messagebox.showerror(message='Ocurrió un error al tratar de hacer conexión con base de datos', title='Error') 
        
    def consultaSql(self, argsql, *args): 
        resultado = ()
        try:
            cursor = self.conexión.cursor()
            cursor.execute(argsql)
            resultado = cursor.fetchall()
            cursor.close()
        except:
                messagebox.showerror(message='Ocurrió un error con la instrucción sql al parecer.', title='Error')
        finally:
            return resultado
                  
    #@consultaSql  ...debo implementar un decorador en el resto de los métodos para eliminar el código repetido. Tarea pendiente.   
    def listaDecolumnasDeTabla(self, tabla, *args):
        cursor = self.conexión.cursor()
        cursor.execute(sql.SQL('SELECT * FROM {} LIMIT 0').format(sql.SQL(tabla))) #SQL string composition.
        columnas = [col[0] for col in cursor.description]  #No sirve tupla.                                
        cursor.close()
        return listaDeColumnas
        
    def listaDeTablasEnLaBaseDeDatos(self, *args):
        cursor = self.conexión.cursor()
        if self.tipo == 'postgre': argsql = 'SELECT table_name FROM information_schema.tables WHERE table_schema="public"'
        if self.tipo == 'sqlite': argsql = 'SELECT name FROM sqlite_master WHERE type ="table" AND name NOT LIKE "sqlite_%"'
        cursor.execute(argsql)
        listaDeTablas = cursor.fetchall()
        cursor.close()
        return listaDeTablas       
                                     