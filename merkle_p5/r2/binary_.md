
#### Nome
### binary()

#### Exemplos

```pde
color c = color(255, 204, 0); 
println(c);             // Prints -13312 
println(binary(c));     // Prints 11111111111111111100110000000000 
println(binary(c, 16)); // Prints 1100110000000000 
 

```

#### Descrição
Converte um byte, char, int, ou color em uma
String contendo o equivalente en notação binária.
Por exemplo, color(0, 102, 153, 255) será convertida para a
String  "11111111000000000110011010011001". Esta
função pode ajudar as sessões de
depuração mais felizes.

#### Sintaxe
```pde
binary(valor)
binary(valor, digitos)

```
Parâmetros
valor
byte, char, int, color: value à converter
digitos
int: número de dígitos a retornar

#### Retorno

	
String

#### Utilização

	
Web & Applicações

#### Relacionado
[unhex()](unhex_)[hex()](hex_)[unbinary()](unbinary_)
