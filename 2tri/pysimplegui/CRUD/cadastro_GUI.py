import PySimpleGUI as sg

sg.theme('Reddit')

menu_def = [
    ['Cadastro', ['Carregar ...', 'Pesquisar']],
    ['Ajuda', ['Ajuda','Sobre']]
]

tab_pessoal = [
    [sg.T('CPF:'),sg.Input(key='-CPF-',size=12,enable_events=True),sg.Text('somente números, não digitar pontos e traços ', font='Arial 10', text_color='grey' )],
    [sg.Text('Nome: '),sg.Input(key='-NAME-')],
    [sg.Text('email:'),sg.Input(key='-EMAIL-')]
]

tab_endereco = [
    [sg.Text('Logradouro:'),sg.Input(key='-ADDRESS-')],
    [sg.Text('Numero:'),sg.Input(key='-NUMBER-',size=(6,1)),sg.Text('Complemento:'),sg.Input('optional',key='-COMP-')]
]

tab_telefone = [
    [sg.T('         '),sg.T('DDD'),sg.T('Número     '),sg.T('Tipo')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE1-',s=(10,1)),sg.OptionMenu(values=('Residencial', 'Comercial', 'Recados'),key='-TIPO-F1-')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE2-',s=(10,1)),sg.OptionMenu(values=('Residencial', 'Comercial', 'Recados'),key='-TIPO-F2-')],
    [sg.T('Telefone:'),sg.Input(key='-DDD1-',size=(3,1)),sg.Input(key='-FONE2-',s=(10,1)),sg.OptionMenu(values=('Residencial', 'Comercial', 'Recados'),key='-TIPO-F3-')]
]

tab_grupo = [
    sg.Tab('Dados Pessoais', layout=tab_pessoal),
    sg.Tab('Endereço', layout=tab_endereco),
    sg.Tab('Contato', layout=tab_telefone)
]


layout = [
    [sg.Menu(menu_def)],
    [sg.T('Cadastro de Clientes')],
    [sg.TabGroup([tab_grupo])],
    [sg.VPush()],
    [sg.Push(),sg.Button('Cancelar',button_color='RED'),sg.Button('Salvar')]
]

window = sg.Window('Cadastro de Clientes',layout=layout,size=(800,600),font="Monaco 14",resizable=True,margins=(1,1))

while True:
    event, value = window.read()
    print(event,value)
    if event == sg.WIN_CLOSED:
        break
    if event == '-CPF-':
        digits = '0123456789'
        if value['-CPF-'][-1] not in digits or len(value['-CPF-']) > 11:
            window['-CPF-'].update(value['-CPF-'][:-1])
    if event == 'Pesquisar':
        termo = sg.popup_get_text('Digite o CPF ou o nome:',font='Monaco 14')
        print(termo)


window.close()