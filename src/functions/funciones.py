def convertir_csv_a_lista(csv) :
    lista=list(csv)
    lista.reverse()
    lista.pop()
    lista.reverse()
    return lista

def elementosDeCampoSinRepetir(csv_lista,campo):
    lista=list()
    for i in csv_lista :
        lista.append(i[campo])
    return list(set(lista))

def toString(una_lista) :
    string=""
    for i in una_lista :
        string=string+"    "+str(i)+"\n"
    return string




