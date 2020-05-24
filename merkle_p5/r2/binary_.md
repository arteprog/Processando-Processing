<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### binary()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
binary(<font color="#996600">valor</font>)
binary(<font color="#996600">valor</font>, <font color="#996600">digitos</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor
byte, char, int, color: value à converter
digitos
int: número de dígitos a retornar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[unhex()](unhex_)[hex()](hex_)[unbinary()](unbinary_)
