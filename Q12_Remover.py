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


    def mostrar_in_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia!!")
            return []
        else:
            return self.mostrar_in_ordem_recursivo(self.raiz)

    def mostrar_in_ordem_recursivo(self, no):
        valores_visitados = []
        if no is not None:
            if no.esquerda is not None:
                valores_visitados.extend(self.mostrar_in_ordem_recursivo(no.esquerda))
            valores_visitados.append(no.valor)
            if no.direita is not None:
                valores_visitados.extend(self.mostrar_in_ordem_recursivo(no.direita))
        return valores_visitados


    def remover(self, valor):
        self.raiz = self.remover_recursivo(self.raiz, valor)

    def remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self.remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            no.valor = self.encontrar_sucessor_inordem(no.direita).valor
            no.direita = self.remover_recursivo(no.direita, no.valor)

        return no

    def encontrar_sucessor_inordem(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    

Arvore = ArvoreBinaria()



Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)

print("Arvore Antes da Remoção: ")
print(Arvore.mostrar_in_ordem())

n = int(input("Informe o numero a ser removido: "))


Arvore.remover(n)


print("Arvore apos à remoção: ")
print(Arvore.mostrar_in_ordem())




