<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### bezier()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/bezier_.gif" width="100"/>

```pde
stroke(255, 102, 0); 
line(85, 20, 10, 10); 
line(90, 90, 15, 80); 
stroke(0, 0, 0); 
bezier(85, 20, 10, 10, 90, 90, 15, 80); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/bezier_2.gif" width="100"/>

```pde
stroke(255, 102, 0); 
line(30, 20, 80, 5); 
line(80, 75, 30, 75); 
stroke(0, 0, 0); 
bezier(30, 20,  80, 5,  80, 75,  30, 75); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Desenha uma curva Bezier na tela. Esta curvas
são definidas por uma série de pontos de controle e de
ancoragem.  Os dois primeiros e dos dois últimos
parâmetros representam  o primeiro ponto de ancoragem. Os
parâmetros do meio especificam os pontos de controle que definem
a forma da curva.  As cruvas de Bezier foram desenvolvidas pelo
engenheiro francês Pierre Bezier. A utilização da
versão 3D requer a renderização com  P3D ou
OPENGEL (veja a referência do Ambiente para mais
informações).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
bezier(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>, <font color="#996600">x4</font>, <font color="#996600">y4</font>);
bezier(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">z1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">z2</font>, <font color="#996600">x3</font>, <font color="#996600">y3</font>, <font color="#996600">z3</font>, <font color="#996600">x4</font>, <font color="#996600">y4</font>, <font color="#996600">z4</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x1, y1, z1
int ou float: coordenadas do primeiro ponto de ancoragem
x2, y2, y3
int ou float: coordenadas do primeiro ponto de controle
x3, y3, z3
int ou float: coordenadas do segundo ponto de controle
x4, y4, z4
int ou float: coordenadas do segundo ponto de ancoragem
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[bezierVertex()](bezierVertex_)[curve()](curve_)
