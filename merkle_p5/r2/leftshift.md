
#### Nome
### << (deslocamento à esquerda)

#### Exemplos

```pde
int m = 1 << 3;   // Em binário: 1 à 1000 
println(m);  // Imprime "8" 
int n = 1 << 8;   // Em binário: 1 à 100000000 
println(n);  // Imprime "256" 
int o = 2 << 3;   // Em binário: 10 à 10000 
println(o);  // Imprime "16" 
int p = 13 << 1;  // Em binário: 1101 à 11010 
println(p);  // Imprime "26" 

```



```pde
// Empacota quatro números de 8 bits em um de 32 bits
int a = 255;  // Binário: 00000000000000000000000011111111 
int r = 204;  // Binário: 00000000000000000000000011001100 
int g = 204;  // Binário: 00000000000000000000000011001100 
int b = 51;   // Binário: 00000000000000000000000000110011 
a = a << 24;  // Binário: 11111111000000000000000000000000 
r = r << 16;  // Binário: 00000000110011000000000000000000 
g = g << 8;   // Binário: 00000000000000001100110000000000 
 
// Equivale a operação "color argb = color(r, g, b, a)", mas mais rápida
color argb = a | r | g | b; 
fill(argb); 
rect(30, 20, 55, 55); 

```



#### Descrição
Desloca bits à esquerda. O número
à esquerda do operador é deslocado na quantidade de bits
especificada pelo número à direira.  Cada
deslocamento duplica o valor do número. Conseqüentemente,
cada deslocamento multiplica o valor original por dois.  Utilizar
o deslocamento à esquerda para multiplicações
rápidas, ou para agregar um grupo de números em um
número maior. O deslocamento à esquerda trabalha apenas
com números inteiros, ou os números serão
primeiramente convertidos para inteiro, como um byte ou char.

#### Sintaxe
```pde
valor << n
            
```
Parâmetros
valor
int: o número a deslocar


n
int: o número de lugares a deslocar à esquerda



#### Utilização

	
Web & Applicações

#### Relacionado
[>> (deslocamento à direita)](rightshift
)

