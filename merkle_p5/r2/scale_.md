
#### Nome
### scale()

#### Exemplos
<img border="0" height="100" src="media/scale_.gif" width="100"/>

```pde
rect(30, 20, 50, 50); 
scale(0.5); 
rect(30, 20, 50, 50); 

```
<img border="0" height="100" src="media/scale_2.gif" width="100"/>

```pde
rect(30, 20, 50, 50); 
scale(0.5, 1.3); 
rect(30, 20, 50, 50); 

```
<img border="0" height="100" src="media/scale_3.gif" width="100"/>

```pde
// Scaling in 3D requires P3D 
// or OPENGL as a parameter to size() 
size(100, 100, P3D); 
fill(255, 102); 
translate(width/2+12, height/2); 
box(20, 20, 20); 
scale(2.5, 2.5, 2.5); 
box(20, 20, 20); 

```

#### Descrição
Incrementar ou decrementar o tamanho de um objeto
ao expandir ou contrair vértices. Valores de escala são
especificados em percentagens decimais. A chamada de
função `scale(2.0)` incrementa a dimensão de uma forma em 200%. Objetos sempre são translacionados em relação a sua
posição relativa à
origem do sistema de coordenadas.  Transformações se aplicam a
todos eventos que aconteçam após
sua chamada, e chamadas subseqüentes multiplicam seu efeito.  Por exemplo, ao se chamar `scale(2.0) ` e em seguida ` scale(1.5) `equivale a se chamar `scale(2.5)`. Quando ` scale` `() `é chamada dentro de `draw()`,
a transformação é reinicializada ao começo
do novo laço.  A utilização desta função com o parâmetro `z ` requer a passagem
de P3D ou OPENGL como parâmetro à função
size(),  como mostrado no exemplo acima.

#### Sintaxe
```pde
scale(taxa);
scale(x, y);
scale(x, y, z);

```
Parâmetros
size
float: razão a se escalar um objeto


x
float: razão a escalar um objeto no eixo "x"


y
float: razão a escala um objeto no eixo "y"


z
float: razão a escalar um objeto no eixo "z"



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[translate()](translate_
)
[rotate()](rotate_
)
[rotateX()](rotateX_
)
[rotateY()](rotateY_
)
[rotateZ(](rotateZ_
)
[pushMatrix()](pushMatrix_
)
[popMatrix()](popMatrix_
)

