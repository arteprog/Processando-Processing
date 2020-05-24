
#### Nome
### rotateZ()

#### Exemplos
<img border="0" height="100" src="media/rotateZ_.gif" width="100"/>

```pde
size(100, 100, P3D); 
translate(width/2, height/2); 
rotateZ(PI/3.0); 
rect(-26, -26, 52, 52); 

```
<img border="0" height="100" src="media/rotateZ_.gif" width="100"/>

```pde
size(100, 100, P3D); 
translate(width/2, height/2); 
rotateZ(radians(60)); 
rect(-26, -26, 52, 52); 

```

#### Descrição
Rotaciona um objeto em torno do eixo Z em uma quatidade especificada pelo parâmetro**angulo**.
 Ângulos devem ser especificados em radianos (valores entre
0 e 2*PI) ou antes convertidos para radianos pela função**radians()**.
Objetos sempre são rotacionados em torno de sua
posição relativa à
origem, e números positivos rotacionam objetos em sentido
anti-horário.  Transformações se aplicam a
todos eventos que aconteçam após
sua chamada, e chamadas subseqüentes a
transformações têm efeito
cumulativo. Por exemplo, ao se chamar**rotateZ(PI/2) ** e em seguida** rotateX (PI/2) **equivale a se chamar**rotateX(PI)**. Quando** ****rotate() **é chamada dentro de**draw()**,
a transformação é reinicializada ao começo
do novo laço.  Esta função requer a passagem
de P3D ou OPENGL como parâmetro à função
size() como mostrado no exemplo acima.

#### Sintaxe
```pde
rotateZ(angulo)

```
Parâmetros
angulo
float: ângulo de rotação especificado em radianos

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[rotateZ() ](rotateX_)[rotateY() ](rotateY_)[translate() ](translate_)[rotate() ](rotate_)[scale() ](scale_)[pushMatrix() ](pushMatrix_)[popMatrix() ](popMatrix_)
