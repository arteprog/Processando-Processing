<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### rotateY()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/rotateY_.gif" width="100"/>

```pde
size(100, 100, P3D); 
translate(width/2, height/2); 
rotateY(PI/3.0); 
rect(-26, -26, 52, 52); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/rotateY_.gif" width="100"/>

```pde
size(100, 100, P3D); 
translate(width/2, height/2); 
rotateY(radians(60)); 
rect(-26, -26, 52, 52); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Rotaciona um objeto em torno do eixo Y em uma quatidade especificada pelo parâmetro**angulo**.
 Ângulos devem ser especificados em radianos (valores entre
0 e 2*PI) ou antes convertidos para radianos pela função**radians()**.
Objetos sempre são rotacionados em torno de sua posição relativa à
origem, e números positivos rotacionam objetos em sentido anti-horário.
 Transformações se aplicam a todos eventos que aconteçam após
sua chamada, e chamadas subseqüentes a transformações têm efeito
cumulativo. Por exemplo, ao se chamar**rotateY(PI/2) ** e em seguida** rotateX (PI/2) **equivale a se chamar**rotateX(PI)**. Quando** ****rotate() **é chamada dentro de**draw()**,
a transformação é reinicializada ao começo do novo laço.  Esta função
requer a passagem de P3D ou OPENGL como parâmetro à função size() como
mostrado no exemplo acima.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
rotateY(<font color="#996600">angulo</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
angulo
float: ângulo de rotação especificado em radianos
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[rotateX() ](rotateX_)[rotateZ() ](rotateZ_)[translate() ](translate_)[rotate() ](rotate_)[scale() ](scale_)[pushMatrix() ](pushMatrix_)[popMatrix() ](popMatrix_)
