import math
class FuncoesAuxiliares:

    def __init__(self):
        self.weightArray = []
        self.weightArray.append(-0.061219)
        self.weightArray.append(-0.976196)
        self.weightArray.append(-0.325755)
        self.weightArray.append(-0.675635)
        self.weightArray.append(0.588569)
        self.weightArray.append(-0.377570)
        self.weightArray.append(0.057066)
        self.weightArray.append(-0.668703)
        self.weightArray.append(0.203964)
        self.weightArray.append(-0.474057)
        self.weightArray.append(0.308158)
        self.weightArray.append(0.378429)
        self.weightArray.append(0.496303)
        self.weightArray.append(-0.098917)
        self.weightArray.append(-0.832357)
        self.weightArray.append(-0.542046)
        self.weightArray.append(0.826675)
        self.weightArray.append(-0.695244)
        self.weightArray.append(0.651634)
        self.weightArray.append(0.076685)
        self.weightArray.append(0.992269)
        self.weightArray.append(-0.843649)
        self.weightArray.append(-0.114643)
        self.weightArray.append(-0.786694)
        self.weightArray.append(0.923796)
        self.weightArray.append(-0.990732)
        self.weightArray.append(0.549821)
        self.weightArray.append(0.634606)
        self.weightArray.append(0.737389)
        self.weightArray.append(-0.831128)

    def getWeights(self):
        return self.weightArray
    
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
