class No:

    def __init__ (self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.valor, self.valor, self.esquerda and self.direita.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else: 
            self.inserir_em_nivel_recursivo(valor, self.raiz)
        
    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else: 
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else: 
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

    def BuscarValor(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            return self.BuscarValorRecursivo(self.raiz, valor)
            

    def BuscarValorRecursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor > no.valor:
            return self.BuscarValorRecursivo(no.direita, valor)
        else:
            return self.BuscarValorRecursivo(no.esquerda, valor)
    
    
    def mostrar_valores(self):
        valores = []
        self.mostrar_valores_recursivo(self.raiz, valores)
        return valores

    def mostrar_valores_recursivo(self, no, valores):
        if no is not None:
            self.mostrar_valores_recursivo(no.esquerda, valores)
            valores.append(no.valor)
            self.mostrar_valores_recursivo(no.direita, valores)
        
        
        
Arvore = ArvoreBinaria()


Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)


n = int(input("Informe o valor que deseja busca na árvore: "))

if Arvore.BuscarValor(n):
    print(f"O valor {n} esta presente na árvore :)")
    print("Valores na arvore: ", Arvore.mostrar_valores())
else:
    print(f"O valor {n} NÂO esta presente na árvore :(")
    print("Valores na arvore: ", Arvore.mostrar_valores())