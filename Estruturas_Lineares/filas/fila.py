class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.fila.append(item)

    def desenfileirar(self):
        """Remove e retorna o item no início da fila."""
        if not self.esta_vazia():
            return self.fila.pop(0)
        else:
            return None  # Retorna None se a fila estiver vazia

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.fila) == 0

    def tamanho(self):
        """Retorna o tamanho da fila."""
        return len(self.fila)

    def frente(self):
        """Retorna o item no início da fila sem removê-lo."""
        if not self.esta_vazia():
            return self.fila[0]
        else:
            return None  # Retorna None se a fila estiver vazia

    def __str__(self):
        """Retorna uma representação em string da fila."""
        return str(self.fila)


# Exemplo de uso da fila
fila = Fila()

# Enfileirando elementos
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

print("Fila após enfileirar 10, 20 e 30:", fila)

# Desenfileirando um elemento
elemento_removido = fila.desenfileirar()
print("Elemento removido:", elemento_removido)
print("Fila após desenfileirar:", fila)

# Verificando o elemento na frente da fila
print("Elemento na frente da fila:", fila.frente())

# Verificando o tamanho da fila
print("Tamanho da fila:", fila.tamanho())

# Verificando se a fila está vazia
print("A fila está vazia?", fila.esta_vazia())