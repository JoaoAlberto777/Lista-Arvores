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


    def encontrar_Nos_Filhos(self, No_Pai):
        
        no_pai = self.encontrar_no(self.raiz, No_Pai)

        if no_pai is None:
            return []  
        
        Nos_Filhos = []
        if no_pai.esquerda:
            Nos_Filhos.append(no_pai.esquerda.valor)
        if no_pai.direita:
            Nos_Filhos.append(no_pai.direita.valor)

        return Nos_Filhos

    def encontrar_no(self, no_atual, valor_alvo):
        if no_atual is None:
            return None  
        if no_atual.valor == valor_alvo:
            return no_atual  
        
        no_esquerdo = self.encontrar_no(no_atual.esquerda, valor_alvo)
        no_direito = self.encontrar_no(no_atual.direita, valor_alvo)
        
        return no_esquerdo or no_direito


    
Arvore = ArvoreBinaria()



Arvore.inserir_em_nivel(5)
Arvore.inserir_em_nivel(3)
Arvore.inserir_em_nivel(7)
Arvore.inserir_em_nivel(2)
Arvore.inserir_em_nivel(4)
Arvore.inserir_em_nivel(6)
Arvore.inserir_em_nivel(8)



No_Pai = int(input("Informe o nó que está procurando: "))
Nos_Filhos = Arvore.encontrar_Nos_Filhos(No_Pai)

if Nos_Filhos:
    print(f"Os filhos do no {No_Pai} são: {Nos_Filhos}")
else:
    print(f"O nó {No_Pai} não foi encontrado na árvore ou Não possui filhos.")





