# Importa o módulo 'sys' para acessar a função 'sys.getsizeof()',
# que retorna o tamanho em bytes de um objeto.
import sys

# Função para demonstrar a alocação dinâmica de memória
def demonstrar_alocacao_dinamica(quantidade):
    # Cria uma lista vazia. Inicialmente, a lista não contém elementos.
    lista = []
    
    print("Iniciando a alocação dinâmica de memória...")
    
    # Loop para adicionar elementos à lista
    for i in range(quantidade):
        # Adiciona o valor atual de 'i' à lista
        lista.append(i)
        
        # Mostra o tamanho atual da lista e o uso de memória
        print(f"Elemento {i} adicionado. Tamanho da lista: {len(lista)}. Uso de memória: {sys.getsizeof(lista)} bytes")
    
    # Retorna a lista final
    return lista

# Define a quantidade de elementos a serem adicionados
quantidade_elementos = 10

# Chama a função para demonstrar a alocação dinâmica
lista_final = demonstrar_alocacao_dinamica(quantidade_elementos)

# Imprime a lista final
print("Lista final:", lista_final)