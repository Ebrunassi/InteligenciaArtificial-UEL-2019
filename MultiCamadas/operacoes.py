class Operacoes:
    
    
    def __init__(self):
        self.vp = 0.0
        self.fp = 0.0
        self.fn = 0.0
        self.vn = 0.0
        pass

    def projecao(self,y):
        maior = 0.0
        index = -1
        
        for i in range(len(y)):
            if maior < y[i][0]:
                maior = y[i][0]
                index = i
                y[index] = 1
        for i in range(len(y)):
            if i != index:
                y[i][0] = 0
        return y

    def projecaoTamanhoUm(self,y):
        if y[0][0] >= 0.5:
            y[0][0] = 1
        else:
            y[0][0] = 0
        return y

    def aplicaTabelaConfusao(self,y,d):
        for i in range (len(y)):
            if(y[i][0] == 1.0):
                if(y[i][0] == d[i][0]):
                    self.vp += 1
                else:
                    self.fp += 1
            elif(y[i][0] == 0.0):
                if(y[i][0] == d[i][0]):
                    self.vn += 1
                else:
                    self.fn += 1
        print("vp : ",self.vp, " - fp : ", self.fp,"\nfn : ",self.fn," - vn : ",self.vn)
    
    def precisao(self):
        return(self.vp/ (self.vp + self.fp) * 100)
        
        

        