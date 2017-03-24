# Natureza do código - por Daniel Shiffman

### Introdução

*"Eu sou dois com a natureza." - Woody Allen*

<br>
Aqui estamos: o começo. Bem, quase o começo. Se faz algum tempo que você não programa em Processing (ou, ainda, que você não usa qualquer matemática), esta introdução deve trazer de volta à sua mente o modo de pensar computacional antes de chegarmos ao material mais difícil e complexo.

No Capítulo 1, vamos falar sobre o conceito de vetor e como este serve como base para construção de simulações de movimento ao longo do livro. Mas antes de tomar este passo, pensemos sobre o que significa algo se mover pela tela. Vamos começar com uma das mais conhecidas e simples simulações de movimento — a caminhada aleatória. 

### I.1 Caminhada Aleatória

Imagine que você está no meio de uma trave olímpica. A cada dez segundos, você lança uma moeda. Cara, você dá um passo para frente. Coroa, um passo para trás. Isso é uma caminhada aleatória—um percurso definido por uma série de passos aleatórios. Descendo da trave de exercícios para o chão, você pode fazer uma caminhada aleatória em duas dimensões lançando a mesma moeda duas vezes seguindo os resultados:

Jogada 1 | Jogada 2 | Resultado
------------ | ------------- | -------------
Cara | Cara | Passo para frente.
Cara | Coroa | Passo para direita.
Coroa | Cara | Passo para esquerda.
Coroa | Coroa | Passo para trás.

Bom, isso pode parecer um algoritmo particularmente simples. No entanto, caminhadas aleatórias podem ser usadas para modelar fenômenos que acontecem no mundo real, de movimentos de moléculas num gás ao comportamento de um jogador passando o dia em um cassino. Começamos o livro estudando uma caminhada aleatória com três objetivos em mente.

1. Precisamos rever um conceito de programação central para este livro — programação orientada a objetos. O nosso passeador aleatório, random walker, servirá de modelo para como usaremos a programação orientada a objetos para fazer coisas que se movem numa janela do Processing.

2. A caminhada aleatória instiga duas questões que vamos nos perguntar repetidamente neste livro: “Como vamos definir as regras que governam o comportamento dos nossos objetos?” e então, “Como vamos implementar essas regras no Processing?”

3. Ao longo do livro, vamos periodicamente precisar de uma compreensão básica da aleatoriedade, probabilidade e ruído Perlin. A caminhada aleatória nos permitirá demonstar alguns pontos chave que serão úteis mais para frente.

### I.2 A classe Random Walker

