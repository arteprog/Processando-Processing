<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### resetMatrix()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/resetMatrix_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
box(80); 
printMatrix(); 
// Imprime: 
// 01.0000  00.0000  00.0000 -50.0000 
// 00.0000  01.0000  00.0000 -50.0000 
// 00.0000  00.0000  01.0000 -86.6025 
// 00.0000  00.0000  00.0000  01.0000 
 
resetMatrix(); 
box(80); 
printMatrix(); 
// Imprime: 
// 1.0000  0.0000  0.0000  0.0000 
// 0.0000  1.0000  0.0000  0.0000 
// 0.0000  0.0000  1.0000  0.0000 
// 0.0000  0.0000  0.0000  1.0000 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Substitui a matrix corrente pela matriz identidade. A função equivalente em OpenGL é glLoadIdentity().
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
resetMatrix()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[pushMatrix()](pushMatrix_)[popMatrix()](popMatrix_)[applyMatrix()](applyMatrix_)[printMatrix()](printMatrix_)
