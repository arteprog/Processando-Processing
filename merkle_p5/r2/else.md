
#### Nome
### else

#### Exemplos
<img border="0" height="100" src="media/else.gif" width="100"/>

```pde
for(int i = 5; i < 95; i += 5) { 
  if(i < 35) { 
    line( 30, i, 80, i ); 
  } else { 
    line( 20, i, 90, i ); 
  } 
} 

```
<img border="0" height="100" src="media/else2.gif" width="100"/>

```pde
for(int i = 5; i < 95; i += 5) { 
  if(i < 35) { 
    line( 30, i, 80, i ); 
  } else if (i < 65) { 
    line( 20, i, 90, i ); 
  } else { 
    line( 0, i, 100, i ); 
  } 
} 

```

#### Descrição
Estende a estrutura de controle**if()**,
permitindo a execução do programa escolher entre dois ou
mais blocos de código.  Especifica um bloco de
código a ser executado nos casos em que a expressão no**if()** for falsa.

#### Sintaxe
```pde
if(expressão) { 
  comandos 
} else { 
  comandos 
} 

if(expressão) { 
  comandos 
} else if(expressão) { 
  comandos 
} else { 
  comandos 
}

```
Parâmetros
expressão
qualquer expressão que possa ser avaliada como verdadeira ou falsa
comandos
um ou mais comandos a executar

#### Utilização

	
Web & Applicações

#### Relacionado
[if()](if_)
