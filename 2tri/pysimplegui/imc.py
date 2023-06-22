import PySimpleGUI as sg      

# incluir o tema da interface
sg.theme('TanBlue')


layout = [
    [sg.Text('IMC')],
    [sg.Text('Massa  '),sg.Input(key='-MASS-',size=(5,1))],
    [sg.Text('Altura '),sg.Input(key='-HIGH-',size=(5,1))],
    [sg.Push(),sg.Button('Calcular'),sg.Button('Sair'),sg.Push()]
]

window = sg.Window('IMC',layout=layout,font='Monaco 18')

while True:
    event, value = window.read()
    print(event,value)
    if event == 'Calcular':
        massa=float(value['-MASS-'])
        altura=float(value['-HIGH-'])
        imc = massa / (altura**2)
        sg.Popup(f'Seu imc é {imc:.2f}', font='26')
    if event == 'Sair' or event == sg.WIN_CLOSED:
        break

window.close()