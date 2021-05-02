from src.windows import menu
import PySimpleGUI as sg
from src.functions import funcionesVacunasAplicadas
from src.components import ventanaVacunasAplicadas, ventanaViajesDeFuncionarios

def generarVentanaMenu() :
    ventana_menu=menu.build()
    while True :
        event,values=ventana_menu.read()
        if event in (sg.WINDOW_CLOSED,"-EXIT-") :
            break
        if event == "-VIAJES-" :
            ventana_menu.hide()
            ventanaViajesDeFuncionarios.generarVentanaViajesDeFuncionarios()
            ventana_menu.un_hide()    
        if event == "-VACUNAS-" :
            ventana_menu.hide()
            ventanaVacunasAplicadas.generarVentanaVacunasAplicadas()
            ventana_menu.un_hide()                
    ventana_menu.close()