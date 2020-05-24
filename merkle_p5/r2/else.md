<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### else
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Estende a estrutura de controle**if()**,
permitindo a execução do programa escolher entre dois ou
mais blocos de código.  Especifica um bloco de
código a ser executado nos casos em que a expressão no**if()** for falsa.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
if(<font color="#996600">expressão</font>) { 
  <font color="#996600">comandos</font> 
} else { 
  <font color="#996600">comandos</font> 
} 

if(<font color="#996600">expressão</font>) { 
  <font color="#996600">comandos</font> 
} else if(<font color="#996600">expressão</font>) { 
  <font color="#996600">comandos</font> 
} else { 
  <font color="#996600">comandos</font> 
}

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
expressão
qualquer expressão que possa ser avaliada como verdadeira ou falsa
comandos
um ou mais comandos a executar
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[if()](if_)
