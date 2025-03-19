class Lista:
    def __init__(self):
        self.lista = []

    def adicionar(self, item):
        """Adiciona um item ao final da lista."""
        self.lista.append(item)

    def remover(self, item):
        """Remove a primeira ocorrência de um item da lista."""
        if item in self.lista:
            self.lista.remove(item)
        else:
            print(f"Item '{item}' não encontrado na lista.")

    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return len(self.lista) == 0

    def tamanho(self):
        """Retorna o tamanho da lista."""
        return len(self.lista)

    def buscar(self, item):
        """Retorna o índice de um item na lista. Retorna -1 se não encontrado."""
        if item in self.lista:
            return self.lista.index(item)
        else:
            return -1

    def acessar(self, indice):
        """Retorna o item no índice especificado. Retorna None se o índice for inválido."""
        if 0 <= indice < len(self.lista):
            return self.lista[indice]
        else:
            return None  # Retorna None se o índice for inválido

    def __str__(self):
        """Retorna uma representação em string da lista."""
        return str(self.lista)


# Exemplo de uso da lista
lista = Lista()

# Adicionando elementos
lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(30)

print("Lista após adicionar 10, 20 e 30:", lista)

# Removendo um elemento
lista.remover(20)
print("Lista após remover 20:", lista)

# Verificando se a lista está vazia
print("A lista está vazia?", lista.esta_vazia())

# Verificando o tamanho da lista
print("Tamanho da lista:", lista.tamanho())

# Buscando um elemento
indice = lista.buscar(30)
if indice != -1:
    print("Elemento 30 encontrado no índice:", indice)
else:
    print("Elemento 30 não encontrado na lista.")

# Acessando um elemento por índice
elemento = lista.acessar(1)
if elemento is not None:
    print("Elemento no índice 1:", elemento)
else:
    print("Índice inválido.")