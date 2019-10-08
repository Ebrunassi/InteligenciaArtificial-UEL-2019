import math
import random

class FuncoesAuxiliares:

    def __init__(self,num):
        self.weightArray = []
        self.bias = 0
        for i in range(num):
            self.weightArray.append(random.randrange(-1,1))
        self.bias = random.randrange(-1,1)
    def getWeights(self):
        return self.weightArray
    
    def getBias(self):
        return self.bias
        
    def sinal(self, soma):
        if soma > 0:
            soma = 1
        elif soma == 0:
            soma = 0
        elif soma < 0:
            soma = -1
        return soma
    
    def sigmoide(self,soma):
        return 1/(1 + (math.exp(-soma)))
    
    def tangHiperbolica(self,soma):
        return (math.exp(soma) - math.exp(-soma)) / (math.exp(soma) + math.exp(-soma))