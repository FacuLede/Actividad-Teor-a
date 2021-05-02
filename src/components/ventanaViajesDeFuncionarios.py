from src.windows import viajesDeFuncionarios
from src.functions import funcionesViajesDeFuncionarios, funciones
import PySimpleGUI as sg
import csv
import os
import json
from datetime import datetime

def generarVentanaViajesDeFuncionarios() :
    """Esta función es la encargada de mantener abierta la ventana donde se va a mostrar
    el resultado de los análisis realizados sobre los datos, también es la que llama a 
    las funciones que realizarán los cálculos necesarios para dichos análisis y los 
    almacenará de forma persistente en un archivo json
    """
    #creo el archivo json donde voy a guardar los resultados
    path_resultados= os.path.join(os.getcwd(), "src", "resultados_json" )
    archivo=open(path_resultados+"/analisisViajesDeFuncionarios.txt","w")

    #traigo los datos sobre losn que voy a trabajar
    path_csv = os.path.join(os.getcwd(), "src", "csvs" )
    datos=open(path_csv+"/registro-viajes-financiados-terceros-20210426.csv","r",encoding="utf8")
    csvreader=csv.reader(datos,delimiter=',')

    #llamo a las funciones     
    csv_lista=funciones.convertir_csv_a_lista(csvreader)
    fecha1=datetime(2019,12,1)
    fecha2=datetime(2019,12,31)
    nombres=funcionesViajesDeFuncionarios.funcQueViajaronEntreDosFechas(csv_lista,fecha1,fecha2)
    nombres_str=funciones.toString(nombres)
    max_jurisdicciones=funcionesViajesDeFuncionarios.getJurisdiccionConMasViajesEnUnAnio(csv_lista,2020)
    destinos_mas_frecuentes=funcionesViajesDeFuncionarios.detinoMasFrecuente(csv_lista)

    #guardo los resultados de las funciones en el archivo json
    diccionario={}
    lista=[]
    diccionario["Funcionarios que viajaron en diciembre de 2019"]=nombres
    diccionario["Jurisdiccion que mas viajes hizo en 2020 y cantidad de viajes"]=max_jurisdicciones
    diccionario["Destinos mas frecuentes"]=[destinos_mas_frecuentes[0],destinos_mas_frecuentes[1],destinos_mas_frecuentes[2]]
    lista.append(diccionario)
    lista_string=json.dumps(lista, indent=4)
    archivo.seek(0)
    archivo.write(lista_string)    
    
    #genero la ventana en la que voy a mostrar los resultados
    ventana_viajes_funcionarios=viajesDeFuncionarios.build(nombres_str,max_jurisdicciones,destinos_mas_frecuentes)
    while True :
        event,values=ventana_viajes_funcionarios.read()
        if event in (sg.WINDOW_CLOSED,"-OK-") :
            break
    ventana_viajes_funcionarios.close()
    archivo.close()