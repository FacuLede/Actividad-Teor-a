def convertir_csv_a_lista(csv) :
    """Esta función convierte el iterador recuperado del archivo csv
    en una lista sin el primer elemento donde se encuntran los nombres 
    de los campos
    """
    lista=list(csv)
    lista.reverse()
    lista.pop()
    lista.reverse()
    return lista

def elementosDeCampoSinRepetir(csv_lista,campo):
    """Esta función recibe la lista de listas generada 
    a partir del archivo csv y un campo, y retorna los elemntos
    de ese campo sin repetirse en una lista
    """
    lista=list()
    for i in csv_lista :
        lista.append(i[campo])
    return list(set(lista))

def toString(una_lista) :
    """Convierte una lista recibida por parámetro
    en un string con el formato que se necesitaba 
    para este caso en específico
    """
    string=""
    for i in una_lista :
        string=string+"    "+str(i)+"\n"
    return string




