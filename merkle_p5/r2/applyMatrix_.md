<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### applyMatrix()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/applyMatrix_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
translate(50, 50, 0); 
rotateY(PI/6); 
stroke(153); 
box(35); 
// Determina ângulo de rotação
float ct = cos(PI/9.0); 
float st = sin(PI/9.0);          
//Matriz de rotação em torno do eixo Y
applyMatrix(  ct, 0.0,  st,  0.0, 
             0.0, 1.0, 0.0,  0.0, 
             -st, 0.0,  ct,  0.0, 
             0.0, 0.0, 0.0,  1.0);  
stroke(255); 
box(50); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Multiplica a matriz corrente por aquela
especificada pelos parâmetros. Isto é bastante lento
porque tentará tentar calculara o inverso da
transformação. Portanto, a evite sempre que
possível. A função equivalente em OpenGL é
glMultMatrix().
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
applyMatrix(n00, n01, n02, n03
            n04, n05, n06, n07
            n08, n09, n10, n11
            n12, n13, n14, n15)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
n00-n15
float: números que definem a matriz 4x4 a ser multiplicada
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[pushMatrix()](pushMatrix_)[popMatrix()](popMatrix_)[resetMatrix()](resetMatrix_)[printMatrix()](printMatrix_)
