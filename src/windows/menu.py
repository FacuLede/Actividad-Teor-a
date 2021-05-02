import PySimpleGUI as sg 

def build () :
    layout=[
        [sg.Text("¿Qué datos analizamos?",font=("Helvetica", 15))],
        [sg.Button("Viajes de funcionarios",key="-VIAJES-",font=("Helvetica", 15),size=(28,2),border_width=5)],
        [sg.Button("Vacunas contra el COVID \naplicadas en Argentina",key="-VACUNAS-",font=("Helvetica", 15),size=(28,2),border_width=5)],
        [sg.Button("Salir",key="-EXIT-",font=("Helvetica", 15),size=(28,2),border_width=5)]
    ]

    window=sg.Window("Actividad 1 x Python Plus - TEORÍA",layout,margins=(100,60))

    return window