<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### curveTightness()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/curveTightness_.gif" width="100"/>

```pde
// White curve 
stroke(255); 
beginShape(LINE_STRIP); 
curveVertex(10, 26); 
curveVertex(10, 26); 
curveVertex(83, 24); 
curveVertex(83, 61); 
curveVertex(25, 65); 
curveVertex(25, 65); 
endShape(); 
 
// Gray curve 
stroke(126); 
curveTightness(3.5); 
beginShape(LINE_STRIP); 
curveVertex(10, 26); 
curveVertex(10, 26); 
curveVertex(83, 24); 
curveVertex(83, 61); 
curveVertex(25, 65); 
curveVertex(25, 65); 
endShape(); 
 
// Black curve 
stroke(0); 
curveTightness(-2.5); 
beginShape(LINE_STRIP); 
curveVertex(10, 26); 
curveVertex(10, 26); 
curveVertex(83, 24); 
curveVertex(83, 61); 
curveVertex(25, 65); 
curveVertex(25, 65); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Modivida a qualidade das curvas criadas com<span style="font-weight: bold;">curve**()**</span> e**curveVertex()**.  O parâmetro**squishy **define como a curva se ajusta aos pontos que são vértices.  O valor 0.o é o valor padrão de**squishy **(este
parâmetro defina as curvas como sendo Catmul-Rom splines) e o
calor 1.0 conecta todos os pontos com linhas retas. Valores no
intervalo de -5.0 a +5.0 deformarão a curva  mas a
deixarão reconhecível, e na medida que os valore
creçam em magnitude, a deformação será
continuada.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
curveTightness(<font color="#996600">squishy</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
squishy
float ou int: quantidade de deformacão relativa aos vértices originais.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)
