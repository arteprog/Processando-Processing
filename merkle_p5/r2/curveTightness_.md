
#### Nome
### curveTightness()

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

#### Descrição
Modivida a qualidade das curvas criadas com<span style="font-weight: bold;">curve `()` </span> e `curveVertex()`.  O parâmetro `squishy `define como a curva se ajusta aos pontos que são vértices.  O valor 0.o é o valor padrão de `squishy `(este
parâmetro defina as curvas como sendo Catmul-Rom splines) e o
calor 1.0 conecta todos os pontos com linhas retas. Valores no
intervalo de -5.0 a +5.0 deformarão a curva  mas a
deixarão reconhecível, e na medida que os valore
creçam em magnitude, a deformação será
continuada.

#### Sintaxe
```pde
curveTightness(squishy)

```
Parâmetros
squishy
float ou int: quantidade de deformacão relativa aos vértices originais.



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[curve()](curve_
)
[curveVertex()](curveVertex_
)

