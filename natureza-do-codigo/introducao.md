# Natureza do código - por Daniel Shiffman

## Introdução

*"Eu sou dois com a natureza." - Woody Allen*

<br>

Aqui estamos: o começo. Bem, quase o começo. Se faz algum tempo que você não programa em Processing (ou, ainda, que você não usa um pouco de matemática), esta introdução deve trazer de volta à sua mente o modo de pensar computacional antes de chegarmos ao material mais difícil e complexo.

No Capítulo 1, vamos falar sobre o conceito de vetor e como este serve como base para construção de simulações de movimento ao longo do livro. Mas antes de darmos este passo, vamos pensar sobre o que significa algo se mover pela tela. Vamos começar com uma das mais conhecidas e simples simulações de movimento — a caminhada aleatória. 

### I.1 Caminhada Aleatória

Imagine que você está no meio de uma trave olímpica. A cada dez segundos, você lança uma moeda. Cara, você dá um passo para frente. Coroa, um passo para trás. Isso é uma caminhada aleatória—um percurso definido por uma série de passos aleatórios. Descendo da trave de exercícios para o chão, você pode fazer uma caminhada aleatória em duas dimensões lançando a mesma moeda duas vezes seguindo os resultados:

Jogada 1 | Jogada 2 | Resultado
------------ | ------------- | -------------
Cara | Cara | Passo para frente.
Cara | Coroa | Passo para direita.
Coroa | Cara | Passo para esquerda.
Coroa | Coroa | Passo para trás.

Bom, isso pode parecer um algoritmo particularmente simples. No entanto, caminhadas aleatórias podem ser usadas para modelar fenômenos que acontecem no mundo real, de movimentos de moléculas em um gás até o comportamento de um jogador passando o dia em um cassino. Começamos o livro estudando uma caminhada aleatória com três objetivos em mente.

1. Precisamos rever um conceito de programação central para este livro — programação orientada a objetos. O nosso passeador aleatório, *random walker*, servirá de modelo para como usaremos a programação orientada a objetos para fazer coisas que se movem numa janela do Processing.

2. A caminhada aleatória instiga duas questões que vamos nos perguntar repetidamente neste livro: “Como vamos definir as regras que governam o comportamento dos nossos objetos?” e então, “Como vamos implementar essas regras no Processing?”

3. Ao longo do livro, nós vamos periodicamente precisar de uma compreensão básica da aleatoriedade, probabilidade e ruído Perlin. A caminhada aleatória nos permitirá demonstrar alguns pontos chave que serão úteis mais para frente.

### I.2 A classe Random Walker

