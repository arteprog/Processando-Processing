<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### hex()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
color c = #ffcc00; 
println(c);          // Imprime -13312 
println(hex(c));     // Imprime FFFFCC00 
println(hex(c, 6));  // Imprime FFCC00 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
hex(<font color="#996600">valor</font>)
hex(<font color="#996600">valor</font>, <font color="#996600">digitos</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor
byte, char, int, color: value to convert
digitos
int: number of digits to return
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[unhex()](unhex_)[binary()](binary_)[unbinary()](unbinary_)
