import csv
import numpy as np
import random
from Estatisticas import Estatistica
from Neuronio import FuncoesAuxiliares


def treinamento(dataset,numIteracoes):
    func = FuncoesAuxiliares(5)         # Cria os pesos e bias dentro da classe
    pesos = func.getWeights()       # Pega o vetor de 'pesos'
    bias = func.getBias()
    lr = 0.1
    for i in range(numIteracoes):
        j = random.randrange(1,len(dataset))
        x = []
        for k in range (len(dataset[j])): # Pegando os valores de 'x' do arquivo
            x.append(dataset[j][k])
        d = dataset[j][5]               # Valor esperado
        soma = 0
        for k in range(len(pesos)):
            soma = soma + (x[k] * pesos[k])
        # soma += func.getBias()
        soma = soma + bias

        sigmoide = func.sigmoide(soma)
        derivadas = (2*sigmoide - 2*d) * (sigmoide * (1-sigmoide))
        for k in range(len(pesos)):
            pesos[k] = pesos[k] - (lr * ( derivadas * x[k]))
        bias = bias - lr * (derivadas * 1)
        # if(i % 20 == 0):
        #     print("{}.").format(i)
        #     print("     Pesos : {}").format(pesos)
        #     print("     Bias : {0:.5f}").format(bias)
        #     print("     Sigmoide : {:.5f}").format(sigmoide)
        #     print("     Esperado : {}" .format(d))
        #     print("     Erro : {}".format((d-sigmoide) * (d-sigmoide) ))
        sigmoide  = 0
    if numIteracoes == 10000:
        print("k = {}".format(numIteracoes))    
        print("     Peso : [", end='')
        for l in range(len(pesos)):
            print("{:.5f},".format(pesos[l]), end='')
        print("]")
        # print("     Pesos : {}").format(pesos)
        print("     Bias : {0:.5f}".format(bias))
        # print("     Sigmoide : {:.5f}").format(sigmoide)
        # print("     Esperado : {}" .format(d))
        # print("     Erro : {}".format((d-sigmoide) * (d-sigmoide) ))
    else:
        print("k = {}".format(numIteracoes))
    return pesos,bias

def verificaNeuronio(pesos,bias):
    dataset = np.genfromtxt('/home/evandro/Documentos/dataset1_teste.csv', delimiter=',')
    # Verdadeiro = 1    Falso = 0
    verdadeiroPositivo = 0.0
    falsoPositivo = 0.0    
    verdadeiroNegativo = 0.0
    falsoNegativo = 0.0
    for k in range(len(dataset)):
        d = dataset[k][5]
        x = []

        # Pega os valores de entrada
        for i in range(len(dataset[k])):
            x.append(dataset[k][i])
        
        # Calcula o valor de saida do neuronio
        soma = 0
        for i in range(len(pesos)):
            soma = soma + (x[i] * pesos[i])
        soma = soma + bias
        func = FuncoesAuxiliares(20)
        sigmoide = func.sigmoide(soma)

        # if sigmoide >= 0.5 and d == 1:
        #     verdadeiroPositivo = verdadeiroPositivo + 1
        # elif sigmoide >= 0.5 and d == 0:
        #     falsoPositivo = falsoPositivo + 1
        # elif sigmoide < 0.5 and d == 0:
        #     verdadeiroNegativo = verdadeiroNegativo + 1
        # elif sigmoide < 0.5 and d == 1:
        #     falsoNegativo = falsoNegativo + 1

        if sigmoide <= 0.5 and d == 0:
            verdadeiroPositivo = verdadeiroPositivo + 1
        elif sigmoide <= 0.5 and d == 1:
            falsoPositivo = falsoPositivo + 1
        elif sigmoide > 0.5 and d == 1:
            verdadeiroNegativo = verdadeiroNegativo + 1
        elif sigmoide > 0.5 and d == 0:
            falsoNegativo = falsoNegativo + 1
    print("verdadeiroPositivo : {}".format(verdadeiroPositivo))
    print("falsoPositivo : {}".format(falsoPositivo))
    print("verdadeiroNegativo : {}".format(verdadeiroNegativo))
    print("falsoNegativo : {}".format(falsoNegativo))

    precisao = (verdadeiroPositivo / (verdadeiroPositivo + falsoPositivo) ) * 100
    revocacao = (verdadeiroPositivo / (verdadeiroPositivo + falsoNegativo) ) * 100
    print("Precisao : {:.2f}%".format(precisao))
    print("Revocacao : {:.2f}%".format(revocacao))

dataset = np.genfromtxt('/home/evandro/Documentos/dataset1_treinamento.csv', delimiter=',')
pesos = []
bias = 0
pesos, bias = treinamento(dataset,10000)
verificaNeuronio(pesos,bias)