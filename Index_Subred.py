import PySimpleGUI as sg
from subred_clases import Input_Octet_IP, Det_SNM
from Subnet_Layout import Estructura

def Check_Octet(Oct):
    if 256 >Oct >= 0 :      return True
    else:                   return False

def Inicio(IP_det_Num, Subredes, IPs_Sub_Gen):
    IP_SN_Num = [0,0,0,0]
    table_content = []
    Salto_SN = 0 #salto
    
    obj_SNM = Det_SNM()
    Clase_Selecta_Let = obj_SNM.Class_Type(IP_det_Num[0])
    #Convierte el Numero Decimal a Octeto Binario.
    IP_det_Bin = [obj_SNM.Dec_to_Bin(x) for x in  IP_det_Num]
    # CANTIDAD DE BITS DIPONIBLES
    Bits_Dis = obj_SNM.Cant_Bits_Disp(Clase_Selecta_Let)    
    # CALCULO DE LA CANTIDAD DE BITS NECESARIOS PARA OBTENER LAS "N" SUB-REDES
    #Num_Subred, iteration
    N_SR_Necesarias = obj_SNM.get_SN_Cant_Bits(Subredes)    
    # IP_SR_Bin, IP_SR_Num, Num_Subred
    IP_SR_Bin, IP_SR_Num, IP_SNM = obj_SNM.SNM_Clase(N_SR_Necesarias[1], Clase_Selecta_Let)
    IP_SN_Bin = obj_SNM.get_SN_Binario(IP_det_Num, Clase_Selecta_Let)
    
    window['txt_Clase'].update(Clase_Selecta_Let)
    window['txt_Bits'].update(Bits_Dis)
    window['txt_N'].update(N_SR_Necesarias[1])
    window['txt_IP_SN'].update(str(IP_SR_Num) +" "+ str(IP_SN_Bin))
    window['txt_Saltos'].update(IP_SNM[1])
    
    I_Salto = IP_SNM[0]
    Oct_Ubic = I_Salto - 1
    for i in range(0, IPs_Sub_Gen+1):
        IP_SN_Bin[I_Salto] =+ Salto_SN
        Salto_SN += IP_SNM[1]
        table_content.append([i, str(IP_SN_Bin)])

        if Salto_SN > 255 :
            if Oct_Ubic >= obj_SNM.SubNet_Class[Clase_Selecta_Let][1] :
                if IP_SN_Bin[Oct_Ubic] >= 254 :
                    IP_SN_Bin[Oct_Ubic] += 1
                    Oct_Ubic -= 1
                Salto_SN -= 256
                IP_SN_Bin[Oct_Ubic]+=1
            else:
                break
    window['tbl_Result'].update(table_content)

window = sg.Window('Subred', Estructura())
while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'btn_Enter':
        IP_det_Num = [ 
            values['Oct_1'], 
            values['Oct_2'], 
            values['Oct_3'], 
            values['Oct_4']
        ]
        N_generar = values['txt_n_generar']
        Subred = values['txt_Subred']
        try:
            if (
                all( Check_Octet(int(item)) for item in IP_det_Num) and 
                all(item.isdigit() for item in IP_det_Num) and
                N_generar.isnumeric() and Subred.isnumeric()
                ):
                Ip_det_Num =[int(x) for x in IP_det_Num]
                Inicio(Ip_det_Num, int(Subred), int(N_generar))
        except  (ValueError, RuntimeError, TypeError, NameError):
            print(TypeError + " " + ValueError + " "+NameError)
    
window.close()  