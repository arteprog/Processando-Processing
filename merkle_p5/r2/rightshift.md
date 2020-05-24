
#### Nome
### >> (deslocamento à direita)

#### Exemplos

```pde
int m = 8 >> 3;    // Em binário: 1000 to 1 
println(m);  // Imprime "1" 
int n = 256 >> 6;  // Em binário: 100000000 to 100 
println(n);  // Imprime "4" 
int o = 16 >> 3;   // Em binário: 10000 to 10 
println(o);  // Imprime "2" 
int p = 26 >> 1;   // Em binário: 11010 to 1101 
println(p);  // Imprime "13" 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
color argb = color(204, 204, 51, 255); 
int a = argb >> 24 & 0xFF; 
int r = argb >> 16 & 0xFF;  // Maneira mais rápida de se obter red(argb) 
int g = argb >> 8 & 0xFF;   // Maneira mais rápida de se obter green(argb) 
int b = argb & 0xFF;        // Maneira mais rápida de se obter blue(argb) 
fill(r, g, b, a); 
rect(30, 20, 55, 55); 

```

#### Descrição

Desloca bits à direira. O número à esquerda do operador é deslocado na
quantidade de bits especificada pelo número à direita.  Cada
deslocamento divide por dois o valor do número. Conseqüentemente, cada
deslocamento divide o valor original por dois.  Utilizar o
deslocamento à direita para divisões rápidas, ou para extrair um número individual de um
grupo de números. O deslocamento à direita trabalha
apenas com números inteiros, ou os números serão primeiramente
convertidos para inteiro, como um byte ou char.

#### Sintaxe
```pde
valor >> n
            
```
Parâmetros
valor
int: o valor a deslocar
n
int: o número de lugares a deslocar à direita

#### Utilização

	
Web & Applicações

#### Relacionado
[<< (deslocamento à esquerda)](leftshift)
