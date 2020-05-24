<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### switch()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int num = 1; 
 
switch(num) { 
  case 0: 
    println("Zero");  // Não é executado
    break; 
  case 1: 
    println("Um");  // Imprime "Um" 
    break; 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
char letter = 'N'; 
 
switch(letter) { 
  case 'A': 
    println("Alpha");  // Não é executado
    break; 
  case 'B': 
    println("Bravo");  // Não é executado 
    break; 
  default:             // É executado caso os rótulos ou casos
    println("Nenhum");   // não beterem com o parâmentro do switch
    break; 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
// A remoção de um "break" permite testar por mais  
// de um valor em um único momento
 
char letra = 'b'; 
 
switch(letra) { 
  case 'a': 
  case 'A': 
    println("Alpha");  // Não executa 
    break; 
  case 'b': 
  case 'B': 
    println("Bravo");  // Imprime "Bravo" 
    break; 
} 

```

#### Descrição
Funciona como uma estrutura de controle condicional**if else**, mas o**swith()**
é mais conveniente quando se tem a necessidade de
seleção de três ou mais alternatias.  A
execução do programa segue ao ponto onde o caso  (*case*)
tem valor equivalente à expressão de controle. Todos os
demais comandos no switch são executados exceto quando a
execução for redirecionalda por um comando**break.**
Apenas dados primitivos que podem ser convertidos para um inteiro
(byte, char, and int) podem ser utilizados com parâmetro**expressão. ** O caso padrão (*default*) é opcional.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
switch(<font color="#996600">expressão</font>)
{
  case<font color="#996600"> rotulo</font>: 
     <font color="#996600">statements</font>          
  case <font color="#996600">rotulo</font>:        // Optional
     <font color="#996600">statements</font>        // "
  default:             // "
     <font color="#996600">statements</font>        // "
}

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
expressão
byte, char, or int
rotulo
byte, char, or int
comandos
um ou mais comando a executar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[case](case)[default](default)[break](break)[if()](if_)[else](else)
