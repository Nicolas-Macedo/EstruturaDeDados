class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.pilha.append(item)

    def desempilhar(self):
        """Remove e retorna o item no topo da pilha."""
        if not self.esta_vazia():
            return self.pilha.pop()
        else:
            return None  # Retorna None se a pilha estiver vazia

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.pilha) == 0

    def tamanho(self):
        """Retorna o tamanho da pilha."""
        return len(self.pilha)

    def topo(self):
        """Retorna o item no topo da pilha sem removê-lo."""
        if not self.esta_vazia():
            return self.pilha[-1]
        else:
            return None  # Retorna None se a pilha estiver vazia

    def __str__(self):
        """Retorna uma representação em string da pilha."""
        return str(self.pilha)


# Exemplo de uso da pilha
pilha = Pilha()

# Empilhando elementos
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

print("Pilha após empilhar 10, 20 e 30:", pilha)

# Desempilhando um elemento
elemento_removido = pilha.desempilhar()
print("Elemento removido:", elemento_removido)
print("Pilha após desempilhar:", pilha)

# Verificando o elemento no topo da pilha
print("Elemento no topo da pilha:", pilha.topo())

# Verificando o tamanho da pilha
print("Tamanho da pilha:", pilha.tamanho())

# Verificando se a pilha está vazia
print("A pilha está vazia?", pilha.esta_vazia())
