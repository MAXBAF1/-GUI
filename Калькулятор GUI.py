import PySimpleGUI as sg
from math import *

layout = [ [sg.InputText(size = (36,1), k = "T")],
           [sg.Button('%', size = (6,2)), sg.Button('CE', size = (6,2)), sg.Button('C', size = (6,2)), sg.Button('⌫', size = (6,2))],
           [sg.Button('1/x', size = (6,2)), sg.Button('x^2', size = (6,2)), sg.Button('sqrt(x)', size = (6,2)), sg.Button('/', size = (6,2))],
           [sg.Button('7', size = (6,2)), sg.Button('8', size = (6,2)), sg.Button('9', size = (6,2)), sg.Button('*', size = (6,2))],
           [sg.Button('4', size = (6,2)), sg.Button('5', size = (6,2)), sg.Button('6', size = (6,2)), sg.Button('-', size = (6,2))],
           [sg.Button('1', size = (6,2)), sg.Button('2', size = (6,2)), sg.Button('3', size = (6,2)), sg.Button('+', size = (6,2))],
           [sg.Button('+/-', size = (6,2)), sg.Button('0', size = (6,2)), sg.Button(',', size = (6,2)), sg.Button('=', size = (6,2))] ]

window = sg.Window('Калькулятор', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == '0':
        window["T"].Update(values['T'] + '0')
    elif event == '1':
        window["T"].Update(values['T'] + '1')
    elif event == '2':
        window["T"].Update(values['T'] + '2')
    elif event == '3':
        window["T"].Update(values['T'] + '3')
    elif event == '4':
        window["T"].Update(values['T'] + '4')
    elif event == '5':
        window["T"].Update(values['T'] + '5')
    elif event == '6':
        window["T"].Update(values['T'] + '6')
    elif event == '7':
        window["T"].Update(values['T'] + '7')
    elif event == '8':
        window["T"].Update(values['T'] + '8')
    elif event == '9':
        window["T"].Update(values['T'] + '9')
    elif event == '+':
        window["T"].Update(values['T'] + '+')
    elif event == '-':
        window["T"].Update(values['T'] + '-')
    elif event == '*':
        window["T"].Update(values['T'] + '*')
    elif event == '/':
        window["T"].Update(values['T'] + '/')
    elif event == '+/-':
        window["T"].Update(float(values['T'])*-1)
    elif event == '%':
        window["T"].Update(values['T'] + '%')
    elif event == ',':
        window["T"].Update(values['T'] + '.')
    elif event == '⌫':
        window["T"].Update((values['T'])[:-1])
    elif event == 'C':
        window["T"].Update('')
    elif event == 'CE':
        window["T"].Update('')
    elif event == '1/x':
        window["T"].Update(1/float(values['T']))
    elif event == 'x^2':
        window["T"].Update(float(values['T'])**2)
    elif event == 'sqrt(x)':
        window["T"].Update(sqrt(float(values['T'])))
    elif event == '=':
        try:
            window["T"].Update(eval(values['T']))
        except: window["T"].Update('ERROR')


window.close()