
#### Nome
### hex()

#### Exemplos

```pde
color c = #ffcc00; 
println(c);          // Imprime -13312 
println(hex(c));     // Imprime FFFFCC00 
println(hex(c, 6));  // Imprime FFCC00 

```



```pde
color c = color(255, 204, 0); 
println(c);          // Imprime -13312 
println(hex(c));     // Imprime FFFFCC00 
println(hex(c, 6));  // Imprime FFCC00 

```



#### Descrição
Converte um byte, char, int, ou color em
uma String contendo o equivalente em sua
representação hexadecimal. Por exemplo 
color(0, 102, 153, 255)
será convertico na String "FF006699". Esta
função pode ajudar as sessões de
depuração mais felizes.

#### Sintaxe
```pde
hex(valor)
hex(valor, digitos)

```
Parâmetros
valor
byte, char, int, color: value to convert


digitos
int: number of digits to return



#### Retorno

	
String

#### Utilização

	
Web & Applicações

#### Relacionado
[unhex()](unhex_
)
[binary()](binary_
)
[unbinary()](unbinary_
)

