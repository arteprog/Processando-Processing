<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### curve()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
curve(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>, <font color="#996600">x4</font>, <font color="#996600">y4</font>);
curve(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">z1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">z2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>, <font color="#996600">z3</font>, <font color="#996600">x4</font>, <font color="#996600">y4</font>, <font color="#996600">z4</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x1, y1, z1
int or float: coordenadas da primeira ângora
x2, y2, z2
int or float: coordenadas do primeirio ponto
x3, y3, z3
int or float: coordenadas do segundo ponto
x4, y4, z4
int or float: coordenadas da segunda âncora
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curveVertex()](curveVertex_)[bezier()](bezier_)
