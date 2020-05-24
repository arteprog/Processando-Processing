
#### Nome
### lerp()

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

#### Descrição
Calcula um número entre dois números em um incremento expecífico. O parâmetro `amt `representa
a quantidade a interpolar entre os dois valores, onde 0.0 equivale ao
primeiro ponto;  0.1 está muito próximo deste
primeire ponto;  0.5  está a meio caminho entre os
dois, etc.  A função lerp() é conveniente
para se criar movimento ao longo de um caminho reto, e para se criar
linhas tracejadas.

#### Sintaxe
```pde
lerp(valor1, valor2, amt)

```
Parâmetros
valor1
float ou int: primeiro valor


valor2
float ou int: segundo valor


amt
float: entre 0.0 e 1.0



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[curvePoint()](curvePoint_
)
[bezierPoint()](bezierPoint_
)

