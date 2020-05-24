<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### pointLight()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/pointLight_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
pointLight(51, 102, 126, 35, 40, 36); 
translate(80, 50, 0); 
sphere(30); 
 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Adiciona um luz pontual.  Luzes precisam
ser incluidas em**draw()** para se manterem persistentes em programas em laço. A sua colocação no**setup()**
de um programa em laço causará efeito apenas
 durante a primeira passagem pelo laço. Os efeitos dos parâmetros**v1**,**v2**, e**v3** parameters são determinados pelo atual modo de cor. Os par6ametros**x**,**y**, e**z **especificam a posição da luz.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
pointLight(<font color="#996600">v1</font>, <font color="#996600">v2</font>, <font color="#996600">v3</font>, <font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
v1
int ou float: valor de vermelho ou de matiz
v2
int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho
x
int ou float: coordenada x da luz pontual
y
int ou float: coordenada y da luz pontual
z
int ou float: coordenada z da luz pontual
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[lights()](lights_)[directionalLight()](directionalLight_)[ambientLight()](ambientLight_)[spotLight()](spotLight_)
