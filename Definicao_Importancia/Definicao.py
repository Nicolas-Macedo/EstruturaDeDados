def contar_frequencia_palavras(texto):
    palavras = texto.split()  # Divide o texto em palavras
    frequencia = []  # Lista para armazenar pares (palavra, contagem)

    for palavra in palavras:
        encontrada = False
        # Percorre a lista para verificar se a palavra já foi contada
        for i, (p, cnt) in enumerate(frequencia):
            if p == palavra:
                frequencia[i] = (p, cnt + 1)  # Atualiza a contagem
                encontrada = True
                break
        if not encontrada:
            frequencia.append((palavra, 1))  # Adiciona nova palavra

    return frequencia

# Exemplo de uso
texto = "o rato roeu a roupa do rei de roma e o rato roeu tudo"
resultado = contar_frequencia_palavras(texto)
print(resultado)

'''
Em um codigo sem tratamendo de estrutura de dados o codigo perde desempenho deixando de ser eficiente a medida que o texto 
aumenta o tempo de execução cresce tornando o codigo lento, e o codigo fica mais complexo pois para cada palavra é necessario
percorrer a lista de palavras para verificar se a palavra ja foi contada, e se não foi contada adicionar a palavra na lista.
'''