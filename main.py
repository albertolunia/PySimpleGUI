import PySimpleGUI as Sg

layout = [
    [Sg.Text('De', enable_events=True, key='-TEXTO1-'), Sg.Spin(['Centimetros', 'Metros', 'Quilometros']),
     Sg.Text('Para', enable_events=True, key='-TEXTO2-'), Sg.Spin(['Centimetros', 'Metros', 'Quilometros'])],
    [Sg.Input(key='-INPUT-')],
    [Sg.Button('Calcular', key='-BOTAO1-'), Sg.Text(f'Resultado:', key='-RES-')]
]

janela = Sg.Window('Conversor', layout)

while True:
    evento, valores = janela.read()

    if evento == Sg.WIN_CLOSED:
        break

    if evento == '-BOTAO1-':
        if valores[0] == 'Quilometros' and valores[1] == 'Metros':
            vf = int(valores["-INPUT-"]) * 1000
            janela['-RES-'].update(f'Resultado: {vf} Metros')

        if valores[0] == 'Quilometros' and valores[1] == 'Centimetros':
            vf = int(valores["-INPUT-"]) * 100000
            janela['-RES-'].update(f'Resultado: {vf} Centimetros')

        if valores[0] == 'Metros' and valores[1] == 'Quilometros':
            vf = int(valores["-INPUT-"]) / 1000
            janela['-RES-'].update(f'Resultado: {vf} Quilometros')

        if valores[0] == 'Metros' and valores[1] == 'Centimetros':
            vf = int(valores["-INPUT-"]) * 100
            janela['-RES-'].update(f'Resultado: {vf} Centimetros')

        if valores[0] == 'Centimetros' and valores[1] == 'Quilometros':
            vf = int(valores["-INPUT-"]) / 100000
            janela['-RES-'].update(f'Resultado: {vf} Quilometros')

        if valores[0] == 'Centimetros' and valores[1] == 'Metros':
            vf = int(valores["-INPUT-"]) / 100
            janela['-RES-'].update(f'Resultado: {vf} Metros')

janela.close()
