import PySimpleGUI as sg

sg.popup('Vamos calcular o produto de dois números!',font="Comfortaa 28")
numero_1 = sg.popup_get_text('Digite um número',size=10,font="Comfortaa 28")
numero_2 = sg.popup_get_text('Digite outro número',size=10,font="Comfortaa 28")
produto = float(numero_1) * float(numero_2)
sg.popup(produto,font="Comfortaa 28")

