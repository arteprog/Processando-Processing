
#### Nome
### resetMatrix()

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

#### Descrição
Substitui a matrix corrente pela matriz identidade. A função equivalente em OpenGL é glLoadIdentity().

#### Sintaxe
```pde
resetMatrix()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[pushMatrix()](pushMatrix_)[popMatrix()](popMatrix_)[applyMatrix()](applyMatrix_)[printMatrix()](printMatrix_)
