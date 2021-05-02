from datetime import datetime
from src.functions import funciones

def funcQueViajaronEntreDosFechas(csv_lista,fecha_inicio,fecha_fin) :
    """Esta funcion primeramente filtra los viajes que se dieron entre
    las dos fechas recibidas como parámetro y luego de la lista resultante
    se extraen los nombres de los funcionarios que realizaron dichos viajes
    a otra lista
    """
    viajes_filtrados=filtrarPorFecha(csv_lista,fecha_inicio,fecha_fin)
    nombres=getNombreYApellido(viajes_filtrados)
    return nombres
    
def filtrarPorFecha(csv_lista,fecha_inicio,fecha_fin) :
    """Esta función recibe una lsita de viajes y dos fechas 
    y retorna un subconjunto de la lista conformado por aquellos viajes
    que pertencen al intervalo entre ambas fechas
    """
    return filter(lambda t: fecha_inicio < convertirEnFecha(t[8]) < fecha_fin,csv_lista)

def convertirEnFecha(un_string) :
    """Esta función recibe una fecha en formato string
    y retorna un objeto datetime
    """
    return datetime.strptime(un_string,"%Y-%m-%d")

def getNombreYApellido(csv_lista):
    """Retorna una lista con los nombres y apellidos de 
    los funcionarios que aparecen en la lista recibida como parámetro
    sin repetirse
    """
    nombresApellidos=list()
    for i in csv_lista :
        nombresApellidos.append(i[1]+" "+i[2])
    return list(set(nombresApellidos))

def getViajesEnUnAnio(csv_lista,anio) :
    """Retorna una lista (subconjunto de la lista recibida como parámetro)
    con los viajes que se hayan realizado en el año ingresado como parámetro
    """
    return filter(lambda t: convertirEnFecha(t[8]).year==anio ,csv_lista)

def getMaxJurisdicciones(jurisdicciones,viajes) :
    """Retorna una tupla con el nombre de la jurisdiccion que haya 
    haya realizado mas viajes, y la cantidad de viajes que realizó
    """
    max=("",-1)
    cant=int()
    for i in jurisdicciones :
        cant=0
        for j in viajes :
            if i == j[4] :
                cant=cant+1
        if cant > max[1] :
            max=(i,cant)
    return max

def getJurisdiccionConMasViajesEnUnAnio(viajes,anio) :
    viajes_en_el_anio=getViajesEnUnAnio(viajes,anio)
    jurisdicciones=funciones.elementosDeCampoSinRepetir(viajes_en_el_anio,4)
    return getMaxJurisdicciones(jurisdicciones,viajes)

def detinoMasFrecuente(viajes) :
    """Crea una lista de tuplas donde cada tupla contiene la el nombre de 
    un destino y la cantidad de viajes realizados al mismo, luego ordena dicha lista
    según la cantidad de viajes y finalmente la invierte para que la tupla perteneciente
    al destino con mas viajes quede como primer elemento de la lista
    """
    destinos=funciones.elementosDeCampoSinRepetir(viajes,7)
    cant=int()
    destinos_cant=[]
    for i in destinos :
        cant=0
        for j in viajes :
            if i == j[7] :
                cant=cant+1
        destinos_cant.append((str(i),cant))    
    destinos_cant_ordenado=list(sorted(destinos_cant, key=lambda t : t[1]))
    return list(reversed(destinos_cant_ordenado))


    

