# **2D Transformations**

### **by J David Eisenberg**

Você já aprendeu que pode mudar a posição onde desenha um retângulo. Mas há uma maneira diferente de fazer isso. E se você **mover a grade de coordenadas? 
**O efeito visual obtido é o mesmo. Isso se chama translação. **Qual a vantagem?**





'''Compare com esta versão que usa o translate(). Neste caso o código desenha a casa no mesmo lugar, com o canto superior esquerdo em (0, 0), e a translação, *In this case, the code draws the house in the same place every time, with its upper left corner at (0, 0), and lets translation do all the work instead!*'''


Além da translação que move a grade, é possível girar o sistema de coordenadas com a função **rotate()**. Essa função tem um parâmetro ou argumento, um número de *radianos* que você quer rodar. Em graus, um círculo tem 360°. Quando descrevemos os ângulos em radianos, a circuferência completa tem  2π radianos.

*Here is a diagram of how Processing measures angles in degrees (black) and radians (red).** **Processing has a built-in radians() function which takes a number of degrees as its argument and converts it for you. It also has a degrees() function that converts radians to degrees. Given that background, let’s try rotating a square clockwise 45 degrees.*



  
     

*Hey, what happened? How come the square got moved and cut off? The answer is: the square did not move. The ***_grid_*** was rotated. Here is what really happened. As you can see, on the rotated coordinate system, the square still has its upper left corner at (40, 40).*

### **Girando da maneira certa**

A maneira certa de girar o quadrado é::

1. Mova a origem do sistema de coordenadas (0, 0) para onde você quer que seja o canto superior esquerdo do quadrado.

2. Gire a grade π/4 radianos (45°)

3. Desenhe o quadrado na origem.



void setup() {
  size(200, 200);
  background(255);
  smooth();
  noStroke();
}

void draw(){
  if (frameCount % 10 == 0) {
    fill(frameCount * 3 % 255, frameCount * 5 % 255,
      frameCount * 7 % 255);
    pushMatrix();
    translate(100, 100);
    rotate(radians(frameCount * 2  % 360));
    rect(0, 0, 80, 20);
    popMatrix();
  }
}

void setup() {

  smooth();

  size(300,300);

  background(0);

}

void draw() {

  translate(mouseX, mouseY);

  rotate(frameCount/3);

  strokeWeight(20+sin(frameCount)*20);

  stroke(abs(sin(frameCount/10)*255), abs(cos(frameCount/10)*255), abs(cos(frameCount/10)*255), 75);

  line(0, 0, 0, random(height/2));

  line(0, 0, 0, -random(height/2));

}