Vamos rever um pouco de programação orientada a objetos (POO) primeiramente construindo um objeto Walker ("Caminhante"). Esta será apenas uma revisão rápida. Se você nunca trabalhou com POO antes, pode ser que queira algo mais completo; Eu sugeriria parar aqui e revisar o básico no site do [Processing](https://processing.org/tutorials/objects/) (página em Inglês) antes de continuar.


Um **objeto** em Processing é uma entidade que possui dados e funcionalidade. Nós queremos projetar um objeto Walker que mantém tanto o registro de seus dados (onde ele existe na tela) quanto tem a capacidade de executar certas ações (como se desenhar ou dar um passo).

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

A segunda função direciona o objeto Walker para dar um passo. Agora, é aqui que as coisas ficam um pouco mais interessantes. Se lembra de quando estávamos andando aleatoriamente pelo chão? Bem, agora podemos usar uma janela no Processing para fazer a mesma coisa. Existem quatro passos possíveis. Um passo para a direita pode ser simulado incrementando x (x ++); Para a esquerda, decrementando x (x --); Para a frente, indo para baixo um pixel (y ++); E para trás, subindo um pixel (y --). Como escolhemos uma dessas quatro possibilidades? Anteriormente, afirmamos que poderíamos virar duas moedas. No Processing, no entanto, quando queremos escolher aleatoriamente de uma lista de opções, podemos escolher um número aleatório usando random().

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

Agora que escrevemos a classe, é hora de fazer um objeto Walker na parte principal do nosso *sketch* - setup() e draw(). Assumindo que estamos procurando modelar uma única caminhada aleatória, declaramos uma variável global do tipo Walker.

```java
Walker w;    // Um objeto walker
```
Em seguida, criamos o objeto no setup() chamando o construtor com o novo operador.

#### Exemplo I.1: Caminhada aleatória tradicional

*Cada vez que você vê o cabeçalho de Exemplo neste livro, significa que há um exemplo de código correspondente disponível no* [GitHub](https://github.com/shiffman/The-Nature-of-Code-Examples).

```java
void setup() {
  size(640,360);
  w = new Walker();    // Crie o walker.
  background(255);
}
```

Finalmente, durante cada ciclo através do draw(), pedimos ao Walker para dar um passo e desenhar um ponto.

```java
void draw() {
  w.step();    // Chame as funções do walker.
  w.display();
}
```

Uma vez que desenhamos o plano de fundo apenas uma vez no setup(), em vez de limpá-lo continuamente cada vez através do draw(), vemos a trilha da caminhada aleatória em nossa janela do Processing.

Existem algumas melhorias que poderíamos fazer para o caminhante aleatório. Primeiro, as escolhas deste Walker estão limitadas a quatro opções - para cima, para baixo, para a esquerda e para a direita. Mas qualquer pixel da janela tem oito possíveis vizinhos, e uma nona possibilidade é ficar no mesmo lugar.

![1](https://github.com/arteprog/Processando-Processing/blob/master/natureza-do-codigo/assets/intro_01.png?raw=true)

Figura I.1

Para implementar um objeto Walker que pode pisar em qualquer pixel vizinho (ou ficar parado), poderíamos escolher um número entre 0 e 8 (nove escolhas possíveis). No entanto, a maneira mais eficiente para escrever este código seria a de simplesmente escolher a partir de três passos possíveis ao longo do eixo x (-1, 0, ou 1) e três passos possíveis ao longo do eixo y.

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
  
Todas estas variações na caminhada aleatória "tradicional" têm uma coisa em comum: a qualquer momento no tempo, a probabilidade de que o Walker dê um passo em uma determinada direção é igual à probabilidade de que o Walker dê um passo em qualquer direção. Em outras palavras, se houver quatro passos possíveis, há uma chance de 1 em 4 (ou 25%) que o Walker irá dar qualquer passo. Com nove passos possíveis, é uma chance de 1 em 9 (ou 11,1%). 

Convenientemente, é assim que a função random() funciona. O gerador de números aleatórios do Processing (que opera nos bastidores) produz o que é conhecido como distribuição "uniforme" de números. Podemos testar esta distribuição com um *sketch* no Processing que sorteia um número aleatório de cada vez e utiliza o resultado para definir a altura de um retângulo.

![random1.2](https://github.com/arteprog/Processando-Processing/blob/master/natureza-do-codigo/assets/randomDistribution.jpg?raw=true)

#### Exemplo 1.2: Distribuição aleatória de números

```java
int[] randomCounts; // um array que registra qual a frequência que um número aleatório é sorteado

void setup(){
 size(640, 240);
 randomCounts = new int[20];
}

void draw(){
 background(255);
 
 int index = int(random(randomCounts.length)); // sorteia um número pseudo-randômico e incrementa o conta
 randomCounts[index]++;
 
 stroke(0);
 fill(175);
 int w = width/randomCounts.length;

 for (int x = 0; x < randomCounts.length; x++){ // desenhandoos resultados
   rect(x*w, height-randomCounts[x], w-1, randomCounts[x]);
 }
}
```

A captura de tela acima mostra o resultado do *sketch* sendo executado por alguns minutos. Observe como cada barra do gráfico difere em altura. Nosso tamanho de amostra (ou seja, o número de números aleatórios que escolhemos) é bastante pequeno e existem algumas discrepâncias ocasionais, em que determinados números são selecionados com mais frequência. Com o tempo, com um bom gerador de números aleatórios, isso seria o mesmo.

---
**Números Pseudo-Randômicos**

Os números randômicos que obtemos utilizando a função random() não são realmente randômicos; portanto são chamados de "pseudo-randômicos". Eles são o resultado de funções matemáticas que simulam randomicidade. A função pode gerar um padrão ao longo do tempo, mas esse período é tão longo para nós que o padrão é imperceptível. Os números "pseudo-randômicos" funcionam tão bem quanto os randômicos nas aplicações de Processing.
---

#### Exercício I.1

Crie um caminhante aleatório que tenha a tendência de se mover para baixo e para a direita (Veremos a solução para isso na próxima seção).

### I.3 Probabilidade e distribuições não uniformes

Lembra quando você começou a programar em Processing? Talvez você queira desenhar muitos círculos na tela. Então você disse a si mesmo: “Ah, eu sei. Vou desenhar todos esses círculos em locais aleatórios, com tamanhos e cores aleatórias”. Em um sistema de computação gráfica, muitas vezes é mais fácil semear um sistema com aleatoriedade. Neste livro, no entanto, nós estamos a procura de construir sistemas modelados com base no que vemos na natureza. Um padrão de aleatoriedade não é uma solução particularmente cuidadosa para um problema de design – em particular, o tipo de problema que envolve a criação de uma simulação orgânica ou de aparência natural.

Com alguns truques, nós podemos modificar a maneira como usamos random() para produzir distribuições “não uniformes” de números aleatórios. Isso será útil ao longo do livro, quando examinarmos diversos cenários diferentes. Quando examinamos algoritmos genéticos, por exemplo, nós precisaremos de uma metodologia para realizar a “seleção” – quais membros da nossa população devem ser selecionados para passar seu DNA para a próxima geração? Lembra do conceito de sobrevivência do mais apto? Digamos que temos uma população de macacos evoluindo. Nem todos os macacos terão chances iguais de reprodução. Para simular a evolução Darwiniana, não podemos simplesmente escolher dois macacos aleatórios para serem os pais. Precisamos que os mais “adequados” tenham maior probabilidade de serem escolhidos. Precisamos definir a “probabilidade do mais apto”. Por exemplo, um macaco particularmente rápido e forte pode ter 90% de chance de procriar, enquanto um macaco mais fraco tem apenas 10% de chance.

Vamos fazer uma pausa aqui e dar uma olhada nos princípios básicos da probabilidade. Primeiro, examinaremos a probabilidade de um único evento, ou seja, a probabilidade de um determinado evento ocorrer.

Se você tem um sistema com um certo número de resultados possíveis, a probabilidade de ocorrência de um determinado evento é igual ao número de resultados que se qualificam como aquele evento dividido pelo número total de todos os resultados possíveis. O lançamento da moeda é um exemplo simples - tem apenas dois resultados possíveis: cara ou coroa. Só existe uma maneira de virar cara. A probabilidade de que a moeda dê cara, portanto, é dividida por dois: 1/2 ou 50%.

Pegue um baralho de cinquenta e duas cartas. A probabilidade de tirar um ás desse baralho é:

número de ases / número de cartas = 4/52 = 0,077 = ~ 8%

A probabilidade de tirar um diamante é:

número de diamantes / número de cartas = 13/52 = 0,25 = 25%

Também podemos calcular a probabilidade de vários eventos ocorrerem em sequência. Para fazer isso, simplesmente multiplicamos as probabilidades individuais de cada evento.

A probabilidade de uma moeda dar cara três vezes seguidas é:

(1/2) * (1/2) * (1/2) = 1/8 (ou 0,125)

... o que significa que uma moeda vai dar cara três vezes seguidas em uma em cada oito vezes (cada "vez" sendo três lançamentos).

#### Exercício I.2

Qual é a probabilidade de tirar dois ases seguidos de um baralho de cinquenta e duas cartas?

Existem algumas maneiras pelas quais podemos usar a função random() com probabilidade no código. Uma técnica é preencher um *array* com uma seleção de números - alguns dos quais serão repetidos - e, em seguida, escolher números aleatórios desse *array* e gerar eventos com base nessas escolhas.

```java
nt[] stuff = new int[5]

stuff[0] = 1; // 1 será guardado no array duas vezes, aumentando a probabilidade de seleciona-lo
stuff[1] = 1;

stuff[2] = 2;
stuff[3] = 3;
stuff[4] = 3;

int index = int(random(stuff.length)); // selecionando um elemento do array
```

A execução desse código produzirá 40% de chance de imprimir o valor 1, 20% de chance de imprimir 2 e 40% de chance de imprimir 3.

Também podemos pedir um número aleatório (vamos simplificar e apenas considerar valores de ponto flutuante aleatório entre 0 e 1) e permitir que um evento ocorra apenas se nosso número aleatório estiver dentro de um determinado intervalo. Por exemplo:

```java
float prob = 0.10; // probabilidade de 10%

float r = random(1); // um valor de ponto flutuante aleatório entre 0 e 1

If our random number is less than 0.1, try again!

if (r < prob) { // se nosso número aleatório for menor que 0.1, tente novamente!
   // tente novamente!
}
```

Este método também pode ser aplicado para múltiplos resultados. Digamos que o Resultado A tenha 60% de chance de acontecer, o Resultado B, uma chance de 10% e o Resultado C, uma chance de 30%. Implementaremos isso no código, escolhendo um *float* aleatório e vendo em que intervalo ele irá cair.

- entre 0,00 e 0,60 (60%) –> Resultado A
- entre 0,60 and 0,70 (10%) –> Resultado B
- entre 0,70 e 1,00 (30%) –> Resultado C

```java
float num = random(1);

if (num < 0.6) { // se o número aleatório for menor que 0,6
  println("Resultado A");

} else if (num < 0.7) { // entre 0,6 e 0,7
  println("Resultado B");

} else { // maior que 0,7
  println("Resultado C");
}

```

Poderíamos usar a metodologia acima para criar um *walker* ("caminhante") aleatório que tende a se mover para a direita. Aqui está um exemplo de um *walker* com as seguintes probabilidades:

- chance de subir: 20%
- chance de descer: 20%
- chance de mover para a esquerda: 20%
- chance de mover para a direita: 40%

**INSERIR FIGURA DE EXEMPLO**

Exemplo I.3: O *walker* que tende se mover para a direita

```java
void step() {
 
    float r = random(1);

    if (r < 0.4) { // chance de 40% de se mover para a direita!
      x++;
    } else if (r < 0.6) {
      x--;
    } else if (r < 0.8) {
      y++;
    } else {
      y--;
    }
  }
```

#### Exercício I.3

Crie um *walker* aleatório com probabilidades dinâmicas. Por exemplo, você conseguiria dar a ele uma probabilidade de 50% de chance de se mover na direção do mouse?

### I.4 Uma Distribuição Normal de Números Aleatórios

Vamos voltar para aquela população de macacos simulada no Procesing. Seu programa gera mil objetos Monkey ("Macacos"), cada um com um valor de altura entre 200 e 300 (pois este é um mundo de macacos que possuem alturas entre 200 e 300 pixels).

```java
float h = random(200,300);
```

Isso representa com precisão as alturas dos organismos do mundo real? Pense em uma calçada lotada na cidade de Nova York. Escolha qualquer pessoa nessa rua e isso pode parecer que sua altura é aleatória. No entanto, não é o tipo de aleatório que random() produz. As alturas das pessoas não são distribuídas uniformemente; há muito mais pessoas de estatura média do que muito altas ou muito baixas. Para simular a natureza, gostaríamos de uma maior probabilidade de que nossos macacos tenham uma altura média (250 pixels), mas ainda permitir que eles sejam, ocasionalmente, muito baixos ou muito altos.

Uma distribuição de valores que se agrupam em torno de uma média (*mean*) é conhecida como distribuição "normal". É também chamada de distribuição Gaussiana (em homenagem ao matemático Carl Friedrich Gauss) ou, se você for francês, de distribuição Laplaciana (em homenagem a Pierre-Simon Laplace). Ambos os matemáticos trabalharam simultaneamente no início do século XIX na definição dessa distribuição.

Ao representar graficamente a distribuição, você obtém algo semelhante a seguinte imagem, informalmente conhecida como curva de sino:

**INSERIR FIGURAS I.2 e I.3**

A curva é gerada por uma função matemática que define a probabilidade de qualquer valor ocorrer em função da média (muitas vezes escrita como μ, a letra grega mu) e do desvio padrão (σ, a letra grega sigma).

A média é muito fácil de entender. No caso dos nossos valores da altura entre 200 e 300, você provavelmente tem uma noção intuitiva da média como 250. No entanto, e se eu dissesse que o desvio padrão é 3 ou 15? O que isso significa para os números? Os gráficos acima devem nos dar uma dica. O gráfico à esquerda nos mostra a distribuição com um desvio padrão muito baixo, onde a maioria dos valores se agrupa próximo à média. O gráfico à direita nos mostra um desvio padrão mais alto, em que os valores são mais uniformemente espalhados da média.

Os números funcionam da seguinte forma: dada uma população, 68% dos membros dessa população terão valores na faixa de um desvio padrão da média, 98% dentro de dois desvios padrão e 99,7% dentro de três desvios padrão. Dado um desvio padrão de 5 pixels, apenas 0,3% das alturas dos macacos será menor que 235 pixels (três desvios padrão abaixo da média de 250) ou maior que 265 pixels (três desvios padrão acima da média de 250).

---

**Calculando a Média e o Desvio Padrão**

Considere uma sala de aula com dez alunos que recebem as seguintes pontuações (de 100) em um teste:

85, 82, 88, 86, 85, 93, 98, 40, 73, 83

A média é: 81,3

O desvio padrão é calculado como a raiz quadrada da média dos quadrados dos desvios em torno da média. Em outras palavras, pegue a diferença da média para cada pessoa e eleve ao quadrado (variância). Calcule a média de todos esses valores e tome a raiz quadrada como o desvio padrão.

| **Pontuação** | **Diferença da média** | **Variância**        |
|---------------|------------------------|----------------------|
| 85            | 85-81,3 = 3,7          | (3,7)^2 = 13,69      |
| 40            | 40-81,3 = -41,3        | (-41,3)^22 = 1705,69 |
| etc.          |                        |                      |
|               | **Variância média**    | 254,23               |


**O desvio padrão é a raiz quadrada da variância média: 15,13**

---

Felizmente para nós, para utilizarmos uma distribuição normal de números aleatórios em um *sketch* no Processing, não precisamos fazer nenhum desses cálculos manualmente. Em vez disso, podemos fazer uso de uma classe conhecida como Random, que obtemos gratuitamente como parte das bibliotecas padrão em Java importadas para o Processing (para mais informações consulte os [JavaDocs](http://docs.oracle.com/javase/6/docs/api/java/util/Random.html)).

Para utilizar a classe Random, devemos primeiro declarar uma variável do tipo Random e criar o objeto Random em setup().

```java
Random generator; // nós utilizamos o nome "generator" porque o que temos aqui pode ser pensado como um gerador de números aleatórios
 
void setup() {
  size(640,360);
  generator = new Random();
}

```

Se quisermos produzir um número aleatório com uma distribuição normal (ou Gaussiana) cada vez que executamos o draw(), é tão fácil quanto chamar a função nextGaussian().


```java
void draw() { // pedindo para um número aleatório Gaussiano (note que nextGaussian() retorna um "double" e deve ser convertido em um "float")
  float num = (float) generator.nextGaussian();
}
```

Aqui está um detalhe. O que devemos fazer com esse valor? E se quiséssemos usá-lo, por exemplo, para atribuir a posição x de um desenho na tela?

A função nextGaussian() retorna uma distribuição normal de números aleatórios com os seguintes parâmetros: uma média de zero e um desvio padrão de um. Digamos que queremos uma média de 320 (o pixel horizontal central em uma janela de 640 largura) e um desvio padrão de 60 pixels. Podemos ajustar o valor aos nossos parâmetros multiplicando-o pelo desvio padrão e adicionando a média.

**INSERIR FIGURA EXEMPLO I.4**

```java
void draw() { // observe que o nextGaussian() retorna um "double".

  float num = (float) generator.nextGaussian();
  float sd = 60;
  float mean = 320;
 
  float x = sd * num + mean; // multiplique pelo desvio padrão da média e adicione-o na média
 
  noStroke();
  fill(255,10);
  ellipse(x,180,16,16);
}
```

Desenhando as elipses umas sobre as outras com um pouco de transparência, podemos observar a distribuição claramente. O ponto mais brilhante fica próximo ao centro, onde a maioria dos valores se agrupam, mas de vez em quando os círculos são desenhados mais à direita ou à esquerda do centro.

#### Exercício I.4

Considere uma simulação de respingos de tinta desenhada como uma coleção de pontos coloridos. A maior parte da tinta se aglomera em torno de um local central, mas alguns pontos se espalham em direção às bordas. Você consegue utilizar a distribuição normal de números aleatórios para gerar as localizações destes pontos? Você também conseguiria utilizar a distribuição normal de números aleatórios para gerar uma paleta de cores?

#### Exercício I.5

Um caminhante aleatório gaussiano (*Gaussian random walker*) é definido como aquele em que o tamanho do passo (a distância que o objeto se move em uma determinada direção) é gerado por uma distribuição normal. Implemente esta variação no nosso caminhante aleatório.

### I.5 Uma Distriuição de Números Aleatórios Personalizados
