# Estrutura de dados lineares:
## Lista
As listas (especificamente as listas ligadas) são uma forma de organizar e armazenar dados em programação. Elas funcionam como uma corrente de elos, onde cada elo (chamado de "nó") contém duas coisas:
1. O dado que você quer guardar (por exemplo, um número, texto, etc.).
2. Um ponteiro (ou "endereço") que indica onde está o próximo elo da corrente.

A grande diferença entre listas ligadas e arrays (vetores) é que, nas listas, os elos não precisam estar um ao lado do outro na memória. Cada elo pode estar em um lugar completamente diferente, mas eles permanecem conectados porque cada um sabe onde está o próximo. Isso traz algumas vantagens:
1. Flexibilidade no tamanho:
- Em um array, você precisa definir o tamanho no início, e ele não pode mudar. Já em uma lista, você pode adicionar ou remover elos conforme necessário, sem se preocupar com um limite fixo.
2. Inserção e remoção facilitadas:
- Em um array, se você quiser adicionar ou remover um elemento no meio, precisa "empurrar" ou "puxar" todos os outros elementos para reorganizar o espaço. Isso pode ser lento e trabalhoso.
- Já em uma lista, basta ajustar os ponteiros. Por exemplo, se você quiser adicionar um novo elo no meio, basta fazer o elo anterior apontar para o novo, e o novo apontar para o próximo. Nenhum outro elo precisa ser movido.
3. Uso de memória dinâmica:
- Como os elos não precisam estar em blocos de memória sequenciais, as listas são mais eficientes em situações onde a memória está fragmentada (ou seja, há espaços livres espalhados).

Por outro lado, as listas têm uma desvantagem: para acessar um elemento específico, você precisa percorrer a corrente desde o início até chegar no elo desejado. Isso pode ser mais lento do que em um array, onde você pode acessar qualquer posição diretamente.

[referencia](https://www.alura.com.br/artigos/estruturas-de-dados-introducao?srsltid=AfmBOorF1JuhgjpDMFLHCm7KT3aWVsh0mAh4cd-i5wpxwMsolA_nM6GT#fila)