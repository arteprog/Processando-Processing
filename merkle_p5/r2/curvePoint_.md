
#### Nome
### curvePoint()

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

#### Descrição
Avalia uma curva spline em ponto t para os
pontos a, b, c, e d. O parâmetro t varia entre 0 e 1; a e d
são pontos na curva; e b e c são pontos de controle. Isto
pode ser feito em uma primeira ocasião com as coordenadas x e em
um segundo momento com as coordenadas y pare se ter a
localização da curva spline em t.

#### Sintaxe
```pde
curvePoint(a, b, c, d, t)

```
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

#### Utilização

	
Web & Applicações

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)[bezierPoint()](bezierPoint_)