Vamos rever um pouco de programação orientada a objetos (POO) primeiramente construindo um objeto Walker. Esta será uma revisão rápida apenas. Se você nunca trabalhou com POO antes, pode ser que queira algo mais completo; Eu sugeriria parar aqui e revisar o básico no site do [Processing](https://processing.org/tutorials/objects/) (página em Inglês) antes de continuar.


Um **objeto** em Processing é uma entidade que possui dados e funcionalidade. Nós queremos projetar um objeto Walker que mantém tanto o registro de seus dados (onde ele existe na tela) quanto tem a capacidade de executar certas ações (como desenhar-se ou dar um passo).

Uma **classe** é o modelo para criar instâncias reais de objetos. Pense em uma classe como um cortador de biscoitos; os objetos são os próprios biscoitos.

Vamos começar definindo a classe Walker - o que significa ser um objeto Walker. O Walker só precisa de dois dados - um número para sua localização x e um para sua localização y.

```java
    class Walker {
      int x;          // Objetos têm dados.
      int y;
```

Cada classe deve ter um construtor, uma função especial que é chamada quando o objeto é criado pela primeira vez. Você pode pensar nisso como o setup() - configuração - do objeto. Lá, inicializaremos a localização inicial do Walker (neste caso, o centro da janela).

```java
    Walker() {    // Os objetos têm um construtor onde eles são inicializados.
     x = width/2;
     y = height/2;
    }
```

Finalmente, além de dados, as classes podem ser definidas com funcionalidades. Neste exemplo, um Walker tem duas funções. Primeiro, escrevemos uma função que permite que o objeto se exiba (como um ponto branco).

```java
void display() {    // Os objetos têm funções.
    stroke(0);
    point(x,y);
  }
```

A segunda função direciona o objeto Walker para dar um passo. Agora, é aqui que as coisas ficam um pouco mais interessantes. Lembra-se de quando estavámos andando aleatoriamente no chão? Bem, agora podemos usar uma janela no Processing para fazer a mesma coisa. Existem quatro passos possíveis. Um passo para a direita pode ser simulado incrementando x (x ++); Para a esquerda, decrementando x (x -); Para a frente, indo para baixo um pixel (y ++); E para trás, subindo um pixel (y -). Como escolhemos uma dessas quatro possibilidades? Anteriormente, afirmamos que poderíamos virar duas moedas. No processamento, no entanto, quando queremos escolher aleatoriamente de uma lista de opções, podemos escolher um número aleatório usando random ().

```java
void step() {
    int choice = int(random(4));    // 0, 1, 2, ou 3
```

A linha de código acima escolhe um número de ponto flutuante aleatório entre 0 e 4 e converte-o em um número inteiro, com um resultado de 0, 1, 2 ou 3. Tecnicamente falando, o número mais alto nunca será 4.0, mas sim 3.999999999 (Com tantos 9s quanto casas decimais existentes); Uma vez que o processo de conversão para um número inteiro sai da casa decimal, o int mais alto que podemos obter é 3. Em seguida, tomamos o passo apropriado (esquerda, direita, para cima ou para baixo) dependendo do número aleatório que foi escolhido.

```java
if (choice == 0) {    // A escolha aleatória determina nosso passo.
      x++;
    } else if (choice == 1) {
      x--;
    } else if (choice == 2) {
      y++;
    } else {
      y--;
    }
  }
}
```

Agora que escrevemos a classe, é hora de fazer um objeto Walker na parte principal do nosso sketch - setup() e draw(). Assumindo que estamos procurando modelar uma única caminhada aleatória, declaramos uma variável global do tipo Walker.

```java
Walker w;    // Um objeto Walker
```
Em seguida, criamos o objeto no setup() chamando o construtor com o novo operador.

### Exemplo I.1: Caminhada aleatória tradicional

Cada vez que você vê o cabeçalho de Exemplo neste livro, significa que há um exemplo de código correspondente disponível no [GitHub](https://github.com/shiffman/The-Nature-of-Code-Examples).

```java
void setup() {
  size(640,360);
  w = new Walker();    // Crie o Walker.
  background(255);
}
```

Finalmente, durante cada ciclo através do draw(), pedimos ao Walker para dar um passo e desenhar um ponto.

```java
void draw() {
  w.step();    // Chame as funções do Walker.
  w.display();
}
```

Uma vez que desenhamos o plano de fundo apenas uma vez no setup(), em vez de limpá-lo continuamente cada vez através do draw(), vemos a trilha da caminhada aleatória em nossa janela do Processing.

Existem algumas melhorias que poderíamos fazer para o caminhante aleatório. Primeiro, as escolhas deste Walker estão limitadas a quatro opções - para cima, para baixo, para a esquerda e para a direita. Mas qualquer pixel dado na janela tem oito possíveis vizinhos, e uma nona possibilidade é ficar no mesmo lugar.

![1](https://github.com/arteprog/Processando-Processing/blob/master/natureza-do-codigo/assets/intro_01.png?raw=true)

Figura I.1

Para implementar um objeto Walker que pode pisar em qualquer pixel vizinho (ou ficar parado), poderíamos escolher um número entre 0 e 8 (nove escolhas possíveis). No entanto, a maneira mais eficiente para escrever o código seria a de simplesmente escolher a partir de três passos possíveis ao longo do eixo x (-1, 0, ou 1) e três passos possíveis ao longo do eixo y.

```java
 void step() {
    int stepx = int(random(3))-1;    // Fornece -1, 0 ou 1
    int stepy = int(random(3))-1;
    x += stepx;
    y += stepy;
  }
```

Ainda mais longe, poderíamos usar números de ponto flutuante (ou seja, números decimais) para x e y e mover o Walker de acordo com um valor arbitrário aleatório entre -1 e 1.

```java
void step() {
    float stepx = random(-1, 1);    // Fornece qualquer número de ponto flutuante entre -1,0 e 1,0
    float stepy = random(-1, 1);
    x += stepx;
    y += stepy;
  }
```
  
  
  
[FINAL]
Começamos este capítulo falando sobre como a aleatoriedade pode ser uma muleta. De muitas maneiras, é a resposta mais óbvia para certas perguntas que fazemos continuamente, como deve esse objeto se mover? Que cor deve ter? Esta resposta óbvia, contudo, também pode ser preguiçosa.
À medida que terminamos a introdução, é importante notar que poderíamos facilmente cair na armadilha de usar o ruído Perlin como uma muleta também. Como deve esse objeto se mover? Ruído Perlin! Que cor deve ter? Ruído Perlin! O quão rápido ele deve crescer? Ruído Perlin!
O ponto de tudo isto não é dizer que você deve ou não usar aleatoriedade. Ou que você deve ou não usar o ruído Perlin. O ponto é que as regras do seu sistema são definidas por você, e quanto maior a sua caixa de ferramentas, mais escolhas você vai ter como você implementar essas regras. O objetivo deste livro é encher sua caixa de ferramentas. Se tudo o que você sabe é aleatóriedade, então o sua estratégia de design é limitada. Claro, o ruído Perlin ajuda, mas você vai precisar de mais. Muito mais.
Acho que estamos prontos para começar.
