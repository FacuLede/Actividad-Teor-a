from src.windows import vacunasAplicadas
from src.functions import funcionesVacunasAplicadas
from src.functions import funciones
import PySimpleGUI as sg
import csv
import os
import json



def generarVentanaVacunasAplicadas() :
    """Esta función es la encargada de mantener abierta la ventana donde se va a mostrar
    el resultado de los análisis realizados sobre los datos, también es la que llama a 
    las funciones que realizarán los cálculos necesarios para dichos análisis y los 
    almacenará de forma persistente en un archivo json
    """
    #creo el archivo json donde voy a guardar los resultados
    path_resultados= os.path.join(os.getcwd(), "src", "resultados_json" )
    archivo=open(path_resultados+"/analisisVacunasAplicadas.txt","w")

    #traigo los datos sobre losn que voy a trabajar
    path_csv = os.path.join(os.getcwd(), "src", "csvs" )
    datos=open(path_csv+"/Covid19VacunasAgrupadas.csv","r")
    csvreader=csv.reader(datos,delimiter=',')
    
    #llamo a las funciones 
    csv_lista=funciones.convertir_csv_a_lista(csvreader)
    cant_vacunas_aplicadas=funcionesVacunasAplicadas.cantidadTotalDeVacunasAplicadas(csv_lista)
    
    lista_tipos_vacunas=funciones.elementosDeCampoSinRepetir(csv_lista,2)
    vacunas=funciones.toString(lista_tipos_vacunas)    
    dic_cant_tipos=funcionesVacunasAplicadas.cantidadPorCriterio(lista_tipos_vacunas,2,csv_lista)
    vacunas_cant=funcionesVacunasAplicadas.dicToString(dic_cant_tipos)

    provincias=funciones.elementosDeCampoSinRepetir(csv_lista,1)    
    provincia_con_mas_dosis=funcionesVacunasAplicadas.mayorCantidadDeDosis(provincias,csv_lista)

    #guardo los resultados de las funciones en el archivo json
    diccionario={}
    lista=[]
    diccionario["Dosis Aplicadas"]=cant_vacunas_aplicadas
    diccionario["Tipos de vacunas y cantidades"]=dic_cant_tipos
    diccionario["Provincia con mas dosis"]=provincia_con_mas_dosis
    lista.append(diccionario)
    lista_string=json.dumps(lista, indent=4)
    archivo.seek(0)
    archivo.write(lista_string)    
    
    #genero la ventana en la que voy a mostrar los resultados
    ventana_vacunas_aplicadas=vacunasAplicadas.build(cant_vacunas_aplicadas,vacunas,vacunas_cant,provincia_con_mas_dosis)
    while True :
        event,values=ventana_vacunas_aplicadas.read()
        if event in (sg.WINDOW_CLOSED,"-OK-") :
            break
    ventana_vacunas_aplicadas.close()
    archivo.close()