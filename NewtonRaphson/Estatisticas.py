class Estatistica:
    def __init__(self):
        pass
    def precisao(self,vp,fp):
        vp = float(vp)
        fp = float(fp)
        return vp/(vp + fp)

    def revocacao(self,vp,fn):
        vp = float(vp)
        fn = float(fn)
        return vp/(vp + fn)

    def acuracia(self,vp,vn,fp,fn):
        vp = float(vp)
        vn = float(vn)
        fp = float(fp)
        fn = float(fn)
        return (vp + vn) / (vp + fp + fn + vn)
    
    def medidaF(self,precisao,revocacao):
        precisao = float(precisao)
        revocacao = float(revocacao)
        return (2 * ((precisao * revocacao) / (precisao + revocacao)))