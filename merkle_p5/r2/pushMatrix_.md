
#### Nome
### pushMatrix()

#### Exemplos
<img border="0" height="100" src="media/pushMatrix_.gif" width="100"/>

```pde
rect(0, 0, 50, 50);   //Retângulo branco
pushMatrix(); 
translate(30, 20); 
fill(0);  
rect(0, 0, 50, 50);   //Retângulo preto
popMatrix(); 
fill(102);  
rect(15, 10, 50, 50); //Retângulo cinza

```

#### Descrição

	
Insere (n.t.*push*)* *a
matriz corrente no topo da piha de matrixes de
transformações geométricas. O entendimento de
insersões(n.t.*push*)  e retiradas (n.t.* pop*) requer a comprenção co conceito de pilha de matriz de transgomação.  A função**pushmatrix()** salva o sistema de coordenada corrente nesta pilha e a função**popMatrix()** restaura o sistema de coordenadas prévio.  As funções**pushMatrix()** e** popMatrix() ** sao
utilizadas em conjuto com outros métodos de
transformação  e podem ser incorporadas ao controle
do escopo das transformações.

#### Sintaxe
```pde
pushMatrix()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[popMatrix()](popMatrix_)[translate()](translate_)[rotate()](rotate_)[rotateX() ](rotateX_)[rotateY() ](rotateY_)[rotateZ() ](rotateZ_)
