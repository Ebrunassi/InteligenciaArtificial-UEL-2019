import numpy as np
import random
from Weight import FuncoesAuxiliares
# y = sigma(x1.w1 + x2.w2 + x3.w3 + ... + xn.wn + b)
axis = []
wgts = []
func = FuncoesAuxiliares()
wgts = func.getWeights()
soma = 0

# Somatorio de (x1.w1 + x2.w2 + x3.w3 + ... + x30.w30)
print('vetor x gerado : ')
for i in range(0,30,1):
    axis.append(random.uniform(-1,1))
    print(': {}'.format(axis[i]))
    soma += (axis[i] * wgts[i])
soma += 0.5 # Valor do 'bias'

linear = soma
print('Funcao linear : {}'.format(linear))
sinal = func.sinal(soma)
print('Funcao sinal : {}'.format(sinal))
sinal = func.sigmoide(soma)
print('Funcao sigmoide : {}'.format(sinal))
sinal = func.tangHiperbolica(soma)
print('Funcao tangente hiperbolica : {}'.format(sinal))

