from tkinter import messagebox
import os
import sys
from  PaquetesAdminDB.moduloConfiguración import configuración
import psycopg2
import sqlite3

class conexiónConBD:
    """Para postgresql, ubicación es el path de su respectivo archivo .ini. Se debe cerrar la conexión desde el sitio de instanciación, desde el cliente usuaria de la clase."""
    def __init__(self, ubicación, tipo):
        self.conexión = None
        self.path = ubicación
        self.tipo = tipo
        try:
            if self.tipo == 'postgre': self.conexión = psycopg2.connect(**configuración(self.path))
            if self.tipo == 'sqlite' : self.conexión = sqlite3.connect(self.path)  
            
        except:
                messagebox.showerror(message='Ocurrió un error al tratar de hacer conexión con base de datos', title='Error') 
        
    def consultaSql(self, sql, *args): 
        try:
            cursor = self.conexión.cursor()
            resultado = cursor.execute(sql).fetchall()
            cursor.close()
            
        except:
                messagebox.showerror(message='Ocurrió un error con la instrucción sql', title='Error')
        finally:
            return resultado      
        
    def listaDecolumnasDeTabla(self, tabla, *args):
        cursor = self.conexión.cursor()
        cursor.execute('SELECT * FROM products LIMIT 0')
        columnas = [col[0] for col in cursor.description]  #No sirve tupla.                                
        cursor.close()
        return columnas
                                     