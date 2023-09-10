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


    def encontrar_caminho(self, valor_alvo):
        return self.encontrar_caminho_recursivo(self.raiz, valor_alvo, [])

    def encontrar_caminho_recursivo(self, no, valor_alvo, caminho):
        if no is None:
            return None

        caminho.append(no.valor)

        if no.valor == valor_alvo:
            return caminho.copy()

        caminho_esquerda = self.encontrar_caminho_recursivo(no.esquerda, valor_alvo, caminho.copy())
        caminho_direita = self.encontrar_caminho_recursivo(no.direita, valor_alvo, caminho.copy())

        if caminho_esquerda:
            return caminho_esquerda
        if caminho_direita:
            return caminho_direita

        return None



    
Arvore = ArvoreBinaria()



Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)



valor_procurado = int(input("Informe o nó que está procurando: "))
caminho = Arvore.encontrar_caminho(valor_procurado)

if caminho:
    print(f"O caminho até o nó {valor_procurado} é {caminho}")
else:
    print(f"O nó {valor_procurado} não foi encontrado na árvore.")



