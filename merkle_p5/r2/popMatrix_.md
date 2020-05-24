
#### Nome
### popMatrix()

#### Exemplos
<img border="0" height="100" src="media/pop_.gif" width="100"/>

```pde
rect(0, 0, 50, 50);   //Retângulo branco
pushMatrix(); 
translate(30, 20); 
fill(0);  
rect(0, 0, 50, 50);   //Retângulo preto
popMatrix(); 
fill(102);  
rect(15, 10, 50, 50); // Retângulo cinza

```

#### Descrição
Retira (n.t.*pop*)* *a matriz corrente do topo da piha de matrixes de transformações geométricas.
O entendimento de insersões(n.t.*push*)  e retiradas (n.t.* pop*) requer a comprenção co conceito de pilha de matriz de transgomação.  A função**pushmatrix()** salva o sistema de coordenada corrente nesta pilha e a função**popMatrix()** restaura o sistema de coordenadas prévio.  As funções**pushMatrix()** e** popMatrix() ** sao
utilizadas em conjuto com outros métodos de
transformação  e podem ser incorporadas ao controle
do escopo das transformações.

#### Sintaxe
```pde
popMatrix()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[pushMatrix()](pushMatrix_)
