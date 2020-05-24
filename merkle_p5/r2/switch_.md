
#### Nome
### switch()

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
Funciona como uma estrutura de controle condicional `if else`, mas o `swith()`
é mais conveniente quando se tem a necessidade de
seleção de três ou mais alternatias.  A
execução do programa segue ao ponto onde o caso  ( *case*)
tem valor equivalente à expressão de controle. Todos os
demais comandos no switch são executados exceto quando a
execução for redirecionalda por um comando `break.`
Apenas dados primitivos que podem ser convertidos para um inteiro
(byte, char, and int) podem ser utilizados com parâmetro **expressão. ** O caso padrão ( *default*) é opcional.

#### Sintaxe
```pde
switch(expressão)
{
  case rotulo: 
     statements          
  case rotulo:        // Optional
     statements        // "
  default:             // "
     statements        // "
}

```
Parâmetros
expressão
byte, char, or int


rotulo
byte, char, or int


comandos
um ou mais comando a executar



#### Utilização

	
Web & Applicações

#### Relacionado
[case](case
)
[default](default
)
[break](break
)
[if()](if_
)
[else](else
)

