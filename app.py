import PySimpleGUI as sg


sg.theme('DarkRed')
control_col = sg.Column([
    [sg.Frame('Blur', layout = [[sg.Slider(range = (0,10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout = [[sg.Slider(range = (0,10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Contour', key='-CONTOUR-')],
    [sg.Checkbox('Flip X', key='-FLIPX-'), sg.Checkbox('Flip Y', key='-FLIPY-')],
    [sg.Button('Save image', key='-SAVE-')]
])
image_col = sg.Column([[sg.Image('test.png')]])

layout = [[control_col,image_col]]

window = sg.Window('Editor de imagem', layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    print(values)


window.close()