import csv
import numpy as np
import random
from camada import Camada

class Arquivo:
    def __init__(self):
        pass
    
    def get_rede_neural(self,path):
        fp = open(path,"r")
        file = fp.readlines()
        tam = len(file) 
        rede_neural = []
        for k in range(tam):
            pesos = []
            bias = []
            str = file.pop(0)  
            # camd = Camada() 
            lista_pesos = []
            lista_bias = []
            
            if str.find("camada") != -1:                    # Salva a camada
                camada = str.rstrip().split("_")[1]
            elif str.find("entrada") != -1:                 # Salva a entrada
                entrada = str.rstrip().split(" ")[1]
            elif str.find("saida") != -1:                   # Salva a saida
                saida = str.rstrip().split("  ")[1]
            elif str.find("W") != -1:
                str = file.pop(0)
                while str.find("b") == -1:                  # Pega as linhas contendo os pesos
                    pesos = str.rstrip().split(" ")
                    lista_pesos.append(pesos)
                    str = file.pop(0)
                
                str = file.pop(0)                           # Pega o valor do bias
                while str.find("ativacao") == -1:
                    bias = str.rstrip().split(" ")
                    lista_bias.append(bias)
                    str = file.pop(0)
                ativacao = str.rstrip().split(" ")[1]       # Pega o valor da ativacao
            
                str = file.pop(0).strip()                   
                
                # if str == '--':                             # Pegou o final da camada
                #     print("Acabou")
                cmd = Camada(camada, entrada, saida, np.array(lista_pesos,dtype = np.float), np.array(lista_bias,dtype = np.float).transpose(), ativacao)
                rede_neural.append(cmd)
            if(len(file) == 0):
                break
        return rede_neural

    def getEntrada(self,linha,dataset):
        entrada = []
        for i in range(len(dataset[linha])):
            entrada.append(dataset[linha][i])
            print(dataset[linha])
            print(entrada[i])
        return entrada

    def getValorEsperado(self,linha,dim,dataset):
        d = []
        for i in range(len(dataset[linha])):
            if i >= dim:
                d.append(dataset[linha][i])
        return d        
