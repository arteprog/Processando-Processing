<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### vertex()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/vertex_.gif" width="100"/>

```pde
beginShape(POINTS); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/vertex_3.gif" width="100"/>

```pde
// O desenho de vértices em 3D requer P3D
// ou OPENGL com parâmetro de size()
size(100, 100, P3D); 
beginShape(POINTS); 
vertex(30, 20, -50); 
vertex(85, 20, -50); 
vertex(85, 75, -50); 
vertex(30, 75, -50); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/vertex_2.gif" width="100"/>

```pde
noStroke(); 
PImage a = loadImage("arch.jpg"); 
beginShape(); 
texture(a); 
// "arch.jpg" é ima imagem de 100x100 pixels, portanto
// os valores de 0 e 100 são utilizados para os 
// parâmetros "u" e "v" para se mapear diretamente 
// os pontos de vértice 
vertex(10, 20, 0, 0); 
vertex(80, 5, 100, 0); 
vertex(95, 90, 100, 100); 
vertex(40, 95, 0, 100); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Todos as formas são construídas pela conexão de uma série de vértices.**vertex() ** é
utilizada para especificar as coordenadas de pontos, linhas,
triângulos, quadriláteros e  polígonos, e
é utilizada exclusivamente entre chamadas à**beginShape() **e**endShape()**.

O desenho de um vértice em 3D através dop uso do parâmetro**z ** requer o uso do parâmetro P3D ou  OPENGL em combinação co size, como ilustrado no exemplo acima.
Esta função também é utilizada para mapear
uma textura sobre uma forma geométrica. A função**texture() ** decalra a textura a ser aplicada sobre a forma geométrica e as coordenadas**u** e**v** definem o mapeamento desta textura à forma. Como padrão, as coordenadas utilizadas para**u** e**v**
são especificadas em relação ao tamanho da imagem
em pixels, mas esta relação pode ser modificada
através da função**textureMode()**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
vertex(<font color="#996600">x</font>, <font color="#996600">y</font>); 
vertex(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>); 
vertex(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">u</font>, <font color="#996600">v</font>); 
vertex(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>, <font color="#996600">u</font>, <font color="#996600">v</font>); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
int ou float: coordenada-x do vértice
y
int ou float: coordenada-y do vértice
z
int ou float: coordenada-z do vértice
u
int ou float: coordenada horizontal da textura de mapeamento
v
int ou float: coordenada vertica da textura de mapeamento
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application & Web
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[beginShape()](beginShape_)[endShape()](endShape_)[bezierVertex()](bezierVertex_)[curveVertex()](curveVertex_)[texture()](texture_)
