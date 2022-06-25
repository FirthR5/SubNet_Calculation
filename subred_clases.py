def fss(x:int):
    return (x&-x)

class Input_Octet_IP:
    SubNet_Class = {
        "A": [128, 1, 3],
        "B": [192, 2, 2],
        "C": [224, 3, 1] #clase D,E
    }
    def Class_Type(self, Oct):
        self.C_N = ""
        if Oct <= self.SubNet_Class["A"][0]:
            self.C_N = list( self.SubNet_Class.keys() )[0]
        elif self.SubNet_Class["B"][0] >= Oct > self.SubNet_Class["A"][0] :
            self.C_N =list( self.SubNet_Class.keys() )[1]
        else:
            self.C_N =list( self.SubNet_Class.keys() )[2]
        return self.C_N
        #Agregar mas clases
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
        self.Red_Num = self.SubNet_Class[Clase_Letra][1]  
        self.Host_Num = self.SubNet_Class[Clase_Letra][2]
        self.Num_Subred = ( 0, 0 )
        self.SR_B = ["","","",""]
        self.SR_N = [0,0,0,0]
        self.zeros = ""
        self.un = ""
        N_Temp = 0
        
        for i in range(0, self.Red_Num):
            self.SR_B[i] = super(Det_SNM, self).Dec_to_Bin(255)
            self.SR_N[i] = 255     
        for i in range(0, self.Host_Num):
            if N >= 8 :
                self.N_Temp = 8
                self.un = "1" * self.N_Temp
            elif 8 > N > 0 :
                self.N_Temp = N
                self.un = "1" * N
                self.zeros = "0" * (8 - self.N_Temp)
            else:
                self.N_Temp = 0
                self.zeros = super(Det_SNM, self).Dec_to_Bin(0)
            self.SR_B[self.Red_Num+i] = self.un + self.zeros     
            self.SR_N[self.Red_Num+i] = int(self.SR_B[self.Red_Num + i], 2)
            
            if 8 > N > 0 :
                self.Num_Subred = (self.Red_Num+i), fss(int(self.SR_B[self.Red_Num+i]))
            self.un = ""
            self.zeros = ""
            N = N - self.N_Temp
        return self.SR_B, self.SR_N, self.Num_Subred

    def get_SN_Binario(self, IP_Oct,Clase_Letra):
        self.Red_Num = self.SubNet_Class[Clase_Letra][1]  
        self.List_IP = [0, 0, 0, 0]
        for i in range(0, self.Red_Num):
            self.List_IP[i] = IP_Oct[i] 
        for i in reversed(range(self.Red_Num, 4)):
            self.List_IP[i] = 0
        return self.List_IP
    
# CODIGO DE GENERADOR DE SUB-REDES

