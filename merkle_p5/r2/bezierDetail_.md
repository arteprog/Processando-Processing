
#### Nome
### bezierDetail()

#### Exemplos
<img border="0" height="100" src="media/bezierDetail_.gif" width="100"/>

```pde
void setup() { 
  size(100, 100, P3D); 
  noLoop(); 
} 
 
void draw() { 
  bezierDetail(1); 
  bezier(85, 20, 10, 10, 90, 90, 15, 80); 
  stroke(126); 
  bezierDetail(3); 
  bezier(85, 20, 10, 10, 90, 90, 15, 80); 
  stroke(255); 
  bezierDetail(12); 
  bezier(85, 20, 10, 10, 90, 90, 15, 80); 
} 
 

```

#### Descrição
Especificam a resolução na qual as
curvas de Bezier são visualizadas. O valor padrão
é 20.  Esta função é util apenas
quando o renderer de P3D ou OPENGL  como padrão, pois o
visualizador padrão (JAVA2D) não utiliza esta
informação.

#### Sintaxe
```pde
bezierDetail(detalhe)

```
Parâmetros
detalhe
int: resolução das curvas

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[curve()](curve_)[curveVertex()](curveVertex_)[curveTightness()](curveTightness_)
