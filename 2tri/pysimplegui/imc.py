import PySimpleGUI as sg      

sg.theme('Reddit')

layout = [
    [sg.Text('IMC - Índice de massa  corpórea')],
    [sg.Text('massa  '),sg.Input()],
    [sg.Text('altura '),sg.Input()],
    [sg.Button('Calcular')]
]

window = sg.Window('IMC',layout=layout,font='Monaco 18')

while True:
    event, value = window.read()
    if event == 'QUIT' or event == sg.WIN_CLOSED:
        break