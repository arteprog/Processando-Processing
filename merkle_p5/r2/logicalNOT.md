
#### Nome
### ! (operador lógico NÃO)

#### Exemplos
<img border="0" height="100" src="media/logicalNOT.gif" width="100"/>

```pde
boolean a = false; 
if (!a) { 
  rect(30, 20, 50, 50); 
} 
a = true; 
if (a) { 
  line(20, 10, 90, 80); 
  line(20, 80, 90, 10); 
} 

```

#### Descrição
Inverte o valor Booleano de uma expressão.  Retorna verdadeiro ( `true`) ` ` se a expressão é falsa ( `false`) e retorna falso ( `false`) se a expressão é verdadeira ( `true`).  No caso da expressão **(a>b)** ser avaliada como verdadeira , então **!(a>b)** será avaliada como falsa.

#### Sintaxe
```pde
!expressão
            
```
Parâmetros
expressão
qualquer expressão válida



#### Utilização

	
Web & Applicações

#### Relacionado
[|| (lógico OU)](logicalOR
)
[&& (lógico E)](
)
[if()](if_
)

