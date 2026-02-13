class ENDERECO :
    def __init__(self,logadouro,bairro,cidade,uf):
        self.logadouro=logadouro
        self.bairro=bairro 
        self.cidade=cidade
        self.uf=uf

        def enderecocomplero(self):
            return f"{self.logadouro}  - `{self.bairro}  - `{self.cidade} / `{self.uf}   "
        
