import PySimpleGUI as sg

control_col = sg.Column([
    [sg.Button('test')]
])
image_col = sg.Column([[sg.Image('test.png')]])

layout = [[image_col]]

window = sg.Window('Editor de imagem', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


window.close()