
#### Nome
### rotate()

#### Exemplos
<img border="0" height="100" src="media/rotate_.gif" width="100"/>

```pde
translate(width/2, height/2); 
rotate(PI/3.0); 
rect(-26, -26, 52, 52); 

```

#### Descrição
Rotaciona um objeto em  uma qunatidade especificada pelo parâmetro**angulo**.
 Ângulos devem ser especificados em radianos (valores entre
0 e 2*PI) ou antes convertidos para radianos pela função**radians()**.
Objetos sempre são rotacionados em torno de sua
posição relativa à origem, e números
positivos rotacionam objetos em direção contra o
relógio.  Transformações se aplicam a todos
eventos que aconteçam após sua chamada, e chamadas
subseqüentes a transformações têm efeito
cumulativo. Por exemplo, ao se chamar**rotate(PI/2) ** e em seguida** rotate (PI/2) **equivale a se chamar**rotate(PI)**. Quando** ****rotate() ** é chamada dentro de**draw()**, a transformação é reinicializada ao começo do novo laço. Tecnicamente,**rotate()** multiplica a matrz de transformação corrente por uma matriz de rotação.

#### Sintaxe
```pde
rotate(angulo); 

```
Parâmetros
angulo
float: ângulo de rotação em radianos

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[rotateX() ](rotateX_)[rotateY() ](rotateY_)[rotateZ() ](rotateZ_)[translate() ](translate_)[scale() ](scale_)[pushMatrix() ](pushMatrix_)[popMatrix() ](popMatrix_)
