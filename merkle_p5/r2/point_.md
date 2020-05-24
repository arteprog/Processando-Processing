<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### point()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/point_.gif" width="100"/>

```pde
point(30, 20); 
point(85, 20); 
point(85, 75); 
point(30, 75); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/point_2.gif" width="100"/>

```pde
size(100, 100, P3D); 
point(30, 20, -50); 
point(85, 20, -50); 
point(85, 75, -50); 
point(30, 75, -50); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Desenha um ponto na janela de
visualização de dimensão de um píxel. O
primeiro parâmetro é o valor da coordenada horizontal do
ponto, o segundo o valor da vertical, e o terceiro, opcional, o valor
da profundidade.  Para desenhar esta forma em 3D através da
utilização do parâmetro**z**,
requer-se que o parâmetro P3D ou OPENGL tenha sido repassado
à função size(), que configura a janela de
visualização, como ilustrado no exemplo acima.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
point(<font color="#996600">x</font>, <font color="#996600">y</font>); 
point(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
int ou float: coordenada-x do ponto
y
int ou float: coordenada-y do ponto
z
int ou float: coordenada-z do ponto
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[beginShape()](beginShape_)
