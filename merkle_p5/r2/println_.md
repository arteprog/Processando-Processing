<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### println()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
println("begin"); 
float f = 0.3; 
println("f é igual à " + f + " e i é igual à " + 1024); 
String s = "end"; 
println(s); 
 
//O código acima imprime as seguintes linhas:
// begin 
// f é igual à 0.3 e d i é igual à 1024 
// end 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
float[] f = { 0.3, 0.4, 0.5 }; 
println(f); 
 
// O código acima imprime:
// 0.3 
// 0.4 
// 0.5 

```

#### Descrição
Escreve na área do console do ambiente
Processing. Frequentemente, isto é de ajuda para se 
visualizar  os dados que um programa está produzindo. Cada
chamada cria um nova linha de saída.  Elementos
individuais pode ser separados por aspas ("") e  agregados pelo
operador de adição (+).  Ela também escreve o
conteúdo de um array na área de texto do  console do
ambiete Processing. Isto é de ajuda para se  visualizar
 os dados que um programa está produzindo. Uma nova linha
 iniciada para cada elemento do array. Esta
função só pode imprimeir arraus 1D, mas pode
testar se o conteúdo de uma array de mais de duas
dimensões é nulo ou não nulo.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
println(<font color="#996600">dado</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
dado
boolean, byte, char, color, int, float, ou String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
IDE
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[print()](print_)
