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
    
    
    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia!")
            return []
        else:
            return self.mostrar_pre_ordem_recursiva(self.raiz)
    
    
    def mostrar_pre_ordem_recursiva(self, no):
        valores_visitados = []
        if no is not None:
            valores_visitados.append(no.valor)
            if no.esquerda is not None:
                valores_visitados.extend(self.mostrar_pre_ordem_recursiva(no.esquerda))
            if no.direita is not None:
                valores_visitados.extend(self.mostrar_pre_ordem_recursiva(no.direita))
        return valores_visitados

   
    
Arvore = ArvoreBinaria()



Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)

print("Raiz - Esquerda - Direia")
print(Arvore.mostrar_pre_ordem())


