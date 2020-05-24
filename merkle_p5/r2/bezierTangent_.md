<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### bezierTangent()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/bezierTangent_.gif" width="100"/>

```pde
bezier(85, 20, 10, 10, 90, 90, 15, 80); 
ellipseMode(CENTER_DIAMETER); 
int steps = 6; 
for (int i = 0; i <= steps; i++) { 
  float t = i / float(steps); 
  // Pega a coordenada do ponto
  float x = bezierPoint(85, 10, 90, 15, t); 
  float y = bezierPoint(20, 10, 90, 80, t); 
  // Pega os pontos de tangência
  float tx = bezierTangent(85, 10, 90, 15, t); 
  float ty = bezierTangent(20, 10, 90, 80, t); 
  // Calcula os ângulo dos pontos de tangêncoa
  float a = atan2(ty, tx); 
  stroke(255, 102, 0); 
  line(x, y, cos(a)*30 + x, sin(a)*30 + y); 
  // Apróxima linha de códico faz a linha
  // inversa da linha acima
  //line(x, y, cos(a)*-30 + x, sin(a)*-30 + y); 
  stroke(0); 
  ellipse(x, y, 5, 5); 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/bezierTangent_2.gif" width="100"/>

```pde
bezier(85, 20, 10, 10, 90, 90, 15, 80); 
stroke(255, 102, 0); 
int steps = 16; 
for (int i = 0; i <= steps; i++) { 
  float t = i / float(steps); 
  float x = bezierPoint(85, 10, 90, 15, t); 
  float y = bezierPoint(20, 10, 90, 80, t); 
  float tx = bezierTangent(85, 10, 90, 15, t); 
  float ty = bezierTangent(20, 10, 90, 80, t); 
  float a = atan2(ty, tx); 
  a += PI/2.0; 
  line(x, y, cos(a)*8 + x, sin(a)*8 + y); 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula a tangente de um ponto sobre uma curva de
bezier. Há uma boa definição de tangente na
Wikipedia:[http://en.wikipedia.org/wiki/Tangent](http://en.wikipedia.org/wiki/Tangent)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
bezierPoint(<font color="#996600">a</font>, <font color="#996600">b</font>, <font color="#996600">c</font>, <font color="#996600">d</font>, <font color="#996600">t</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
a
int ou float: coordenada do primeiro ponto na curva
b
int ou float: coordenada do primeiro ponto de controle
c
int ou float: coordenada do segundo ponto de controle
d
int ou float: coordenada do segundo ponto na curva
t
float: valor entre 0 e 1
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[bezier()](bezier_)[bezierVertex()](bezierVertex_)[curvePoint()](curvePoint_)
