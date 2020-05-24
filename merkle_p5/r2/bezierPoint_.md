
#### Nome
### bezierPoint()

#### Exemplos
<img border="0" height="100" src="media/bezierPoint_.gif" width="100"/>

```pde
bezier(85, 20, 10, 10, 90, 90, 15, 80); 
ellipseMode(CENTER); 
int steps = 10; 
for (int i = 0; i <= steps; i++) { 
  float t = i / float(steps); 
  float x = bezierPoint(85, 10, 90, 15, t); 
  float y = bezierPoint(20, 10, 90, 80, t); 
  ellipse(x, y, 5, 5);
} 

```

#### Descrição
Avalia uma curva de Bezier em ponto t para os
pontos a, b, c, e d. O parâmetro t varia entre 0 e 1; a e d
são pontos na curva; e b e c são pontos de controle. Isto
pode ser feito em uma primeira ocasião com as coordenadas x e em
um segundo momento com as coordenadas y pare se ter a
localização da curva de bezier em t.

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
