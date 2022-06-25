def fss(x:int):
    return (x&-x)

class Input_Octet_IP:
    SubNet_Class = {
        "A": [128, 1, 3],
        "B": [192, 2, 2],
        "C": [224, 3, 1]
    }
    def Check_Octet(self, Oct):
        if (Oct >= 0 and Oct < 256):
            return True
        else:
            return False

    def Class_Type(self, Oct):
        if(Oct <= self.SubNet_Class["A"][0]):
            return list( self.SubNet_Class.keys() )[0]

        elif(Oct > self.SubNet_Class["A"][0] and Oct <= self.SubNet_Class["B"][0]):
            return list( self.SubNet_Class.keys() )[1]

        else:
            return list( self.SubNet_Class.keys() )[2]

    def Dec_to_Bin(self, Oct):
        self.Octeto = format(Oct, "b")
        return str(self.Octeto).rjust(8,'0')

class Det_SNM(Input_Octet_IP):
    def Cant_Bits_Disp(self, Le_Classe):
        self.Le_Bits = 8
        if(Le_Classe == "A"):
            self.Le_Bits *=3
        elif(Le_Classe == "B"):
            self.Le_Bits *=2
        else:
            self.Le_Bits *=1

        return self.Le_Bits-2

    #ToDo Later: Zzzz
    #def _3_Bits_Disponibles:

    # Cantidad de bits necesarios para obtener las 35 subredes
    def get_SN_Cant_Bits(self,Num_Sub_Req):
        self.Deux = 2
        self.Num_Subred = 0
        self.N_Exp = -1
        while(self.Num_Subred < Num_Sub_Req):
            self.N_Exp += 1
            self.Num_Subred = (self.Deux ** self.N_Exp) - 2
        return self.Num_Subred, self.N_Exp

    #Sacar SNM
    
    def SNM_Clase(self, N, Clase_Letra):
        N_Temp = 0
        self.Red_Num = self.SubNet_Class[Clase_Letra][1]  
        self.Host_Num= self.SubNet_Class[Clase_Letra][2]
        self.zeros = ""
        self.un =""
        self.Num_Subred =(0,0)
        self.SR_B=["","","",""]
        self.SR_N=[0,0,0,0]
        for i in range(0, self.Red_Num):
            self.SR_B[i] = super(Det_SNM, self).Dec_to_Bin(255)
            self.SR_N[i] = 255     
        for i in range(0, self.Host_Num):
            self.un = ""
            self.zeros = ""
            if( N >= 8):
                self.N_Temp = 8
                self.un = "1"* self.N_Temp

            elif( N>0 and N<8):
                self.N_Temp = N
                self.un = "1" * N
                self.zeros = "0" * (8-self.N_Temp)

            else:
                self.N_Temp = 0
                self.zeros = super(Det_SNM,self).Dec_to_Bin(0)
            
            
            self.SR_B[self.Red_Num+i] = self.un + self.zeros     
            self.SR_N[self.Red_Num+i] = int(self.SR_B[self.Red_Num+i], 2)
            
            if(N>0 and N <8):
                self.Num_Subred = (self.Red_Num+i), fss(int(self.SR_B[self.Red_Num+i]))
            N = N - self.N_Temp

        return self.SR_B, self.SR_N, self.Num_Subred

    def get_SN_Binario(self, IP_Oct,Clase_Letra):
        self.Red_Num = self.SubNet_Class[Clase_Letra][1]  
        self.List_IP = [0,0,0,0]
        for i in range(0, self.Red_Num):
            self.List_IP[i]= IP_Oct[i] 

        for i in reversed(range(self.Red_Num,4)):
            self.List_IP[i] = 0
        
        return self.List_IP

def Inicio():
    IP_SR_Bin = ["","","",""]
    IP_SR_Num = [0,0,0,0]
    # LISTO
    IP_det_Num = [0,0,0,0]      
    IP_det_Bin = ["","","",""] 
    Clase_Selecta_Let=""
    IP_SN_Bin = ["","","",""]   # 1
    IP_SN_Num = [0,0,0,0]

    # INGRESO DE VALORES(0-255) de los octetos
    obj_SNM = Det_SNM()
    print("Ingrese la Direccion IP\n")

    for i in range(0, 4):
        IP_det_Num[i] = int(input("Ingrese valor de octeto %s: " % (i+1)))
        
        check_Oct = obj_SNM.Check_Octet(IP_det_Num[i] ) # Comprubea si el octeto ingresado esta en el rango 0-255
        #ToDo: Implementar si el numero ingresado esta correcto
        if(i == 0):
            Clase_Selecta_Let = obj_SNM.Class_Type(IP_det_Num[i])
        
        IP_det_Bin[i] = obj_SNM.Dec_to_Bin(IP_det_Num[i])        #Convierte el Numero Decimal a Octeto Binario.

    Subredes = int(input("Ingrese cuantas subredes utilizara: "))
    IPs_Sub_Gen = int(input("Ingrese cuantas IPs de subredes quiere generar: "))

    Bits_Dis = obj_SNM.Cant_Bits_Disp(Clase_Selecta_Let)    # CANTIDAD DE BITS DIPONIBLES

    #Num_Subred, iteration
    N_SR_Necesarias = obj_SNM.get_SN_Cant_Bits(Subredes)    # CALCULO DE LA CANTIDAD DE BITS NECESARIOS PARA OBTENER LAS "N" SUB-REDES

    IP_SR_Bin, IP_SR_Num, IP_SNM = obj_SNM.SNM_Clase(N_SR_Necesarias[1], Clase_Selecta_Let)# IP_SR_Bin, IP_SR_Num, Num_Subred

    IP_SN_Bin = obj_SNM.get_SN_Binario(IP_det_Num, Clase_Selecta_Let)

    print(f"1.- IP Ingresasa: {IP_det_Num}\nClase: {Clase_Selecta_Let}\n") 
    print(f"2.- Bits disponibles: {Bits_Dis}")

    print(f"4.-Numero de subredes \n{str(tuple(N_SR_Necesarias))}\nN = {N_SR_Necesarias[1]}\n-------------")
    print(f"5.- IP SNM: {str(tuple(IP_SNM))}" )
    print(f"{IP_SN_Bin} {IP_SR_Num}")      
    print(f"{IP_SNM[1]}\n-------")

    Salto_SN = 0 #salto
    I_Salto = IP_SNM[0]
    Oct_Ubic = I_Salto - 1
    for i in range(0, IPs_Sub_Gen+1):
        IP_SN_Bin[I_Salto] =+ Salto_SN
        print(str(i) + str(IP_SN_Bin))
        Salto_SN += IP_SNM[1]

        if(Salto_SN>255):
            if(Oct_Ubic >= obj_SNM.SubNet_Class[Clase_Selecta_Let][1]):
                if(IP_SN_Bin[Oct_Ubic] >= 254):
                    IP_SN_Bin[Oct_Ubic] += 1
                    Oct_Ubic -= 1
                Salto_SN -= 256
                IP_SN_Bin[Oct_Ubic]+=1
            else:
                break

    print("FIN.")
    
Inicio()
