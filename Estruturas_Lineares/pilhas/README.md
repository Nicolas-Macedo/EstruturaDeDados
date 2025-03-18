# Estrutura de dados Lineares:
## Pilha 
- A pilha é uma estrutura de dados que, assim como o array, é similar a uma lista. O paradigma principal por trás da pilha é o LIFO - Last In, First Out, ou “o último a entrar é o primeiro a sair”.<br>
Pensemos como se fosse uma pilha de pratos, o primeiro prato a sair e obrigatoriamente o ultimo que foi colocado na fila,se tentamos retirar o ultimo prato da pilha, tudo vai desabar. Sendo assim o ultimo a ser emplihado e o primeiro a ser retirado.<br>
Ao contrario de um array, as linguagens de programação normalmente não tem metodos nativos para criação e manipulação de pilhas, sendo os métodos possíveis para manipular os dados de uma pilha:
1. Inserir um elemento ao topo da pilha.
2. Remover um elemento do topo da pilha.

- O caso de uso mais famoso da pilha é a call stack ou pilha de chamadas de um programa que está sendo executado: a ordem de execução dos processos “chamados” por um programa via funções ou métodos obedece o princípio de pilha.<br>
Outro recurso que utilizamos todos os dias e que utiliza pilhas para funcionar é o mecanismo de “voltar” e “avançar” páginas dos navegadores (representado normalmente por setas para a esquerda e direita). Os endereços visitados vão se empilhando; ao chamarmos a função de “voltar”, o último endereço visitado - ou seja, o que está no topo da pilha - é o primeiro a ser visualizado.

[Referencia](https://www.alura.com.br/artigos/estruturas-de-dados-introducao?srsltid=AfmBOorF1JuhgjpDMFLHCm7KT3aWVsh0mAh4cd-i5wpxwMsolA_nM6GT#fila)