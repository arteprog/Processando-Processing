# Anatomia de um programa

 Autor to artigo orginal em inglês: **J David Eisenberg**

> Esta é uma tradução de [Anatomy of a Program](https://processing.org/tutorials/anatomy/) disponível em processing.org/tutorials mantendo a licença [Creative Commons BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/).
>

Muitos dos tutoriais para o Processing se concentram no que a linguagem pode fazer (mudar cores, desenhar formas, criar arrays`*` de objetos) a quais chamadas de função permitem a você realizar essas tarefas. Essas são coisas que você precisa saber para escrever um programa em Processing. `*`*[existe a tradução 'arranjo' em português, mas ninguém fala]*

Há uma peça do quebra-cabeça que esses tutoriais não resolvem: como você analisa um problema e o desmonta em passos que o computador consegue executar? Neste tutorial, pretendo mostrar o que aconteceu na minha cabeça conforme eu prosegui na tarefa de escrever funções para desenhar polígonos regulares e figuras em forma de estrela em Processing. Esta é uma boa escolha por não ser uma tarefa grande demais para compreender, mas também não é um problema trivial.

Lembre que o que você está vendo aqui são o meu processo mental e o meu estilo de programação particulares. Há muitas diferentes formas de aproximação e estilos. Conforme você continuar a programar, vai encontrar o seu próprio. Você pode também ver o estilo de programaco de outras pessoas (mas não o seus processos mentais!) olhando o código fonte de programas em [openProcessing.org](http://openprocessing.org/). 

### Desenhando polígonos regulares

Ninguém pensa em construir uma casa sem um projeto executivo, e você não deve pensar em escrever um programa sem algum tipo de planejamento. Uma vez que Processing é uma linguagem tão visual, eu sempre tenho que esboçar o que eu gostaria como resultado antes de me aproximar do teclado. Então é aí que eu começo.

### Passo 1: Planejando no papel

O primeiro passo foi desenhar um diagrama tosco para desenterrar velhas memórias de como polígonos regulares funcionam. O hexágono foi o primeiro que eu desenhei. Como você pode ver pelo lacinho que eu desenhei no interior, os ângulos centrais das fatias somam um círculo completo, ou 360°, e o "raio" do polígono é a linha do centro até cada vértice.O angulo entre cada linha do raio é, portanto, 360º dividido pelo número de lados.

![sketch1](https://processing.org/tutorials/anatomy/imgs/sketch1.jpg)

Eu só precisava ter uma ideia do que era a tarefa, e um diagrama desenhado a mão resolveu isso. Eu não precisei gerar o diagrama em um programa de desenho.

> Dica de Programacão: Quando fizer seu plano, faça este processo longe do computador. Se estiver sentado em frente ao cmputador, a tela irá sussurrar, "Olhe pra mim! Olhe pra mim!" o teclado irá sussurrar "Digite algo! Digite algo!" Ao invés disso, vá para mesa da cozinha.

### Passo 2: Um pouco de trigonometria básica

Então se você tem uma linha do tamanho de *r* iniciando em (0,0) em um anguo theta (0), o que são estas coordenadas em termos de *x* e *y*? Se você conhece um pouco de trigonometria , a resposta é que ponto final da linha está em (*r* cos θ,*sen*),Se você não conhece trigonometria, dê uma olhada,[Neste tutorial](http://catcode.com/trig/) (Uma introdução geral a trigonometrial), [neste tutorial](http://processing.org/learning/trig/) (Trigonometria com Processing) e [neste exemplo a partir do capítulo 13 de *Learning Processing*](http://learningprocessing.com/examples/chp13/example-13-05-polar-cartesian). No seguinte diagrama, os ângulos são desenhados em sentido horário, da mesma maneira como medimos no Processing.

![](https://processing.org/tutorials/anatomy/imgs/sketch2.jpg)


### Passo 3: Decisões de projeto

Isso parece um trabalho para um loop `for` que corre de 0 a *n* (o número de lados), calculando os pontos de cada vértice e desenhando as linhas os conectando. A cada passo, o ângulo no qual desenhamos aumenta 360°/*n*.

O problema de desenhar um grupo de linhas é que elas são só linhas—você fica sem uma forma verdadeira que pode preencher, como `rect()` ou `triangle()`. Por sorte, Processing deixa você criar suas próprias formas com as funções [`beginShape()`](http://processing.org/reference/beginShape_.html), [`vertex()`](file:///home/david/processing-1.0.9/reference/vertex_.html), e [`endShape()`]. O primeiro exemplo da página de referência para o `beginShape()` é o modelo a seguir. Então a próxima decisão é fazer o polígono como verdadeira forma.

Uma vez que provavelmente você quer desenhar muitos polígonos durante o programa, faz sentido ter uma função `polygon()`. Quais parâmetros ela precisa? Quatro vem à mente: O número de lados, as coordenadas do centro *x* e *y*, e o raio. Aqui está o código. Eu escrevei várias chamadas diferentes a `polygon()` dentro da função `setup()`. Apesar de ter calculado `angle` em graus, seno e coseno usam radianos, então eu tive que usar `radians()` para fazer a conversão.

![](https://processing.org/tutorials/anatomy/imgs/polytest1.jpg)

```pde
void setup() {
  size(300, 300);
  background(255);

  noFill();
  polygon(3, 50, 75, 50);
  polygon(4, 170, 75, 50);

  fill(255, 204, 255);
  stroke(128, 0, 128);
  polygon(5, 50, 180, 50);

  noFill();
  stroke(0);
  polygon(6, 170, 180, 50);
}

void polygon(int n, float cx, float cy, float r) {
  float angle = 360.0 / n;

  beginShape();
  for (int i = 0; i < n; i++) {
vertex(cx + r * cos(radians(angle * i)),
  cy + r * sin(radians(angle * i)));
  }
  endShape(CLOSE);
}

```

### Dois passos para frente, um para trás

O programa funciona, então é hora de ver se tem coisas que podem ser acrescentadas ou mudadas. Primeiro, o triângulo e o pentágono parecem de alguma maneira errados; eles são normalmente desenhados apontando pra cima em vez de pro lado. A razão deles parecerem estranhos é que o primeiro vértice (em 0°) aponta pra direita em vez de direto pra cima. Seria legal ter um parâmetro extra que desse o ângulo inicial para o primeiro vértice. (Uma outra solução é deisar as coisas como estão e deixar as pessoas usaresm `rotate()` [veja o tutorial das transformações 2D], mas tomei a descisão de projeto de usar um parâmetro extra.) Deve o ângulo ser fornecido em graus ou em radianos? A resposta: radianos, de maneira a ser consistente com to o resto que Processing faz.

Meu próximo pensamento foi que seria legal ser capaz de especificar uma altura e largura para o polĩgono, parecido com o que fazemos com a `ellipse()`ou `rect()`. E eu já sabia como a fórmula devia ser, mas eu queria fazer um desenho para conferir. Como experimento preliminar, tentei desenhar um pentágono em um quadrado com transferidor régua, e terminei com o horrível desenho à esquerda. Como que os lados não tem comprimentos iguais? Percebi que estava tentando fazer o desenho encaixar nas minhas preconcepções, em vez de fazer um desenho preciso e ver onde isso me levaria. O desenho da direita foi feito muito mais cuidadosamente. Depois de pensar um pouco,percebi que o pentágono não encaixaria no quadrado exatamente, pois os ângulos não eram múltiplos de 90 graus. O polígono regular encaixa em um *círculo*, não em um quadrado!

![pentagon with unequal sides](https://processing.org/tutorials/anatomy/imgs/bad_pentagon.jpg)   ![pentagon with equal sides](https://processing.org/tutorials/anatomy/imgs/accurate_pentagon.jpg)

Bem, isso foi um beco sem saída. Esse tipo de coisa acontece em progrmação o tempo todo, então eu não gastei muito temp me preocupando com isso. Era hora de uma outra aproximação. Uma vez que eu não tinha uma maneira precisa de desenhar elipses, tinha que pensar no problema de outra maneira. Presuma que você tem um círculo desenhado em uma folha de borracha, e você estica de tal maneira que ela fica duas vezes mais larga mas com a mesma altura. A posição vertical dos pontos no círculo não muda, mas as posições horizontais agora estão duas vezes mais distantes do centro do que estavam antes. A mesma ideia se aplica se vocẽ esticar a folha verticalmente. Os desenhos grosseiros a seguir pareciam levar a isto, então estava na hora de reescrever a função `polygon()`.

![diagrams showing stretched circle](https://processing.org/tutorials/anatomy/imgs/stretchy.jpg)

![more complex polygon tests](https://processing.org/tutorials/anatomy/imgs/poly2.png)

```pde
void setup() {
  size(300, 300);
  background(255);

  noFill();
  polygon(3, 50, 75, 100, 100, -PI / 2.0); // -90 degrees
  polygon(4, 170, 75, 50, 125, -PI / 4.0); // -45 degrees

  fill(255, 204, 255);
  stroke(128, 0, 128);
  polygon(5, 50, 200, 75, 50, -PI / 2.0); // -90 degrees

  noFill();
  stroke(0);
  polygon(6, 170, 200, 50, 100, 0);

  stroke(128);
  // Draw enclosing ellipses to make sure we did it right
  ellipse(50, 75, 100, 100);
  ellipse(170, 75, 50, 125);
  ellipse(50, 200, 75, 50);
  ellipse(170, 200, 50, 100);
}

void polygon(int n, float cx, float cy, float w, float h, float startAngle) {
  float angle = TWO_PI/ n;

  // The horizontal "radius" is one half the width,
  // the vertical "radius" is one half the height
  w = w / 2.0;
  h = h / 2.0;

  beginShape();
  for (int i = 0; i < n; i++) {
vertex(cx + w * cos(startAngle + angle * i), 
  cy + h * sin(startAngle + angle * i));
  }
  endShape(CLOSE);
}
```

Uma vez que tudo estava em radianos, agora descrevi os ânguloes em termos de `PI` e `TWO_PI` (2π), já que 2π radianos é igual a 360°. Em acréscimo ao código no`setup()` para testar os novos recursos, desenhei elipses com o mesmo centro e largura e altura como os polígonos para ter certeza de que os véritces estavam dentro da região certa.

### Parâmetros demais

Agora eu tinha uma função muito mais flexível para desenhar polígonos, mas isso veio ao custo de mais parâmetros. Seria legal ser caoaz de desenhar os casos mais comuns (com largura e altura iguais, ângulo inicial zero) sem ter que ficar especificando todos esses parâmetros. A solução é uma sobrecarga de função (*function overloading*). 
Em Processing, você pode ter duas funções com o mesmo nome, desde que tenham diferente número de parâmetros e/ou diferentes tipos de parânetros. Um exemplo disso é a função `stroke()` do Processing, que é sobrecarregada de maneira que você pode chamá-la com um número para cinza, três números para cor, ou quatro números para cor com opacidade. Processing olha para o número de argumentos que você provê e escolhe qual versão do `stroke()` chamar. 

Eis o código para acrescentar ao exemplo anterior. Quando você der `polygon()` apenas quatro números, vai chamar a seguinte função, que chama a versão "grande" da função com largura e altura iguais ao dobro do seu raio desejado e com o ângulo zero.

```pde
void polygon(int n, float cx, float cy, float r) {
  polygon(n, cx, cy, r * 2.0, r * 2.0, 0.0);
}

```

E aqui código para testar a função sobrecarregada.

![](https://processing.org/tutorials/anatomy/imgs/poly3.png)

```pde
void setup() {
  size(300, 300);
  background(255);
  smooth();
  
  noFill();
  polygon(3, 70, 75, 50); // use the defaults
  polygon(4, 170, 75, 25);
  
  stroke(128);
  // draw enclosing ellipses to make sure we did it right
  ellipse(70, 75, 100, 100);
  ellipse(170, 75, 50, 50);
}

```

### Computação segura

O que acontece se alguém tentar desenhar um polígono com 2 lados, 1 lado ou pior, 0 lados? Os dois primeiros casos vão gerar uma linha e um ponto, mas o terceiro vai causar um erro de divisão por zero quando for tentar descobrir o ângulo. E o que aconteceria com números negativos? Uma vez que polígonos com menos do que três lados não fazem muito sentido, encapsuleio o corpo da função `polygon()`em uma instrução `if` . Agora quando alguém especifica dois ou menos lados a função só não vai desenhar nada.

```pde
void polygon(int n, float cx, float cy, float w, float h, float startAngle) {
  if (n > 2) {
float angle = TWO_PI/ n;
.
.
beginShape()
.
.
endShape(CLOSE);
  }
}

```

### Desenhando estrelas

Now that I was satisfied with the `polygon()` function, it was time to move on to drawing stars. From some playing around with a crude sketch, I figured that it would be possible to draw a star by figuring out where all the diagonals of a polygon intersect.

![Stars drawn by intersections of diagonals](https://processing.org/tutorials/anatomy/imgs/bad_stars.jpg)

I saw two problems here. First, finding the intersection point of two lines isa lot of calculation. Not particularly hard calculation, but a lot of it,and it gets tricky when you have vertical lines.Second, I couldn't have a four-sided or three-sidedarrow shape; there weren’t enough diagonals.

Then, I had another idea. I can’t tell you where the idea came from or how I arrived at it; it just hit me. That’s a part of the process that I don’t think can be taught. Here was the idea: What if you had a polygon cut out of cookie dough and you sort of pushed in the sides to make a star shape? That is a method that works for squares and triangles.

![Stars drawn by pushing in the sides](https://processing.org/tutorials/anatomy/imgs/cookie_stars.jpg)

When you push in the sides, you push them in at the midpoint so that you get a nice symmetric cookie. From there, it wasn’t a big leap to figure out: “what if I had a shorter radius at half of every slice of the polygon?” 

![Stars drawn by pushing in the sides](https://processing.org/tutorials/anatomy/imgs/good_stars.jpg)

This code would be fairly easy to write. I would need one extra parameter: the proportion of the small radius to the big radius. In the following code, an `if` statement controls whether to use the short radius or the long radius. I also put in an overloaded version that draws a star with equal width and height and a start angle of zero. For the test, I made the short radius one half the long radius.

![](https://processing.org/tutorials/anatomy/imgs/surprise.png)

```pde
void setup() {
  size(300, 300);
  background(255);
  smooth();

  noFill();
  star(3, 60, 75, 100, 100, -PI / 2.0, 0.50); // -90 degrees
  star(4, 170, 75, 25, 0.50);  // use simpler call

  fill(255, 204, 255);
  stroke(128, 0, 128);
  star(5, 60, 200, 75, 50, -PI / 2.0, 0.50); // -90 degrees

  noFill();
  stroke(0);
  star(6, 170, 200, 50, 100, 0, 0.50);
  stroke(128);
  
  // draw enclosing ellipses to make sure we did it right
  ellipse(60, 75, 100, 100);
  ellipse(170, 75, 50, 50);
  ellipse(60, 200, 75, 50);
  ellipse(170, 200, 50, 100);
}

void star(int n, float cx, float cy, float r, float proportion) {
  star(n, cx, cy, 2.0 * r, 2.0 * r, 0.0, proportion);
}

void star(int n, float cx, float cy, float w, float h,
  float startAngle, float proportion) {

  if (n > 2) {
float angle = TWO_PI/ (2 *n);  // twice as many sides
float dw; // draw width
float dh; // draw height

w = w / 2.0;
h = h / 2.0;

beginShape();
for (int i = 0; i < 2 * n; i++) {
  dw = w;
  dh = h;
  if (i % 2 == 1) { // for odd vertices, use short radius
  
dw = w * proportion;
dh = h * proportion;
  }
  vertex(cx + dw * cos(startAngle + angle * i),
cy + dh * sin(startAngle + angle * i));
}
endShape(CLOSE);
  }
}

```

### O que deu errado?

Quando eu executei esse programa, eu dei uma surtada. Tudo parecia ótimo, exceto a estrela de três lados. Como eu não tinha obtido uma estrela disso? 

When I ran this program, I just freaked out. Everything looked great, except for the three-sided star. How come I didn’t get a star from it?  The code sure looks correct, so I decided to see what would happen if I drew the diagram by hand. I measured the angles with my protractor, and I drew the long radius lines with a length of two inches in black and the short radius lines with a length of one inch in red. Sure enough, it just so happens that the endpoints of the short radius lines are right on the lines of the main triangle. The program *is* drawing a star, with the sides pushed in by zero.

  ![triangular star drawn by hand](https://processing.org/tutorials/anatomy/imgs/triangle_star.jpg)

While wondering why this happened, I remembered that the cosine of the angle between the lines, 60° (π/3) comes out to 0.5, and I strongly suspected that this had something to do with it. To test my hypothesis, I changed the square to use a proportion of cosine of 45° (π/4), the pentagon to cosine of 36° (π/5), and the hexagon to cosine of 30° (π/6). Sure enough, they all came out with no push-in.

So, if you are drawing a star with *n* sides and you set the proportion for the short radius to long radius to the cos(π/*n*), you get a non-star star! I still can’t write a mathematical proof of it, but it is an interesting result. I don’t consider that side trip of writing the test program to be wasted time; I did learn something new and mildly interesting, and it may turn out to be useful in the future.

> **Programming Challenge:** What happens if you set the  proportion to something *greater* than the “non-star”  ratio? Try it and find out.  

Of course, the way to get a three-sided star is to set the proportion  to an amount less than 0.5, which I did in the following setup code,  with much better results. I also changed the proportions for the other  stars just to see what they would look like.

![](https://processing.org/tutorials/anatomy/imgs/better_stars.png)

```pde
void setup(){
  size(300, 300);
  background(255);

  noFill();
  star(3, 60, 75, 100, 100, -PI / 2.0, 0.3); // -90 degrees
  star(4, 170, 75, 25, 0.5);  // use simpler call

  fill(255, 204, 255);
  stroke(128, 0, 128);
  star(5, 60, 200, 75, 50, -PI / 2.0, 0.75); // -90 degrees

  noFill();
  stroke(0);
  star(6, 170, 200, 50, 100, 0, 0.4);
  stroke(128);
  
  // Draw enclosing ellipses to make sure we did it right
  ellipse(60, 75, 100, 100);
  ellipse(170, 75, 50, 50);
  ellipse(60, 200, 75, 50);
  ellipse(170, 200, 50, 100);
}


void star(int n, float cx, float cy, float r, float proportion) {
  star(n, cx, cy, 2.0 * r, 2.0 * r, 0.0, proportion);
}

void star(int n, float cx, float cy, float w, float h,
  float startAngle, float proportion) {

  if (n > 2) {
float angle = TWO_PI/ (2 *n);  // twice as many sides
float dw; // draw width
float dh; // draw height

w = w / 2.0;
h = h / 2.0;

beginShape();
for (int i = 0; i < 2 * n; i++) {
  dw = w;
  dh = h;
  if (i % 2 == 1) {
dw = w * proportion;
dh = h * proportion;
  }
  vertex(cx + dw * cos(startAngle + angle * i),
cy + dh * sin(startAngle + angle * i));
}
endShape(CLOSE);
  }
}

```

### Usando as funções

Finally, in order to use the functions in something other than a test, I decided to write a program that would randomly generate polygons and stars. The window is 300 by 300, and the stars or polygons have a radius of 24 dots, so I have six rows and five columns (the extra dot is for spacing). Remember how I said that knowing the proportions that would create a star “may turn out to be useful in the future”? Well, they aren’t just useful for this program—they’re vital. When I generate a star, I need to make sure it really has a star shape, so I have to keep the proportion of short to long radius less than the cosine of π divided by the number of sides.

Here is the code for `setup()` and `draw()`:

```pde
void setup() {
  size(300, 300);
  background(255);
  frameRate(6);
  rectMode(CENTER);
}

void draw() {
  // Choose a random stroke color
  int r = int(random(0, 255));
  int g = int(random(0, 255));
  int b = int(random(0, 255));
  // Fill opacity
  int opacity = int(random(100, 255));
  int nSides = int(random(3, 9));

  // Determine the center x and y coordinates
  int cx = 25 + 50 * int(random(0, 6));
  int cy = 25 + 50 * int(random(0, 6));

  // If a random number (0 or 1) is 0, draw a polygon;
  // otherwise, draw a star
  boolean isPolygon = int(random(2)) == 0;

  // For stars, you need the proportion of short to long radius
  float proportion;

  stroke(255); // erase any previous drawing in this area
  fill(255);
  rect(cx, cy, 50, 50); 

  stroke(r, g, b);
  fill(r, g, b, opacity);
  if (isPolygon) {
polygon(nSides, cx, cy, 24);
  } else {
proportion = random(0.2, 0.8) * cos(PI / nSides);
star(nSides, cx, cy, 24, proportion);
  }
}

void polygon(int n, float cx, float cy, float r) {
  float angle = 360.0 / n;
  beginShape();
  for (int i = 0; i < n; i++) {
vertex(cx + r * cos(radians(angle * i)),
  cy + r * sin(radians(angle * i)));
  }
  endShape(CLOSE);
}

void star(int n, float cx, float cy, float r, float proportion) {
  star(n, cx, cy, 2.0 * r, 2.0 * r, 0.0, proportion);
}

void star(int n, float cx, float cy, float w, float h,
  float startAngle, float proportion) {
  if (n > 2) {
float angle = TWO_PI/ (2 *n);  // twice as many sides
float dw; // draw width
float dh; // draw height

w = w / 2.0;
h = h / 2.0;

beginShape();
for (int i = 0; i < 2 * n; i++)
{
  dw = w;
  dh = h;
  if (i % 2 == 1) // for odd vertices, use short radius
  {
dw = w * proportion;
dh = h * proportion;
  }
  vertex(cx + dw * cos(startAngle + angle * i),
cy + dh * sin(startAngle + angle * i));
}
endShape(CLOSE);
  }
}

```

### Polígonos e estrelas como objetos

Now that I have working functions for polygons and stars, it mightbe useful to make a `Polygon` and `Star` classso that I can treat them as objects. The method I would use is muchthe same; I would start with simple test cases, build up theclasses step by step, and finally use them in a full-blown program.[Here isa tutorial about objects in Processing.](http://processing.org/learning/objects)

### Resumindo

This tutorial has shown you the things you never see in books.In a book, all the diagrams arepicture perfect. You see a sample program, and it just works, andit produces gorgeous results. To be fair, the authors*can’t* show you their thought process; otherwise,their books would be ten times as large. In fact, I did not includeall the versions where a misplaced parenthesis or a forgotten callto `radians()` made my sketch explode into a mass ofincomprehensible lines. But all of us, the big name authors, thepeople who write these tutorials, and the beginning programmers,go through this same tawdry process of design, trial and error,and development. I wanted you to see that process at least once,because we are all in this together.

> Colaboraram nesta tradução: @ronireis  e [Alexandre Villares](http://abav.lugaralgum.com) 
