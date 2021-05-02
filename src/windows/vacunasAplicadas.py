import PySimpleGUI as sg 

def build(cant_vacunas,tipos_de_vacunas,tipos_de_vacunas_cant,provincia_max) :
    layout=[
        [sg.Text("Se han aplicado un total de "+str(cant_vacunas)+" vacunas.",font=("Helvetica", 20))],
        [sg.Text("Vacunas: ",font=("Helvetica", 20))],
        [sg.Text(tipos_de_vacunas,font=("Helvetica", 15))],
        [sg.Text("Cantidad de dosis aplicadas de cada vacuna: ",font=("Helvetica", 20))],
        [sg.Text(tipos_de_vacunas_cant,font=("Helvetica", 15))],        
        [sg.Text("La provincia con mayor cantidad de dosis fue "+provincia_max[0]+"\ncon un total de "+str(provincia_max[1])+" dosis.",font=("Helvetica", 20))],
        [sg.Ok(key="-OK-",font=("Helvetica", 20),size=(7,1))]
    ]
    ventana_vacunas_aplicadas=sg.Window("Vacunas contra el COVID aplicadas en Argentina ",layout,margins=(100,60),resizable=True)
    return ventana_vacunas_aplicadas