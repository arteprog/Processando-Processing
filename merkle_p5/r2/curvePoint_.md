<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### curvePoint()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/curvePoint_.gif" width="100"/>

```pde
curve(5, 26, 5, 26, 73, 24, 73, 61); 
curve(5, 26, 73, 24, 73, 61, 15, 65); 
ellipseMode(CENTER); 
int steps = 6; 
for (int i = 0; i <= steps; i++) { 
  float t = i / float(steps); 
  float x = curvePoint(5, 5, 73, 73, t); 
  float y = curvePoint(26, 26, 24, 61, t); 
  ellipse(x, y, 5, 5); 
  x = curvePoint(5, 73, 73, 15, t); 
  y = curvePoint(26, 24, 61, 65, t); 
  ellipse(x, y, 5, 5); 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Avalia uma curva spline em ponto t para os
pontos a, b, c, e d. O parâmetro t varia entre 0 e 1; a e d
são pontos na curva; e b e c são pontos de controle. Isto
pode ser feito em uma primeira ocasião com as coordenadas x e em
um segundo momento com as coordenadas y pare se ter a
localização da curva spline em t.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
curvePoint(<font color="#996600">a</font>, <font color="#996600">b</font>, <font color="#996600">c</font>, <font color="#996600">d</font>, <font color="#996600">t</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
a
int ou float: coordenada do primeiro ponto sobre a curva
b
int ou float: coordenada do segundo ponto sobre a curva
c
int ou float: coordenada do terceiro ponto sobre a curva
d
int ou float: coordenada do quarto ponto sobre a curva
t
float: valor entre 0 e 1
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)[bezierPoint()](bezierPoint_)
