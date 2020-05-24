<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### curveVertex()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/curveVertex_.gif" width="100"/>

```pde
beginShape(LINE_STRIP); 
curveVertex(84,  91); 
curveVertex(84,  91); 
curveVertex(68,  19); 
curveVertex(21,  17); 
curveVertex(32, 100); 
curveVertex(32, 100); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Especifica as coordenadas de vértices para curvas. Esta função só pode ser chamada entre**beginShape()** e**endShape()** e pode ser utilizada apenas para desenhar os
tipos  POLYGON, LINE_LOOP, e LINE_STRIP. O uso da versão 3D
requer a renderização com P3D ou OPENGL (ver a
referência ao Ambiente para mais informações).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
curveVertex(<font color="#996600">x</font>, <font color="#996600">y</font>) 
curveVertex(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
float ou int: A coordenada-x do vértice
y
float ou int: A coordenada-y do vértice
z
float ou int: A coordenada-z do vértice
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application & Web
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curve()](curve_)[beginShape()](beginShape_)[endShape()](endShape_)[vertex()](vertex_)[bezierVertex()](bezierVertex_)
