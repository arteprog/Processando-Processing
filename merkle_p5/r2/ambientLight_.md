<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ambientLight()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/ambientLight_.gif" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
// O padrão de cor das esferas é o branco
// A cor ambiente modifica suas cores
ambientLight(51, 102, 126); 
translate(20, 50, 0); 
sphere(30); 
translate(60, 0, 0); 
sphere(30); 
 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/directional_ambient_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
directionalLight(126, 126, 126, 0, 0, -1); 
ambientLight(102, 102, 102); 
translate(32, 50, 0); 
rotateY(PI/5); 
box(40); 
translate(60, 0, 0); 
sphere(30); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Adiciona uma luz ambiente. A luz ambiente
não vem de uma direção específica, pois os
raioz lunminosos já refletiram tanto que os objetos são
iluminados igualmente de todos os lados. Luzes ambientes geralmente
são utilizadas em combinação com outros tipos de
luzes. Luzes precisam ser incluidas em**draw()** para se manterem persistentes em programas em laço. A sua colocação no**setup()**
de um programa em laço causará edeito apenas
 durante a primeira passagem pelo laço. O efeito de seus
parâmetros é determinado pelo atual modo de cor.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
ambientLight(<font color="#996600">v1</font>, <font color="#996600">v2</font>, <font color="#996600">v3</font>)
ambientLight(<font color="#996600">v1</font>, <font color="#996600">v2</font>, <font color="#996600">v3</font>, <font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
v1
int ou float: valor de vermelho ou de matiz
v2
int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho
x
int ou float: coordenada-x da luz
y
int ou float: coordenada-y da luz
z
int ou float: coordenada-z da luz
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[lights()](lights_)[directionalLight()](directionalLight_)[pointLight()](pointLight_)[spotLight()](spotLight_)
