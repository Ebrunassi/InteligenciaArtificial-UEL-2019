import numpy as np
import math

class Camada:
    # matrix = np.array([[1,2,3],[2,4,1]],dtype = np.float)
    def __init__(self, camada, entrada, saida, pesos, bias, ativacao):
        self.camada = camada
        self.entrada = entrada
        self.saida = saida
        self.pesos = np.array(pesos, dtype = np.float)
        self.bias = np.array(bias, dtype = np.float)
        self.ativacao = ativacao
        
    def soma_matrix(self,mat1,mat2):
        if(len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
            return None
        result = []
        for i in range(len(mat1)):   
            result.append([])
            for j in range(len(mat1[0])):
                result[i].append(mat1[i][j] + mat2[i][j])
        return result

    def sigmoide(self,mat):
        result = []
        for i in range(len(mat)):   
            result.append([])
            for j in range(len(mat[0])):
                result[i].append( 1/(1 + (math.exp(-mat[i][j]))))
        return result

    def getCamada(self):
        return(self.camada)
    def getEntrada(self):
        return(self.entrada)
    def getSaida(self):
        return(self.saida)
    def getPeso(self):
        return(self.pesos)
    def getBias(self):
        return(self.bias)
    def getAtivacao(self):
        return(self.ativacao)
    
        
