import matplotlib.pyplot as plt
import csv
import numpy as np
import random
from Estatisticas import Estatistica


def achaReta(dataset,k):
    print('Comeca funcao')
    m = random.uniform(-1,1)
    b = random.uniform(-1,1)
    # m = 1
    # b = 1
    e = pow(10.0,-5)
    
    # e = 0.5
    for i in range(k):
        j = random.randrange(1,len(dataset))
        x1,x2,y = dataset[j]  
        f = x1*m + b - x2
        g = max(e,-y*f)

        # Calculo de 'm'
        if -y * f > e:
            mfc = -y * x1
        else:
            mfc = e
        m = m - (0.1 * mfc)
        # Calculo de 'b'
        if -y * f > e:
            mfb = -y
        else:
            mfb = e
        b = b - (0.1 * mfb)
        # print('f : {} - g : {} - mfc : {} - mfb : {} - m : {} - b : {}'.format(f,b,mfc,mfb,m,b))
    return m,b
    
def whataxis(y,m,b):
    x = (y - b) / m
    print('Axis is : {} '.format(x))
    if x > 1:
        x = 1
    if x < -1:
        x = -1
    return x

def faxis(x):
    x = float(x)
    return float(m*x + b)

dataset = np.genfromtxt('/home/evandro/Documentos/datas/dataset4.csv', delimiter=',')
m,b = achaReta(dataset,20000)

f = lambda x: m*x + b
# plt.plot((-1, 1), (f(-1), f(1)),'black')
x1 = whataxis(-1,m,b)
x2 = whataxis(1,m,b) 

print('1. f({}) = {}     2. f({}) = {}'.format(x1,f(x1),x2,f(x2)))


for cl in [-1,1]:
    valores = dataset[dataset[:,2] == cl]
    plt.plot(valores[:,0], valores[:,1], 'ro' if cl == -1 else 'bo')
cont = -1
# plt.plot((-1, 1), (f(-1), f(1)),'black')
plt.plot((x1,x2),(f(x1),f(x2)),'black')

totalVerdadeiro = 0
totalFalso = 0
verdadeiroPositivo = 0
falsoPositivo = 0
verdadeiroNegativo = 0
falsoNegativo = 0
with open('/home/evandro/Documentos/datas/dataset4.csv') as file:
    data = csv.reader(file)
    for row in data:
        # Conta o numero total de verdadeiros e falsos
        if int(row[2]) == 1:
            totalVerdadeiro += 1
        else:
            totalFalso += 1
        # Vermelho = -1         Azul = 1
        if float(row[1]) > faxis(row[0]):
            if int(row[2]) == -1:
                verdadeiroPositivo += 1
            else:
                falsoPositivo += 1
        else:
            if float(row[2]) == 1:
                verdadeiroNegativo += 1
            else:
                falsoNegativo += 1
    print('total verdadeiro : {}   total falso : {}').format(totalVerdadeiro,totalFalso)
    print('verdadeiro positivo : {}   verdadeiro negativo : {}').format(verdadeiroPositivo,verdadeiroNegativo)
    print('falso positivo : {}   falso negativo : {}').format(falsoPositivo,falsoNegativo)
    est = Estatistica()
    precisao = est.precisao(verdadeiroPositivo,falsoPositivo)
    revocacao = est.revocacao(verdadeiroPositivo,falsoNegativo)
    acuracia = est.acuracia(verdadeiroPositivo,verdadeiroNegativo,falsoPositivo,falsoNegativo)
    medidaF = est.medidaF(precisao,revocacao)
    print('Precisao : {}     Revocacao : {}').format(precisao,revocacao)
    print('Acuracia : {}     Medida F : {} ').format(precisao,medidaF)
plt.show()