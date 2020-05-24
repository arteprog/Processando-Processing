<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### beginShape()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/beginShape_0.gif" width="100"/>

```pde
beginShape(); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_.gif" width="100"/>

```pde
beginShape(POINTS); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_2.gif" width="100"/>

```pde
beginShape(LINES); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_3.gif" width="100"/>

```pde
beginShape(LINE_STRIP); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_4.gif" width="100"/>

```pde
beginShape(LINE_LOOP); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_5.gif" width="100"/>

```pde
beginShape(TRIANGLES); 
vertex(30, 75); 
vertex(40, 20); 
vertex(50, 75); 
vertex(60, 20); 
vertex(70, 75); 
vertex(80, 20); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_6.gif" width="100"/>

```pde
beginShape(TRIANGLE_STRIP); 
vertex(30, 75); 
vertex(40, 20); 
vertex(50, 75); 
vertex(60, 20); 
vertex(70, 75); 
vertex(80, 20); 
vertex(90, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_65.gif" width="100"/>

```pde
beginShape(TRIANGLE_FAN); 
vertex(57.5, 50); 
vertex(57.5, 15); 
vertex(92, 50); 
vertex(57.5, 85); 
vertex(22, 50); 
vertex(57.5, 15); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_7.gif" width="100"/>

```pde
beginShape(QUADS); 
vertex(30, 20); 
vertex(30, 75); 
vertex(50, 75); 
vertex(50, 20); 
vertex(65, 20); 
vertex(65, 75); 
vertex(85, 75); 
vertex(85, 20); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_8.gif" width="100"/>

```pde
beginShape(QUAD_STRIP); 
vertex(30, 20); 
vertex(30, 75); 
vertex(50, 20); 
vertex(50, 75); 
vertex(65, 20); 
vertex(65, 75); 
vertex(85, 20); 
vertex(85, 75); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/beginShape_9.gif" width="100"/>

```pde
beginShape(POLYGON); 
vertex(20, 20); 
vertex(40, 20); 
vertex(40, 40); 
vertex(60, 40); 
vertex(60, 60); 
vertex(20, 60); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
O uso das funções**beginShape() ** e**endShape()** permite a criação de formas mais complexas. A função**beginShape()** inicia o armazenmento dos vértices de uma forma e**endShape()** o interrompe. O valor do parâmetro**MODO**
LINES, LINE_STRIP, LINE_LOOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP,
QUADS, QUAD_STRIP, e POLYGON. especifica qual o tipo de formas
serão criadas a partir dos vértices providos. Os
par6ametros disponíveis para beginShape() são  Caso
não haja**MODO** especificado, o padrão utilizado é POLYGON. Após a chamada a função**beginShape()**, deve seguir uma série de comandos**vertex()**.  Para se parar o desenho da forma, chama-se**endShape()**. Enguanto a função**vertex()**
 com dois parâmetros especifica uma posição em
2D, uma com tr6es parâmetros  especifica uma
posição em 3D. Cada forma será delineada com a cor
do traço corrente e preenchida com  a atual cor de
preenchimento.   Transformações geométricas
como**translate()**,**rotate()**, e**scale() **não funcionam no escopo de**beginShape()**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
beginShape(<font color="#996600">MODE</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODE
qualquer um
entre: LINES, LINE_STRIP, LINE_LOOP, TRIANGLES, TRIANGLE_FAN,
TRIANGLE_STRIP, QUADS, QUAD_STRIP, ou  POLYGON
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[endShape()](endShape_)[vertex()](vertex_)[curveVertex()](curveVertex_)[bezierVertex()](bezierVertex_)
