<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### | (bitwise OR)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int a = 205;   // In Binário: 11001101 
int b = 45;    // In Binário: 00101101 
int c = a | b; // In Binário: 11101101 
println(c);    // Imprime "237", o equivalente decimal de 11101101 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
int a = 255 << 24;   // Binário: 11111111000000000000000000000000 
int r = 204 << 16;   // Binário: 00000000110011000000000000000000 
int g = 204 << 8;    // Binário  00000000000000001100110000000000 
int b = 51;          // Binário: 00000000000000000000000000110011 
// OU de bit de todos os valores:11111111110011001100110000110011 
color argb = a | r | g | b; 
fill(argb); 
rect(30, 20, 55, 55); 

```

#### Descrição
Compara cada bit da representação
binária de dois números. Para cada
comparação, dois 1s  resulta em 1,  um 1 e um 0
resulta em 1, e dois 0 resulta em 0. É mais fácil de ver o
reusltado quando se visualiza a representação
binária dos números.```pde
  11010110  // 214
& 01011100  // 92
  --------
  11011110  // 222
```

            Para se ver a representação binária de um número, utilizar a função**Binário()** em conjunto com**println()**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
<font color="#996600">valor</font> | <font color="#996600">valor2</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor1
int, char, byte
valor2
int, char, byte
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[& (bitwise AND)](bitwiseAND)[Binário()](binary_)
