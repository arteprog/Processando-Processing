<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### bezierVertex()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/bezierVertex_.gif" width="100"/>

```pde
beginShape(LINE_STRIP); 
vertex(30, 20); 
bezierVertex(80, 0, 80, 75, 30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/bezierVertex_2.gif" width="100"/>

```pde
beginShape(POLYGON); 
vertex(30, 20); 
bezierVertex(80, 0, 80, 75, 30, 75); 
bezierVertex(50, 80, 60, 25, 30, 20); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Especifica as coordenadas de vértices para curvas de Bezier. Cada chamada a função**bezierVertex()**
define a posição de dois pontos de controle e um de
ancoragem de uma cruva de Bezier, e adiciona um novo segmento de uma
linha ou forma.  A primeira vez que bezierVertex() é
utilizada no escopo de uma chamada a beginShape(), deve sser prefaciada
com uma chamada a vertex() para estabelecer o primeiro ponto de
ancoragem. Esta função deve ser utilizada entre
beginShape() e endShape(), e pode ser utilizada apenas para desenhar os
tipos POLYGON, LINE_LOOP, e LINE_STRIP. O uso da versão 3D
requer a renderização com P3D ou OPENGL (ver a
referência ao Ambiente para mais informações).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
bezierVertex(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>)
bezierVertex(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">z1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">z2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>, <font color="#996600">z3</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x1
floar ou int: A coordenada-x do primeiro ponto de controle
y1
floar ou int: A coordenada-y do primeiro ponto de controle
z1
floar ou int: A coordenada-z do primeiro ponto de controle
x2
floar ou int: A coordenada-x of segundo ponto de controle
y2
floar ou int: A coordenada-y of segundo ponto de controle
z2
floar ou int: A coordenada-z of segundo ponto de controle
x3
floar ou int: A coordenada-x of ponto de ancoragem
y3
floar ou int: A coordenada-y of ponto de ancoragem
z3
floar ou int: A coordenada-z of ponto de ancoragem
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curveVertex()](curveVertex_)[vertex()](vertex_)[bezier()](bezier_)
