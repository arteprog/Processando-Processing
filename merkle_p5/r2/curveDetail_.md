<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### curveDetail()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Especifica a
resolução na qual uma curva será
visualizada. O valor padrão é 20. Esta
função é util apenas quando o renderer de P3D ou
OPENGL como padrão, pois o visualizador padrão (JAVA2D)
não utiliza esta informação.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
curveDetail(<font color="#996600">detalhe</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
detalhe
int:
resolução da curva
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno
 Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização
 Web &
Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)[curveTightness()](curveTightness_)
