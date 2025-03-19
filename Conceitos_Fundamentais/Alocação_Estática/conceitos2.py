# Importa o módulo 'array' para usar arrays de tamanho fixo
import array

# Função para demonstrar a alocação estática de memória
def demonstrar_alocacao_estatica(tamanho):
    # Cria um array de inteiros com tamanho fixo
    # O array é inicializado com zeros para simular a pré-alocação de memória
    arr = array.array('i', [0] * tamanho)  # 'i' indica que é um array de inteiros
    
    print(f"Array criado com tamanho fixo de {tamanho} elementos.")
    print(f"Uso de memória do array: {arr.itemsize * len(arr)} bytes")  # Tamanho total em bytes
    
    # Preenche o array com valores
    for i in range(tamanho):
        arr[i] = i * 2  # Atribui um valor ao elemento na posição i
    
    # Imprime o array após o preenchimento
    print("Array após preenchimento:")
    for i in range(tamanho):
        print(f"arr[{i}] = {arr[i]}")
    
    # Retorna o array
    return arr

# Define o tamanho fixo do array
tamanho_fixo = 5

# Chama a função para demonstrar a alocação estática
array_final = demonstrar_alocacao_estatica(tamanho_fixo)

# Imprime o array final
print("Array final:", array_final)