def cantidadTotalDeVacunasAplicadas(csvlista) :
    cant_vacunas=0
    #next(csvreader)
    for i in csvlista :
        cant_vacunas=cant_vacunas+int(i[3])+int(i[4])
    return cant_vacunas

def dicToString(diccionario) :
    string=""
    keys=diccionario.keys()
    for i in keys :
        string=string+"    "+i+": "+str(diccionario[i])+"\n"
    return string

def cantidadPorCriterio(lista,k,csv_lista) :
    """Esta función retorna la cantidad de vacunas 
    asosiada a cada elemento de la lista "lista" de 
    un campo recibido por parámetro.
    Los datos del campo recibido deben ser del mismo tipo
    que los contenidos en la lista "lista" recibida
    """
    cant=int()
    diccionario={}
    for i in lista :
        cant=0
        for j in csv_lista :
            if j[k] == i :
                cant=cant+int(j[3])+int(j[4])
        diccionario[i]=cant
    return diccionario

def mayorCantidadDeDosis(provincias,csv_lista) :
    """Esta función retorna una tupla que contiene
    el nombre de al provincia en la que mas dosis se
    aplicaron y dicha cantida de dosis 
    """
    cantidades=cantidadPorCriterio(provincias,1,csv_lista)
    claves=cantidades.keys()
    max=("",-1)
    for i in claves :
        if int(cantidades[i]) > max[1] :
            max=(i,cantidades[i])
    return max




