import PySimpleGUI as sg

def Estructura():  
    In_Row, Out_Row, Tableau = Layout_SN_IP()
    layout = [
        [In_Row], 
        [Out_Row],
        [Tableau]
    ]
    return layout

def Layout_SN_IP():
    tam = (5, 15)
    sz = (480, 250)
    sg.theme('SystemDefault')   
    Oct_1 = [[sg.In(key='Oct_1', size=tam)]]
    Oct_2 = [[sg.In(key='Oct_2', size=tam)]]
    Oct_3 = [[sg.In(key='Oct_3', size=tam)]]
    Oct_4 = [[sg.In(key='Oct_4', size=tam)]]
    
    columnas = [[sg.Column(Oct_1, element_justification='c' ), 
        sg.Column(Oct_2, element_justification='c' ),
        sg.Column(Oct_3, element_justification='c' ), 
        sg.Column(Oct_4, element_justification='c' )
        ]]
    In_Row = sg.Frame('Ingreso de datos', layout=
        [
            [sg.Frame('IP', layout =columnas)],
            [sg.Text('Subredes necesarias'), sg.In(key='txt_Subred')],
            [sg.Text('Cantidad IPs a generar'), sg.In(key='txt_n_generar')],
            [sg.Button('Enter', key='btn_Enter')]
        ]
    )
    Out_Row = sg.Frame('Out-Put', layout = 
        [
            [sg.Text('1. Clase: '), sg.Text('-', key='txt_Clase')],
            [sg.Text('2. Bits: '), sg.Text('-', key='txt_Bits')],
            [sg.Text('3. ---: '), sg.Text('-', key='txt_XD')],
            [sg.Text('4. N:'), sg.Text('-', key='txt_N')],
            [sg.Text('5.')],
            [sg.Text('IP SN:'), sg.Text('-', key='txt_IP_SN')],
            [sg.Text('Saltos:'), sg.Text('-', key='txt_Saltos')],
            [sg.Text('IP SR:'), sg.Text('-', key='txt_IP_SR')],
        ], size=sz
    )
    Tableau = sg.Table (
        headings = ['Numero', 'IP'],
        values = table_content,
        expand_x =True,
        hide_vertical_scroll = True,
        key = 'tbl_Result'
    )
    return In_Row, Out_Row, Tableau

def Layout_SN_H():
    
    pass
table_content = []