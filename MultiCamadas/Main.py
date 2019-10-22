from neuronio import Neuronio
from arquivo import Arquivo
import csv
import numpy as np
from camada import Camada
from operacoes import Operacoes
from classe import Classe

arq = Arquivo()
rede_neural = arq.get_rede_neural('/home/evandro/Documentos/vscode-workspace/MultiCamadas/MDML_NN.txt')

fp = open('/home/evandro/Documentos/vscode-workspace/MultiCamadas/MDML_test.csv',"r")
file = fp.readlines()
tam = len(file) 
op = Operacoes()
classes_lista = []
# Abrindo o arquivo teste
for k in range(tam):
    if k == 0:
        dimensao = file[k].strip().split(":")[1]
        print("Dimensao :",dimensao)
    elif k == 1:
        classes = file[k].strip().split(":")[1]
        print("Classes :",classes)
        for l in range(int(classes)):
            cl = Classe()
            classes_lista.append(cl)        
    elif k > 1:
        entrada = []
        d_esperado = []
        linha = file[k].rstrip().split(",")
        for i in range(len(linha)):
            if i < int(dimensao):
                x = []
                x.append(float(linha[i]))
                entrada.append(x)
            else:
                x = []
                x.append(float(linha[i]))
                d_esperado.append(x)
        entrada = np.array(entrada,dtype = np.float).reshape(int(dimensao),1)
        s = entrada

        d_esperado = np.array(d_esperado,dtype = np.float).reshape(int(classes),1)
        # Sendo 's' a entrada, vamos inseri-la na rede neural de 'i' camadas
        for i in range (len(rede_neural)):
            # Faz a transposta da matrix d_esperado
            saida = int(rede_neural[i].getSaida())      # Pega o numero de saidas que tem essa camada
            
            pesos = rede_neural[i].getPeso()            # Pega a matrix peso dessa camada
            bias = rede_neural[i].getBias()             # Pega a matrix bias dessa camada
            r = np.matmul(pesos,s)                        # r = pesos * entrada
            t = rede_neural[i].soma_matrix(r,bias)              # t = r + bias
            t = np.array(t, dtype = np.float).reshape(saida,1)
            t = rede_neural[i].sigmoide(t)                      # y = sigmoide(t)
            t = np.array(t, dtype = np.float).reshape(saida,1)
            s = t                                          # Atualiza a entrada da proxima camada
        if len(t) != 1:
            y_projetado = op.projecao(t)
        else:
            y_projetado = op.projecaoTamanhoUm(t)
        
        for l in range(len(classes_lista)):
            classes_lista[l].aplicaTabelaConfusao(t[l][0], d_esperado[l][0])

for l in range(len(classes_lista)):
    print("             Precisao  Revocao")
    print("Class ",l," : ", round(classes_lista[l].precisao(),2) , " - ", round(classes_lista[l].revocacao(),2))






        
        
        
    

    
    



# dataset = np.genfromtxt('/home/evandro/Documentos/vscode-workspace/MultiCamadas/ds1_cl4_dim2_treinamento.csv',delimiter=',')

# arq = Arquivo()
# arq.getEntrada(4,dataset)