"""Plantilla modelo para GUI de navegación entre registros con botones de navegación vacío."""
from PaquetesAdminDB.GUIadminDB.GeometriaBase import Geometria
from PaquetesAdminDB.GUIadminDB.BotonesNav import WidgetMarco
from tkinter import Tk

raiz = Tk()      
WidgetMarco(Geometria(raiz)) 
raiz.mainloop()
