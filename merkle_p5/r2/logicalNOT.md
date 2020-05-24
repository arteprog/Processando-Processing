<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ! (operador lógico NÃO)
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Inverte o valor Booleano de uma expressão.  Retorna verdadeiro (**true**)** ** se a expressão é falsa (**false**) e retorna falso (**false**) se a expressão é verdadeira (**true**).  No caso da expressão**(a>b)** ser avaliada como verdadeira , então**!(a>b)** será avaliada como falsa.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
!<font color="#996600">expressão</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
expressão
qualquer expressão válida
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[|| (lógico OU)](logicalOR)[&& (lógico E)]()[if()](if_)
