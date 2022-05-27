import PySimpleGUI as sg

layout = [[]]

window = sg.Window('Editor de imagem', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


window.close()