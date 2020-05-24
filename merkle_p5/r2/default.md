
#### Nome
### default

#### Exemplos

```pde
char letra = 'F'; 
 
switch(letter) { 
  case 'A': 
    println("Alpha");  // Não é executado 
    break; 
  case 'B': 
    println("Bravo");  // Não é executado 
    break; 
  default: 
    println("Zulu");   // Imprime "Zulu" 
    break; 
} 

```

#### Descrição
Palavara chave que define a condição assumida como padrão de um**switch()**. Caso nenhum dos parâmetros coincidir com o parâmetro do**switch()**, o(s) comando(s) após o rótulo**default**  são executados. Estruturas de controle swith() não requerem a presença de**default.**

#### Sintaxe
```pde
default: comandos
            
```
Parâmetros
comandos
um ou mais comandos a serem executados

#### Utilização

	
Web & Applicações

#### Relacionado
[switch()](switch_)[break](break)[case](case)
