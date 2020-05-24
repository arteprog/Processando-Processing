<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### translate()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/translate_.gif" width="100"/>

```pde
translate(30, 20); 
rect(0, 0, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/translate_2.gif" width="100"/>

```pde
// Translating in 3D requires P3D 
// or OPENGL as a parameter to size() 
size(100, 100, P3D); 
translate(30, 20, -50); 
rect(0, 0, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/translate_3.gif" width="100"/>

```pde
translate(30, 20); 
rect(0, 0, 55, 55); 
translate(14, 14); 
rect(0, 0, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Especifica a quantidade de deslocamento na janela de visualização. O parâmetro**x** especifica as traslações direita/esquerda; o parâmetro**y** especifica trasnlações acima/abaixo; e o parâmetro**z ** especifica
translações em direção à ou
além da tela. A utilização desta
função com o parâmetro**z ** requer a passagem
de P3D ou OPENGL como parâmetro à função
size(),  como mostrado no exemplo acima. Transformações se aplicam a
todos eventos que aconteçam após
sua chamada, e chamadas subseqüentes multiplicam seu efeito.  Por exemplo, ao se chamar**translate(50.0,0.0) ** e em seguida** translate(20.0,0.0) **equivale a se chamar**translate(70.0. 0.0)**. Quando** tranalte****() **é chamada dentro de**draw()**,
a transformação é reinicializada ao começo
do novo laço.  Outors controles sobre
aplicação de tranaformações são
obtidas através do uso de**pushMatrix()** e**popMatrix()**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
translate(<font color="#996600">x</font>, <font color="#996600">y</font>);
translate(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
int ou float: translação à direira ou à esquerda
y
int ou float: translação para cima ou para baixo
z
int ou float: tranalação à frente ou à ré
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[rotate() ](rotate_)[rotateX()](rotateX_)[rotateY()](rotateY_)[rotateZ()](rotateZ_)[scale(](scale_)[pushMatrix()](pushMatrix_)[popMatrix(](popMatrix_)
