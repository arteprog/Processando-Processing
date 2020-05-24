
#### Nome
### & (binário E de bit)

#### Exemplos

```pde
int a = 207;   // Em binário: 11001111 
int b = 61;    // Em binário: 00111101 
int c = a & b; // Em binário: 00001101 
println(c);    // Imprime "13", O número decimal equivalente à 00001101 

```



```pde
color argb = color(204, 204, 51, 255); 
// Ao relizar a operação binária E de uma variável com 0xFF, 
// se comparam todos os bits dos dois valores, fazendo-os zeros, 
// com exceção dos últimos 8.
// "0xFF" é 00000000000000000000000011111111 
int a = argb >> 24 & 0xFF; 
int r = argb >> 16 & 0xFF; 
int g = argb >> 8 & 0xFF; 
int b = argb & 0xFF;        
fill(r, g, b, a); 
rect(30, 20, 55, 55); 

```



#### Descrição
Compara cada bit da representação
binária de dois números. Para cada
comparação, dois 1  resulta em 1,  um 1 e um 0
resulta em 0, e dois 0 resulta em 0. É mais fácil de ver o
reusultado quando se visualiza a representação
binária dos números.

```pde
  11010110  // 214
& 01011100  // 92
  --------
  01010100  // 84
```



Para se ver a representação binária de um número, utilizar a função **binary()** em conjunto com **println()**.


#### Sintaxe
```pde
valor & valor2
            
```
Parâmetros
valor1
int, char, byte


valor2
int, char, byte



#### Utilização

	
Web & Applicações

#### Relacionado
[| (binário OU de bit)](bitwiseOR
)
[binary()](binary_
)

