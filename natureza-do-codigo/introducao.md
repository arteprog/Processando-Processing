# Natureza do código - por Daniel Shiffman

### Introdução

*"Eu sou dois com a natureza." - Woody Allen*

<br>
Aqui estamos: o começo. Bem, quase o começo. Se faz algum tempo que você não programa em Processing (ou, ainda, que você não usa qualquer matemática), esta introdução deve trazer de volta à sua mente o modo de pensar computacional antes de chegarmos ao material mais difícil e complexo.

No Capítulo 1, vamos falar sobre o conceito de vetor e como este serve como base para construção de simulações de movimento ao longo do livro. Mas antes de tomar este passo, pensemos sobre o que significa algo se mover pela tela. Vamos começar com uma das mais conhecidas e simples simulações de movimento — a caminhada aleatória. 

### I.1 Caminhada Aleatória

Imagine que você está no meio de uma trave olímpica. A cada dez segundos, você lança uma moeda. Cara, você dá um passo para frente. Coroa, um passo para trás. Isso é uma caminhada aleatória—um percurso definido por uma série de passos aleatórios. Descendo da trave de exercícios para o chão, você pode fazer uma caminhada aleatória em duas dimensões lançando a mesma moeda duas vezes seguindo os resultados:

**Jogada 1** | **Jogada 2** | **Resultado**
------------ | ------------- | -------------
Cara | Cara | Passo a frente.
Cara | Coroa | Passo a direita.
Coroa | Cara | Passo a esquerda.
Coroa | Coroa | Passo para trás.
