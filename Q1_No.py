class No:

    def __init__ (self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.valor, self.valor, self.esquerda and self.direita.valor)
    
raiz = No(10)
no_esquerda = No(5)
no_direita = No(15)

raiz.esquerda = no_esquerda
raiz.direita = no_direita

print(raiz)


