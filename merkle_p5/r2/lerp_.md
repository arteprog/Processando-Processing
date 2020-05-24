<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### lerp()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/lerp_.gif" width="100"/>

```pde
float a = 20; 
float b = 80; 
float c = lerp(a, b, .2); 
float d = lerp(a, b, .5); 
float e = lerp(a, b, .8); 
beginShape(POINTS); 
vertex(a, 50); 
vertex(b, 50); 
vertex(c, 50); 
vertex(d, 50); 
vertex(e, 50); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/lerp_2.gif" width="100"/>

```pde
int x1 = 15; 
int y1 = 10; 
int x2 = 80; 
int y2 = 90; 
line(x1, y1, x2, y2); 
for(int i=0; i<=10; i++) { 
  float x = lerp(x1, x2, i/10.0) + 10; 
  float y = lerp(y1, y2, i/10.0); 
  point(x, y); 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula um número entre dois números em um incremento expecífico. O parâmetro**amt **representa
a quantidade a interpolar entre os dois valores, onde 0.0 equivale ao
primeiro ponto;  0.1 está muito próximo deste
primeire ponto;  0.5  está a meio caminho entre os
dois, etc.  A função lerp() é conveniente
para se criar movimento ao longo de um caminho reto, e para se criar
linhas tracejadas.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
lerp(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">amt</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor1
float ou int: primeiro valor
valor2
float ou int: segundo valor
amt
float: entre 0.0 e 1.0
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curvePoint()](curvePoint_)[bezierPoint()](bezierPoint_)
