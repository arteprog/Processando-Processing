
#### Nome
### curveDetail()

#### Exemplos
<img border="0" height="100" src="media/curveDetail_.gif" width="100"/>

```pde
void setup() { 
 size(100, 100, P3D); 
 noLoop(); 
} 
 
void draw() { 
 curveDetail(1); 
 drawCurves(-15); 
 stroke(126); 
 curveDetail(2); 
 drawCurves(0); 
 stroke(255); 
 curveDetail(4); 
 drawCurves(15); 
} 
 
void drawCurves(float y) { 
 curve( 5, 28+y, 5, 28+y, 73, 26+y, 73, 63+y); 
 curve( 5, 28+y, 73, 26+y, 73, 63+y, 15, 67+y); 
 curve(73, 26+y, 73, 63+y, 15, 67+y, 15, 67+y); 
} 
 

```

#### Descrição
Especifica a
resolução na qual uma curva será
visualizada. O valor padrão é 20. Esta
função é util apenas quando o renderer de P3D ou
OPENGL como padrão, pois o visualizador padrão (JAVA2D)
não utiliza esta informação.

#### Sintaxe
```pde
curveDetail(detalhe)

```
Parâmetros
detalhe
int:
resolução da curva

#### Retorno
 Nenhum

#### Utilização
 Web &
Applicações

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)[curveTightness()](curveTightness_)
