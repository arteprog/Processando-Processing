
#### Nome
### Array

#### Exemplos

```pde
int[] numeros = new int[3]; 
numeros[0] = 90; 
numeros[1] = 150; 
numeros[2] = 30; 
int a = numeros[0] + numeros[1]; // Atribui a variável "a" o valor 240 
int b = numeros[1] + numeros[2]; // Atribui a variável "a" o valor 180 
```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
int[] numeros = { 90, 150, 30 }; 
int a = numeros[0] + numeros[1]; // Atribui a variável "a" o valor 240 
int b = numeros[1] + numeros[2]; // Atribui a variável "a" o valor 180 
```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
int graus = 360; 
float[] cos_vals = new float[graus]; 
for(int i=0; i < graus; i++) { 
  cos_vals[i] = cos(TWO_PI/graus * i); 
} 

```

#### Descrição
Uma*array *é uma lista de dados (n.t um agregado homogêneo de dados) . São possíveis*arrays * de quaisquer tipos de dados. Cada ítem de dados no*array*
é identificado por um índice numérico que
representa sua respectiva posição.  O primeiro
elemento  é identificado pelo índice**[0]**,  o segundo pelo índice**[1]**,
e assim consecutivamente. Arrays são similares a objetos,
conseqüentemente devem ser criados através da palavra chave**new.** Cada*array* tem uma variável**lengh**, a qual armazena um valor inteiro que indica sua quantidade total de elementos.

#### Sintaxe
```pde
datatype[] var
var[elemento] = valor
var.length

```
Parâmetros
datatype
qualquer tipo de dados primitivo ou composto, incluindo classes definidas pelos usuários
var
qualquer nome válido de variável
elemento
int: não deve exceder o tamaho do array decrescido de 1 (var.length -1)
valor
dado a ser atribuído ao elemento do array, que deve ser de tipo igual do do array.
var.lenght
tamanho ou cardinalidade do array "var". É definido  no momento de sua declaração.

#### Utilização

	
Web & Applicações
