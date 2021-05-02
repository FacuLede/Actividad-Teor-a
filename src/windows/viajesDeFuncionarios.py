import PySimpleGUI as sg
from src.functions import funciones

def build (nombres,max_jurisdicciones,destinos_mas_frecuentes) :
    layout=[[sg.Text("Funcionarios que viajaron en diciembre de 2019 :",font=("Helvetica", 20))],
        [sg.Text(nombres,font=("Helvetica", 15))],
        [sg.Text("La jurisdicción que mas viajes realizó en 2020 fue:",font=("Helvetica", 20))],
        [sg.Text("    "+max_jurisdicciones[0]+" con "+str(max_jurisdicciones[1])+" viajes.",font=("Helvetica", 15))],
        [sg.Text("Los destinos mas frecuentados fueron:",font=("Helvetica", 20))],
        [sg.Text("    "+destinos_mas_frecuentes[0][0]+"\n    "+destinos_mas_frecuentes[1][0]+"\n    "+destinos_mas_frecuentes[2][0],font=("Helvetica", 15))],
        [sg.Ok(key="-OK-",font=("Helvetica", 20),size=(7,1))]
    ]
    window=sg.Window("Viajes de funcionarios",layout,margins=(100,60),resizable=True)
    return window
