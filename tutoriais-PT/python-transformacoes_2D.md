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

Let’s look at the translation code in more detail.`pushMatrix()` is a built-in function thatsaves the current position of the coordinate system. The `translate(60, 80)` moves the coordinate system 60 units rightand 80 units down. The `rect(20, 20, 40, 40)` draws therectangle at the same place it was originally. Remember, the things you drawdon’t move—the grid moves instead. Finally,`popMatrix()` restores the coordinate system to the way it wasbefore you did the translate.

Yes, you could have done a `translate(-60, -80)` tomove the grid back to its original position. However, when you startdoing more sophisticated operations with the coordinate system, it’seasier to use `pushMatrix()` and `popMatrix()` tosave and restore the status rather than having to undo all your operations.Later on in this tutorial, you will find out why those functionsseem to have such strange names.

### What’s the Advantage?

You may be thinking that picking up the coordinate system and moving itis a lot more trouble than just adding to coordinates. For a simple examplelike the rectangle, you are correct. But let’s take an example ofwhere `translate()` can make life easier. Here is somecode that draws a row of houses. It uses a loop that callsfunction named `house()`, which takesthe *x* and *y* location of the house’s upper-left corner as its parameters.

![Row of stick-figure houses](https://py.processing.org/tutorials/transform2d/imgs/houses.png)

```python
def setup():
  size(400, 100)
  background(255)
  for i in xrange(10,350,50):
    house(i, 20)

```

This is the code for drawing the house by changing itsposition. Look at all the additions that youhave to keep track of.

```python
def house(int x, int y):
  triangle(x + 15, y, x, y + 15, x + 30, y + 15)
  rect(x, y + 15, 30, 30)
  rect(x + 12, y + 30, 10, 15)

```

Compare isso com esta versão da função que usa `translate()`. Neste caso o código desenha a casa no mesmo lugar, com o canto superior esquerdo em (0, 0), e deixa a translação fazer todo o trabalho.

Compare that to the version of the function that uses `translate()`. In this case, the code draws the house in the same place every time,with its upper left corner at (0, 0), and lets translation do all thework instead.

```python
def house(int x, int y):
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

Since most people think in degrees, Processing has a built-in `radians()` functionwhich takes a number of degrees as its argument and converts it for you.  It also hasa `degrees()` function that converts radians to degrees. Given that background,let’s try rotating a square clockwise 45 degrees.

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

Hey, what happened? How come the square got moved and cut off?The answer is: the square did not move. The **grid** was rotated.Here is what really happened. As you can see, on the rotated coordinate system,the square still has its upper left corner at (40, 40).

![shows grid rotated 45 degrees clockwise](https://py.processing.org/tutorials/transform2d/imgs/rotated_grid.png)

### Girando da maneira certa

A maneira certa de girar o quadrado é:

1. Faça a translação da origem do sistema de coordenadas (0, 0) para onde você quer que seja o canto superior esquerdo do quadrado.
2. Gire a grade π/4 radianos (45°)
3. Desenhe o quadrado na origem.

![Grid translated, then rotated](https://py.processing.org/tutorials/transform2d/imgs/correct_rotate_grid.png)

And here is the code and its result, without the grid marks.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    fill(192)
    noStroke()
    rect(40, 40, 40, 40)
    
    pushMatrix()
    # move the origin to the pivot point
    translate(40, 40)
    
    # then pivot the grid
    rotate(radians(45))
    
    # and draw the square at the origin
    fill(0)
    rect(0, 0, 40, 40)
    popMatrix()


```

And here is a program that generates a wheel of colors by usingrotation. The screenshot is reduced to save space.

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

### Scaling

The final coordinate system transformation isscaling, which changes the size of the grid. Take a look at this example,which draws a square, then scales the grid to twice its normal size,and draws it again.

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

First, you can see that the square appears to have moved. It hasn’t, ofcourse. Its upper left corner is still at (20, 20) on thescaled-up grid, but that point isnow twice as far away from the origin as it was in the original coordinatesystem. You can also see that the lines are thicker. That’s no opticalillusion—the lines really are twice as thick, because the coordinate systemhas been scaled to double its size.

> **Desafio de programação** aumente a o tamnaho do quadrado preto, mas mantenha o cantto superior esquerdo dele no mesmo lugar do quadrado cinza. Dica: use `translate()` para mover a origem, então use `scale()`.


Não tem um lei que diz que você tem que escalar as dimensões em *x* e *y* igualmente. Tente usar `scale(3.0, 0.5)` para fazer a dimensão em  *x* três vezes maior e a dimensão em *y* metado do tamanho normal.

### A ordem importa

When you do multiple transformations, the order makes a difference. A rotationfollowed by a translate followed by a scale will not give the same results as atranslate followed by a rotate by a scale. Here is some sample code andthe results.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    line(0, 0, 200, 0)  # draw axes
    line(0, 0, 0, 200)
    
    pushMatrix()
    fill(255, 0, 0)     # red square
    rotate(radians(30))
    translate(70, 70)
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()

    pushMatrix()
    fill(255)           # white square
    translate(70, 70)
    rotate(radians(30))
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()


```

### A matriz de transformação

Every time you do a rotation, translation, or scaling, the informationrequired to do the transformation is accumulated into a table ofnumbers. This table, or matrix has only a few rowsand columns, yet, through the miracle of mathematics, it contains all theinformation needed to do any series of transformations. And that’swhy the `pushMatrix()` and `popMatrix()` have thatword in their name.

### Push e Pop

What, about the *push* and *pop* part of the names? These come from a computerconcept known as a stack, which works like a spring-loaded traydispenser in a cafeteria. When someone returns a tray to the stack, its weight pushes the platform down.When someone needs a tray, he takes it from the top of the stack,and the remaining trays pop up a little bit.

In a similar manner, `pushMatrix()` puts the current status ofthe coordinate system at the top of a memory area, and `popMatrix()`pulls that status back out. The preceding example used`pushMatrix()` and `popMatrix()` to make sure that thecoordinate system was “clean” before each part of the drawing.In all of the other examples, the calls to those two functions weren’treally necessary, but it doesn’t hurt anything to save and restorethe grid status.

Note: in Processing, the coordinate system is restored to its original state(origin at the upper left of the window, no rotation, and no scaling) everytime that the `draw()` function is executed.

### Transformações Tri-dimensionais

If you are working in three dimensions, you can call the`translate()` function with three arguments for the*x*, *y*, and *z* distances. Similarly, you cancall `scale()` with three arguments that tell howmuch you want the grid scaled in each of those dimensions.

For rotation, call the `rotateX()`, `rotateY()`, or `rotateZ()` functionto rotate around each of the axes. All three of these functionsexpect one argument: the number of radians to rotate.

### Estudo de caso: Um robô que balança os braços

Let’s use these transformations to animate a bluerobot waving its arms. Rather than try to write it all atonce, we will do the work in stages. The first step isto draw the robot without any animation.

The robot is modeled on[thisdrawing](http://www.openclipart.org/detail/5457), although it will not look as charming.First, we draw the robot so that itsleft and top side touch the *x* and *y* axes. Thatwill allow us to use `translate()` to easily placethe robot anywhere we want or to make multiple copies ofthe robot, as we did in the example of the houses.

When we refer to left and right in this drawing, we mean yourleft and right (the left and right side of your monitor),not the robot’s left and right.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    drawRobot()

def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)      # head
    rect(14, 32, 50, 50)     # body
    
    rect(0, 32, 12, 37)      # left arm
    rect(66, 32, 12, 37)     # right arm
    
    rect(22, 84, 16, 50)     # left leg
    rect(40, 84, 16, 50)     # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12)  # left eye
    ellipse(47, 12, 12, 12)  # right eye

```

![robot with red dots at shoulder joints](https://py.processing.org/tutorials/transform2d/imgs/pivot.png)The next step is to identify the points wherethe arms pivot. That is shown in this drawing.The pivot points are (12, 32) and(66, 32). Note: the term “center of rotation”is a more formal term for the pivot point.

Now, separate the code for drawing the left and rightarms, and move the center of rotation for each arm to the origin, becauseyou always rotate around the (0, 0) point. To save space,we are not repeating the code for `setup()`.

```python
def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)      # head
    rect(14, 32, 50, 50)     # body
    drawLeftArm()
    drawRightArm()
    rect(22, 84, 16, 50)     # left leg
    rect(40, 84, 16, 50)     # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12)  # left eye
    ellipse(47, 12, 12, 12)  # right eye

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

Now test to see if the arms rotate properly.Rather than attempt a full animation, we will justrotate the left side arm 135 degreesand the right side arm -45 degrees as a test. Hereis the code that needs to be added, and the result.The left side arm is cut off because of the windowboundaries, but we’ll fix that in the finalanimation.

```python
def drawLeftArm():
    pushMatrix()
    translate(12, 32)

    rotate(radians(135))

    rect(-12, 0, 12, 37)    # left arm
    popMatrix()

def drawRightArm():
    pushMatrix()
    translate(66, 32)

    rotate(radians(-45))

    rect(0, 0, 12, 37)     # right arm
    popMatrix()


```

Now we complete the program by putting in the animation. Theleft arm has to rotate from 0° to 135° and back.Since the arm-waving is symmetric, theright-arm angle will always be the negative value ofthe left-arm angle. To make things simple,we will go in increments of 5degrees. 

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
    translate(50, 50)       # place robot so arms are always on screen
    drawRobot()
    armAngle += angleChange
  
    # if the arm has moved past its limit,
    # reverse direction and set within limits.
    if (armAngle > ANGLE_LIMIT or armAngle < 0):
        angleChange = -angleChange
        armAngle += angleChange
    popMatrix()


def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)     # head
    rect(14, 32, 50, 50)    # body
    drawLeftArm()
    drawRightArm()
    rect(22, 84, 16, 50)    # left leg
    rect(40, 84, 16, 50)    # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12) # left eye
    ellipse(47, 12, 12, 12) # right eye

def drawLeftArm():
    global armAngle
    pushMatrix()
    translate(12, 32)

    rotate(radians(armAngle))

    rect(-12, 0, 12, 37)    # left arm
    popMatrix()

def drawRightArm():
    global armAngle
    pushMatrix()
    translate(66, 32)

    rotate(radians(-armAngle))

    rect(0, 0, 12, 37)     # right arm
    popMatrix()
```

### Estudo de caso: Rotação interativa

Instead of having the arms move on their own, we will modify the programso that the arms follow the mouse while the mouse button is pressed. Insteadof just writing the program at the keyboard, we first think about theproblem and figure out what the program needs to do. 

Since the two arms move independently ofone another, we need to have one variable for each arm’s angle.It’s easy to figure out which arm to track. If the mouse is at theleft side of the robot’s center, track the left arm; otherwise,track the right arm.

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
   These variables are for mouseX and mouseY,
   adjusted to be relative to the robot's coordinate system
   instead of the window's coordinate system.
   """
  
  background(255)
  pushMatrix()
  translate(ROBOT_X, ROBOT_Y)   # place robot so arms are always on screen
  if mousePressed:
      mX = mouseX - ROBOT_X
      mY = mouseY - ROBOT_Y
      if mX < MIDPOINT_X:    # left side of robot
        leftArmAngle = atan2(mY - PIVOT_Y, mX - LEFT_PIVOT_X) - HALF_PI
  else:
        rightArmAngle = atan2(mY - PIVOT_Y, mX - RIGHT_PIVOT_X) - HALF_PI;
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

You can [download the files from this tutorial](https://py.processing.org/tutorials/transform2d/imgs/transform2d.zip),including the program that made the grid diagrams.