# estrutura de dados lineares:
## Filas
- A fila tem uma estrutura semelhante à pilha, porém com uma diferença conceitual importante: o paradigma por trás da fila é o FIFO - First In, First Out, ou “o primeiro a entrar é o primeiro a sair”.<br>
Pense na fila como uma fila de banco. A pessoa que chegou primeiro vai ser atendida antes de quem chegou depois.<br>
Sendo assim, também há somente duas formas de se manipular uma fila: 
1. Inserir um elemento no final da fila 
2. remover um elemento do início da fila.

### Deque
- A estrutura de dados deque é uma variação da fila que aceita inserção e remoção de elementos tanto do início quanto do final da fila.<br>
Ainda com o exemplo do Banco, uma pessoa idosa que chega é atendida antes, ao mesmo tempo que uma pessoa que entrou no final da fila pode desistir de esperar e sair da fila, uma outra forma de entender esse metodo e como uma junção das estruturas de pilha e fila.

### Fila Circular
- Uma outra variação da fila é a fila circular, onde o ultimo elemento é conectado com o primeiro elemento.<br>
A fila circular busca resolver uma limitação da fila linear, que é lidar com espaços vazios que podem se enfileirar após a retirada de elementos do início da fila.

## Usos
- Um uso fácil de lembrar para a fila é justamente a fila de impressão dos sistemas operacionais: o último trabalho de impressão a ser adicionado à fila será o último a ser impresso.<br>
Além disso, as requisições feitas a um servidor também são organizadas em fila para serem respondidas, e quando alternamos entre programas utilizando o atalho alt+tab, o sistema operacional faz o gerenciamento da ordem utilizando o princípio de lista circular.
[Referencia](https://www.alura.com.br/artigos/estruturas-de-dados-introducao?srsltid=AfmBOorF1JuhgjpDMFLHCm7KT3aWVsh0mAh4cd-i5wpxwMsolA_nM6GT#fila)