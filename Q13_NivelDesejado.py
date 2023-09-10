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


    def nos_em_nivel(self, nivel_desejado):
        return self.nos_em_nivel_recursivo(self.raiz, 1, nivel_desejado)

    def nos_em_nivel_recursivo(self, no, nivel_atual, nivel_desejado):
        if no is None:
            return []

        if nivel_atual == nivel_desejado:
            return [no.valor]

        nos_nivel_esquerda = self.nos_em_nivel_recursivo(no.esquerda, nivel_atual + 1, nivel_desejado)
        nos_nivel_direita = self.nos_em_nivel_recursivo(no.direita, nivel_atual + 1, nivel_desejado)

        return nos_nivel_esquerda + nos_nivel_direita

   
    
Arvore = ArvoreBinaria()



Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(1)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(8)

nivel = int(input("Informe o nivel desejado: "))

print(f"Nos no nivel {nivel} são {Arvore.nos_em_nivel(nivel)}")





