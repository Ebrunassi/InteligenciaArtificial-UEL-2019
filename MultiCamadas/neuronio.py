import math
import random

class Neuronio:

    def __init__(self,num):
        self.pesos = []
        self.bias = 0.0
        for i in range(num):
            self.pesos.append(random.uniform(-1,1))
        self.bias = random.uniform(-1,1)

    def getPesos(self):
        return self.pesos
    
    def getBias(self):
        return self.bias