<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### frustum()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/frustum_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
background(204); 
frustum(-width/2, width, 0, height, -100, 200.0); 
rotateY(PI/6); 
box(45); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Configura a matris de perspectiva através de
seus parâmetros. Trabalha como glFrustum, excetp que reinicializa
atual matriz de perspectiva em vez de fazer a
multiplicação a esta.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
frustum(<font color="#996600">esquerda</font>, <font color="#996600">direita</font>, <font color="#996600">inferior</font>, <font color="#996600">superior</font>, <font color="#996600">proximo</font>, <font color="#996600">distante</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
esquerda
float: coordenada esquerda do plano de recorte
direita
float:coordenada direita do plano de recorte
inferior
float: coordenada inferior do plano de recorte
superior
float: coordenada superior do plano de recorte
proximo
float: coordenada do plano de recorte mais próximo
distante
float: coordenada do plano de recorte mais distante
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[camera()](camera_)[endCamera()](endCamera_)[perspective()](perspective_)
