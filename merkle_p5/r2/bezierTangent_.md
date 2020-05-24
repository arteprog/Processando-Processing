
#### Nome
### bezierTangent()

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

#### Descrição
Calcula a tangente de um ponto sobre uma curva de
bezier. Há uma boa definição de tangente na
Wikipedia:[http://en.wikipedia.org/wiki/Tangent](http://en.wikipedia.org/wiki/Tangent)

#### Sintaxe
```pde
bezierPoint(a, b, c, d, t)

```
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

#### Utilização

	
Web & Applicações

#### Relacionado
[bezier()](bezier_)[bezierVertex()](bezierVertex_)[curvePoint()](curvePoint_)
