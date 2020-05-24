
#### Nome
### curve()

#### Exemplos
<img border="0" height="100" src="media/curve_.gif" width="100"/>

```pde
stroke(255, 102, 0); 
curve(5, 26, 5, 26, 73, 24, 73, 61); 
stroke(0); 
curve(5, 26, 73, 24, 73, 61, 15, 65); 
stroke(255, 102, 0); 
curve(73, 24, 73, 61, 15, 65, 15, 65); 

```

#### Descrição
Desenha uma linha curva na tela.  O primeiro e
o segundo parâmetros especificam o primeiro ponto de ancoragem e
os dois  últimos  o segundo ponto de ancoragem. Os
parâmetros do meio especificam os pontos que definem a forma da
curva.  Curvas longas podem ser criadas ao se justapor uma
série de funções**curve().  **Uma  função adicional chamada**curveTightness() **permite o controle da qualidade visual da curva. A função**curve()**
 é uma implementação das splines de
Carmull-Rom.  A utilização da versão 3D
requer a renderização com P3D ou OPENGL (ver
referência ao Ambiente para mais
informaçãoes).

#### Sintaxe
```pde
curve(x1, y1, x2, y2, x3, y3, x4, y4);
curve(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4);

```
Parâmetros
x1, y1, z1
int or float: coordenadas da primeira ângora
x2, y2, z2
int or float: coordenadas do primeirio ponto
x3, y3, z3
int or float: coordenadas do segundo ponto
x4, y4, z4
int or float: coordenadas da segunda âncora

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[curveVertex()](curveVertex_)[bezier()](bezier_)
