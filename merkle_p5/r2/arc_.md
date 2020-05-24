<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### arc()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/arc_.gif" width="100"/>

```pde
arc(50, 55, 50, 50, 0, PI/2); 
noFill(); 
arc(50, 55, 60, 60, PI/2, PI); 
arc(50, 55, 70, 70, PI, TWO_PI-PI/2); 
arc(50, 55, 80, 80, TWO_PI-PI/2, TWO_PI); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Desenha um arco na janela de
visualização. Arcos são desenhados ao longo da
borda de uma elipse definida pelos parâmentros**x**,**y**,**width** e**height**. A origem da respectiva elipse pode ser modificada através da função**ellipseMode()**. Os parâmetros**start** e**stop** especificam os ângulos em radianos a desenhar o arco.** **
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
ellipse(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">width</font>, <font color="#996600">height</font>, <font color="#996600">start</font>, <font color="#996600">stop</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
int ou float: coordenada-x da elipse que define o arco
y
int ou float: coordenada-y  da elipse que define o arco
width
int ou float: largura  da elipse que define o arco
height
int ou float: altura da elipse que define o arco
start
int ou float: ângulo onde iniciar o arco, especificado em radianos
stop
int ou float: ângulo onde terminar o arco, especificado em radianos
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[ellipseMode()](ellipseMode_)[ellipse()](ellipse_)
