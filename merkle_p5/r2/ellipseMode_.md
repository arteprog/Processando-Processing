<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ellipseMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/ellipseMode_.gif" width="100"/>

```pde
ellipseMode(CENTER); 
ellipse(35, 35, 50, 50); 
ellipseMode(CORNER); 
fill(102); 
ellipse(35, 35, 50, 50); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
A origem de uma elipse pode ser modificada através da função**ellipseMode()**.  A configuração padrão é**ellipseMode(CENTER)**,
 a qual especifica a localização de uma elipse como
sendo  o centro de sua forma. O modo CENTER_RADIUS funciona do
mesmo modo, mas os parâmetros width e height repassados à
fun;cão**ellipse()**
especificam os raios da elipse, ao invés de seu diâmetro.
O modo CORNER desenha a forma a partir do canto superior esquerdo da
caixa que a define. O modo CORNERS utiliza os quatro parâmetros
de**ellipse()** para especificar
os dois cantos opostos da caixa que faz fronteira com a forma.
 O parâmetro precisa ser todo escrito "MAIÚSCULA"
pelo fato de Processing ser uma linguagem onde letras
mínúsculas e maiúsculas são diferentes (*case sensitive*).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
ellipseMode(<font color="#996600">MODO</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODO
Qualquer entre: CENTER, CENTER_RADIUS, CORNER, ou CORNERS.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[ellipse()](ellipse_)
