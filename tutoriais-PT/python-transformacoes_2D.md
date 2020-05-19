# Transformações 2D

Autor to artigo orginal em inglês: **J David Eisenberg**

> Esta é uma tradução de [2D Transformations](https://py.processing.org/tutorials/transform2d/) disponível em processing.org/tutorials mantendo a licença [Creative Commons BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[Baixe os arquivos deste tutorial](https://py.processing.org/tutorials/transform2d/imgs/transform2d.zip)

Processing tem funções embutidas que tornam fácil você mover, girar, ecrescer ou encolher objetos em um *sketch*. Este tutorial vai apresentar você às funções `translate`, `rotate`, e `scale`. De maneira que você as possa usar nos seus *sketches*.

### Translação: Movendo a grade

Como você sabe, sua janela do Processing funciona como um pedaço de papel milimetrado. Quando você quer desenhar alguma coisa, especifica as cordenadas. Veja um retângulo simples desenhado com o código `rect(20, 20, 40, 40)`. O sistema de coordenadas (um nome sofisticado para o nosso "papel milimetrado") está mostrado em cinza.

![Black rectangle on gray numbered grid](https://py.processing.org/tutorials/transform2d/imgs/original.png)

Se você quiser mover o retângulo 60 unidades para a direita e 80 unidades para baixo, pode mudar as coordenadas somando ao *x* e *y* do ponto inicial: `rect(20 + 60, 20 + 80, 40, 40)` e o retângulo vai aparecer em um local diferente. (Pusemos a seta aí para efeito dramático.)

![Black rectangle on gray numbered grid, moved](https://py.processing.org/tutorials/transform2d/imgs/new_coords.png)

Mas tem uma maneira mais interessante de fazer isso: **em vez disso mover o papel milimetrado**. Se você moveo o papel milimetrado 60 unidades para a direita e 80 para baixo vai obter exatamente o mesmo resultado visual. Mover o sistema de coordenadas é chamado de translação.

![grid moved with arrow showing motion](https://py.processing.org/tutorials/transform2d/imgs/moved_grid.png)

A coisa importante de se notar no diagrama anterior é que, do ponto de vista do retângulo, ele não se moveu nada. O canto superior esquerdo continual em (20,20). Quando você usa transformações, as coisas que você desenha *nunca* mudam de posição; o sistema de cordenadas muda.

Abaixo o código que desenha o retângulo em vermelho mudando suas coordenadas, e então desenha em azul movendo a grade. Os retângulos são translúcidos de maneira que você pode ver que estão (visualmente) no mesmo lugar. Apenas o método usado para movê-los mudou. Copie este código no Processing e experimente:

```python
def setup():
    size(200, 200)
    background(255)
    noStroke()

    # draw the original position in gray
    fill(192)
    rect(20, 20, 40, 40)
    
    # draw a translucent red rectangle by changing the coordinates
    fill(255, 0, 0, 128)
    rect(20 + 60, 20 + 80, 40, 40)
    
    # draw a translucent blue rectangle by translating the grid
    fill(0, 0, 255, 128)
    pushMatrix()
    translate(60, 80)
    rect(20, 20, 40, 40)
    popMatrix()

```

Vamos olhar o código de conversão em mais detalhes.`pushMatrix()` é uma função embutida que salva a posição atual do sistema de coordendas. O `translate(60, 80)` movbaixo. O `rect(20, 20, 40, 40)` desenha o retângulo no mesmo local em que estava originalmente. Lembre-se de que as coisas que você desenha não se movem - a grade se move. Por fim,`popMatrix()` restaura o sistema de coordenadas como estava antes de você fazer a translação.

Sim, você podia ter feito uma translação `translate(-60, -80)` para mover a grade de volta a sua posição original. No entanto, quando você começa a executar operações mais sofisticadas com o sistema de coordenadas, é mais fácil usar `pushMatrix()` e `popMatrix()` para salvar e restaurar o status em vez de precisar desfazer todas as suas operações. Mais adiante neste tutorial, você descobrirá por que essas funções parecem ter nomes tão estranhos.

### Qual é a vantagem?

Você pode estar pensando que pegar o sistema de coordenadas e movê-lo é muito mais complicado do que apenas adicionar às coordenadas. Para um exemplo simples, como o retângulo, você está correto. Mas vamos dar um exemplo de onde o `translate()` pode facilitar a vida. Aqui está um código que desenha uma fileira de casas. Ele usa um loop que chama a função chamada `casa()`, que recebe o *x* e *y* da posição do canto superioe esquerdo da casa como parâmetros.

![Row of stick-figure casas](https://py.processing.org/tutorials/transform2d/imgs/houses.png)

```python
def setup():
  size(400, 100)
  background(255)
  for i in xrange(10,350,50):
    casa(i, 20)

```

Este é o código para desenhar a casa alterando sua posição. Veja todos os acréscimos que você precisa acompanhar.

```python
def casa(int x, int y):
  triangle(x + 15, y, x, y + 15, x + 30, y + 15)
  rect(x, y + 15, 30, 30)
  rect(x + 12, y + 30, 10, 15)

```

Compare isso com a versão da função que usa `translate()`. Neste caso o código desenha a casa no mesmo lugar, com o canto superior esquerdo em (0, 0), e deixa a translação fazer todo o trabalho.

```python
def casa(int x, int y):
  pushMatrix()
  translate(x, y)
  triangle(15, 0, 0, 15, 30, 15)
  rect(0, 15, 30, 30)
  rect(12, 30, 10, 15)
  popMatrix()


```

### Rotação

Além da translação que move a grade, é possível girar o sistema de coordenadas com a função `rotate()`. Essa função tem um parâmetro ou argumento, um número de *radianos* que você quer rodar. Em graus, um círculo tem 360°. Quando descrevemos os ângulos em radianos, a circuferência completa tem 2π radianos. Eis aqui um diagrama de como Processing mede ângulos em graus (preto) e radianos (vermelho).

![Degrees are measured clockwise with zero being at 3 o'clock](https://py.processing.org/tutorials/transform2d/imgs/degrees.png)

Como a maioria das pessoas pensa em graus, o Processing possui uma função embutida `radians()` que recebe um número em graus como argumento e o converte para você. Ele também possui uma função  `degrees()` que converte radianos em graus. Dado esse cenário, vamos tentar girar um quadrado 45 graus no sentido horário.

```python
def setup():
  size(200, 200)
  background(255)
  smooth()
  fill(192)
  noStroke()
  rect(40, 40, 40, 40)
  
  pushMatrix()
  rotate(radians(45))
  fill(0)
  rect(40, 40, 40, 40)
  popMatrix()
```
Ei o que aconteceu? Como o quadrado foi movido e cortadao A resposta é: o quadrado não se moveu. A ** grade ** foi girada. Aqui está o que realmente aconteceu. Como você pode ver, no sistema de coordenadas girado, o quadrado ainda tem seu canto superior esquerdo em (40, 40).

![shows grid rotated 45 degrees clockwise](https://py.processing.org/tutorials/transform2d/imgs/rotated_grid.png)

### Girando da maneira certa

A maneira certa de girar o quadrado é:

1. Faça a translação da origem do sistema de coordenadas (0, 0) para onde você quer que seja o canto superior esquerdo do quadrado.
2. Gire a grade π/4 radianos (45°)
3. Desenhe o quadrado na origem.

![Grid translated, then rotated](https://py.processing.org/tutorials/transform2d/imgs/correct_rotate_grid.png)

E aqui está o código que gera o resultado, sem as marcas de grade.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    fill(192)
    noStroke()
    rect(40, 40, 40, 40)
    
    pushMatrix()
    # mova a origem para o ponto de giro
    translate(40, 40)
    
    # em seguida gire a grade
    rotate(radians(45))
    
    # e desenhe o quadrado na origem
    fill(0)
    rect(0, 0, 40, 40)
    popMatrix()
```

E aqui está um programa que gera uma roda de cores usando rotação. A captura de tela é reduzida para economizar espaço.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    noStroke()

def draw():
    if (frameCount % 10 == 0):
        fill(frameCount * 3 % 255, frameCount * 5 % 255,
          frameCount * 7 % 255)
        pushMatrix()
        translate(100, 100)
        rotate(radians(frameCount * 2  % 360))
        rect(0, 0, 80, 20)
        popMatrix()

```

### Escalando

A transformação final do sistema de coordenadas é a mudançã de escala, que altera o tamanho da grade. Dê uma olhada neste exemplo, que desenha um quadrado, depois redimensiona a grade para o dobro do tamanho normal e a desenha novamente.

```python
def setup():
    size(200,200)
    background(255)
    
    stroke(128)
    rect(20, 20, 40, 40)
    
    stroke(0)
    pushMatrix()
    scale(2.0)
    rect(20, 20, 40, 40)
    popMatrix()


```
Primeiro, você pode ver que o quadrado parece ter se movido. Claro que não. Seu canto superior esquerdo ainda está em (20, 20) na grade escalada para cima, mas esse ponto está agora duas vezes mais distante da origem do que no sistema de coordenadas original. Você também pode ver que as linhas são mais grossas. Isso não é ilusão de ótica - as linhas realmente têm o dobro da espessura, porque o sistema de coordenadas foi dimensionado para dobrar seu tamanho.

> **Desafio de programação** aumente a o tamnaho do quadrado preto, mas mantenha o cantto superior esquerdo dele no mesmo lugar do quadrado cinza. Dica: use `translate()` para mover a origem, então use `scale()`.


Não tem um lei que diz que você tem que escalar as dimensões em *x* e *y* igualmente. Tente usar `scale(3.0, 0.5)` para fazer a dimensão em  *x* três vezes maior e a dimensão em *y* metado do tamanho normal.

### A ordem importa

Quando você faz várias transformações, a ordem faz diferença. Uma rotação seguida de uma translação seguida por uma mudança de escala não produzirá os mesmos resultados que uma translação seguida de uma rotação e uma mudança de escala. Aqui está um exemplo de código e os resultados.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    line(0, 0, 200, 0)  # desenha eixos
    line(0, 0, 0, 200)
    
    pushMatrix()
    fill(255, 0, 0)     # quadrado vermelho
    rotate(radians(30))
    translate(70, 70)
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()

    pushMatrix()
    fill(255)           # quadrado branco
    translate(70, 70)
    rotate(radians(30))
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()


```

### A matriz de transformação

Sempre que você faz uma rotação, translação ou mudança de escla, as informações necessárias para a transformação são acumuladas em uma tabela de números. Essa tabela, ou matriz, possui apenas algumas linhas e colunas; no entanto, através do milagre da matemática, ela contém todas as informações necessárias para realizar qualquer série de transformações. E é por isso que `pushMatrix ()` e `popMatrix ()` têm essa palavra em seu nome.

### Push e Pop

Sobre a parte *push* e *pop* dos nomes? Elas vêm de um conceito de computação conhecido como pilha, que funciona como um dispensador de bandejas com mola em uma lanchonete. Quando alguém devolve uma bandeja para a pilha, seu peso empurra a plataforma para baixo. Quando alguém precisa de uma bandeja, ela a pega da parte superior da pilha e as bandejas restantes aparecem um pouco.


De maneira semelhante, `pushMatrix()` coloca o status atual do sistema de coordenadas no topo de uma área de memória, e `popMatrix()` pega de volta o status. O exemplo anterior usou `pushMatrix()` e `popMatrix()` para garantir que o sistema de coordenação estivesse "limpo" antes de cada parte do desenho. Em todos os outros exemplos, as chamadas para essas duas funções não eram realmente necessárias, mas não custa nada salvar e restaurar o status da grade.


Nota: Em Processing, o sistema de coordenadas é restaurado ao seu estado original (origem na parte superior esquerda da janela, sem rotação e sem mudança de escala) toda vez que a função `draw \()` é executada.

### Transformações Tri-dimensionais


Se você estiver trabalhando em três dimensões, poderá chamar a função `translate()` com três argumentos para as distâncias *x*, *y*, e *z*. Da mesma forma, você vhama `scale()` com três argumentos que indicam o quanto você deseja que a grade seja redimensionada em cada uma dessas dimensões

Para rotação, chame as funções `rotateX()`, `rotateY()`, ou `rotateZ()` para girar em torno de cada um dos eixos. Todas essas três funções esperam um argumento: o número de radianos a serem rotacionados.

### Estudo de caso: Um robô que balança os braços

Vamos usar essas transformações para animar um robô azul agitando os braços. Em vez de tentar escrever tudo de uma vez, faremos o trabalho em etapas. O primeiro passo é desenhar o robô sem nenhuma animação.

O robô é baseado em [thisdrawing](http://www.openclipart.org/detail/5457), embora não pareça tão charmoso. Primeiro, desenhamos o robô para que sua esquerda e a parte superior toquem os eixos *x* e *y*. Isso nos permitirá usar `translate()` para posicionar facilmente o robô em qualquer lugar que desejarmos ou que façamos várias cópias do robô, como fizemos no exemplo das casas.

Quando nos referimos à esquerda e à direita neste desenho, queremos dizer sua esquerda e direita (o lado esquerdo e direito do monitor), não o esquerdo e o direito do robô.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    drawRobot()

def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)      # cabeça
    rect(14, 32, 50, 50)     # corpo
    
    rect(0, 32, 12, 37)      # braço esquerdo
    rect(66, 32, 12, 37)     # braço direito
    
    rect(22, 84, 16, 50)     # perna esquerda
    rect(40, 84, 16, 50)     # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12)  # olho esquerdo
    ellipse(47, 12, 12, 12)  # olho direito

```

![robô com pontos vermelhos nas articulações dos ombros](https://py.processing.org/tutorials/transform2d/imgs/pivot.png)

O próximo passo é identificar os pontos nos quais os braços giram. Isso é mostrado neste desenho. Os pontos de articulação são (12, 32) e (66, 32). Nota: o termo "centro de rotação" é um termo mais formal para o ponto de articulação.

Agora separe o código para desenhar os braços direito e esquerdo, e mova o centro de rotação de cada braço para a orgigem, porque você sempre gira em torno do ponto (0, 0). Para economizar espaço, não estamos repetindo o código para `setup()`.

```python
def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)      # cabeça
    rect(14, 32, 50, 50)     # corpo
    drawLeftArm()
    drawRightArm()
    rect(22, 84, 16, 50)     # perna esquerda
    rect(40, 84, 16, 50)     # perna direita
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12)  # olho esquerdo
    ellipse(47, 12, 12, 12)  # olho direito

def drawLeftArm():
    pushMatrix()
    translate(12, 32)
    rect(-12, 0, 12, 37)
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)
    rect(0, 0, 12, 37)
    popMatrix()
```


Agora, teste para ver se os braços giram corretamente. Em vez de tentar uma animação completa, iremos apenas girar o braço esquerdo esquerdo 135 graus e o braço direito -45 graus como teste. Aqui está o código que precisa ser adicionado e o resultado. O braço esquerdo foi cortado por causa dos limites da janela, mas corrigiremos isso na animação final.

```python
def drawLeftArm():
    pushMatrix()
    translate(12, 32)

    rotate(radians(135))

    rect(-12, 0, 12, 37)    # braço esquerdo
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)

    rotate(radians(-45))

    rect(0, 0, 12, 37)     # braço direito
    popMatrix()
```

Agora, concluímos o programa inserindo a animação. O braço esquerdo deve girar de 0 ° a 135 ° e vice-versa. Como o movimento do braço é simétrico, o ângulo do braço direito sempre será o valor negativo do ângulo do braço esquerdo. Para simplificar, iremos em incrementos de 5 graus.

Now we complete the program by putting in the animation. Thebraço esquerdo has to rotate from 0° to 135° and back.Since the arm-waving is symmetric, theright-arm angle will always be the negative value ofthe left-arm angle. To make things simple,we will go in increments of 5degrees. 

```
armAngle = 0
angleChange = 5
ANGLE_LIMIT = 135

def setup():
  size(200, 200)
  smooth()
  frameRate(30)

def draw():
    global armAngle, angleChange, ANGLE_LIMIT
    print armAngle
    background(255)
    pushMatrix()
    translate(50, 50)  # para que os braços caibam na tela
    drawRobot()
    armAngle += angleChange
  
    # se o braço ultrapassou seu limite,
    # inversta a direção e ponha no limite.
    if armAngle > ANGLE_LIMIT or armAngle < 0:
        angleChange = -angleChange
        armAngle += angleChange
    popMatrix()


def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)     # cabeça
    rect(14, 32, 50, 50)    # corpo
    drawLeftArm()
    drawRightArm()
    rect(22, 84, 16, 50)    # perna esquerda
    rect(40, 84, 16, 50)    # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12) # olho esquerdo
    ellipse(47, 12, 12, 12) # olho direito

def drawLeftArm():
    global armAngle
    pushMatrix()
    translate(12, 32)

    rotate(radians(armAngle))

    rect(-12, 0, 12, 37)    # braço esquerdo
    popMatrix()

def drawRightArm():
    global armAngle
    pushMatrix()
    translate(66, 32)

    rotate(radians(-armAngle))

    rect(0, 0, 12, 37)     # braço direito
    popMatrix()
```

### Estudo de caso: Rotação interativa

Instead of having the arms move on their own, we will modify the programso that the arms follow the mouse while the mouse button is pressed. Insteadof just writing the program at the keyboard, we first think about theproblem and figure out what the program needs to do. 

Since the two arms move independently ofone another, we need to have one variable for each arm’s angle.It’s easy to figure out which arm to track. If the mouse is at theleft side of the robot’s center, track the braço esquerdo; otherwise,track the braço direito.

The remaining problem is to figure out the angle of rotation. Given thepivot point position and the mouse position, how do you determine theangle of a line connecting those two points?  The answer comes from the`atan2()` function, which gives (in radians) the angleof a line from the origin to a given *y* and *x* coordinate.In constrast to most other functions, the *y* coordinate comesfirst. `atan2()` returns a value from -π to π radians,which is the equivalent of -180° to 180°.

But what about finding the angle of a line that doesn’t startfrom the origin, such as the line from (10, 37) to (48, 59)?No problem; it’s the same as the angle of a line from(0, 0) to (48-10, 59-37). In general, to find theangle of the line from (*x*0, *y*0)to (*x*1, *y*1), calculate

```pyde
   atan2(y1 - y0, x1 - x0)
```

Because this is a new concept, rather than integrate it into the robotprogram, you should write a simple test program to see that you understand how `atan2()`works. This program draws a rectangle whose center of rotation isits upper left corner at (100, 100) and tracks the mouse.

```python
def setup():
    size(200, 200)

def draw():
    angle = atan2(mouseY - 100, mouseX - 100)
    
    background(255)
    pushMatrix()
    translate(100, 100)
    rotate(angle)
    rect(0, 0, 50, 10)
    popMatrix()


```

That works great. What happens if we draw the rectangle so it istaller than it is wide? Change the preceding code to read`rect(0, 0, 10, 50)`. How come itdoesn’t seem to follow the mouse any more? The answer isthat the rectangle really *is* still following the mouse,but it’s the short side of the rectangle that does the following.Our eyes are trained to want the long side to be tracked. Becausethe long side is at a 90 degree angle to the short side,you have to subtract 90° (or π/2 radians) to get thedesired effect. Change the preceding code to read`rotate(angle - HALF_PI)` and try it again.Since Processing deals almost exclusively in radians,the language has defined the constants `PI` (180°),`HALF_PI` (90°), `QUARTER_PI` (45°)and `TWO_PI` (360°) for your convenience.

At this point, we can write the final version of thearm-tracking program. We start off with definitionsof constants and variables. The number 39in the definition of `MIDPOINT_X`comes from the fact that the body of the robot starts at*x*-coordinate 14 and is 50 pixels wide, so 39 (14 + 25)is the horizontal midpoint of the robot’s body.

```
# Where upper left of robot appears on screen 
ROBOT_X = 50
ROBOT_Y = 50

# The robot's midpoint and arm pivot points 
MIDPOINT_X = 39
LEFT_PIVOT_X = 12
RIGHT_PIVOT_X = 66
PIVOT_Y = 32

leftArmAngle = 0.0
rightArmAngle = 0.0

def setup():
    size(200, 200)
    smooth()
    frameRate(30)


```

The `draw()` function is next. It determines if themouse is pressed and the angle between the mouse locationand the pivot point, setting `leftArmAngle` and`rightArmAngle` accordingly.

```python
def draw():
   """
   Estas variáveis são para mouseX and mouseY,
   adjustadas para serem relativas ao sistema de coordenadas
   do robô em vez do sistema de coordenadas da janela.
   """
  
  background(255)
  pushMatrix()
  translate(ROBOT_X, ROBOT_Y)   # locar robô para caber braços
  if mousePressed:
      mX = mouseX - ROBOT_X
      mY = mouseY - ROBOT_Y
      if mX < MIDPOINT_X:    # lado direito do robô
        leftArmAngle = atan2(mY - PIVOT_Y,
                             mX - LEFT_PIVOT_X) - HALF_PI
      else:
        rightArmAngle = atan2(mY - PIVOT_Y,
                              mX - RIGHT_PIVOT_X) - HALF_PI;
      drawRobot()
  
  popMatrix()


```

The `drawRobot()` function remains unchanged, but a minor change to `drawLeftArm()` and `drawRightArm()`is now necessary. Because `leftArmAngle` and`rightArmAngle` are now computed in radians, thefunctions don’t have to do any conversion. As mudanças nas funções foram indicadas com comentários.

```python
def drawLeftArm():
    pushMatrix()
    translate(12, 32)
    rotate(leftArmAngle)  # mudou
    rect(-12, 0, 12, 37)  # braço esquerdo
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)
    rotate(rightArmAngle)  # mudou
    rect(0, 0, 12, 37)     # braço direito
    popMatrix()


```

Você pode [baixar os arquivos do tutorial original ](https://py.processing.org/tutorials/transform2d/imgs/transform2d.zip) (py.processing.org/tutorials/transform2d), incluido o programa para fazer os diagramas de grade.