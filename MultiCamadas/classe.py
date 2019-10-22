class Classe:

    def __init__(self):
        self.vp = 0.0
        self.vn = 0.0
        self.fp = 0.0
        self.fn = 0.0
    
    def aplicaTabelaConfusao(self,y,d):
        if(y == 1.0):
            if(y == d):
                self.vp += 1
            else:
                self.fp += 1
        elif(y == 0.0):
            if(y == d):
                self.vn += 1
            else:
                self.fn += 1
    
    def precisao(self):
        if(self.vp + self.fp) == 0:
            return 0.0
        return(self.vp/ (self.vp + self.fp) * 100)
    def revocacao(self):
        return(self.vp/ (self.vp + self.fn) * 100)
