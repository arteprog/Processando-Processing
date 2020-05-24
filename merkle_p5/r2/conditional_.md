<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ?: (condicional)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int s = 0; 
for(int i=5; i<100; i+=5) { 
  s = (i < 50) ? 0 : 255; 
  stroke(s); 
  line(30, i, 80, i); 
} 

```

#### Descrição
Uma abreviação para se escrever uma estrutura de controle**se() **e**senão **(**if()** e**else**). Se a condição for avaliada como verdadeira (**true**) , a**expressão1 ** é valiada e retornada. Se a condição for avaliada como falsa (**false**) , a**expressão2 ** é valiada e retornada.
A seguinte estrutura conticional :```pde
condição : expressão1 ? expressão2
```
is equivalent to this structure:```pde
if(condição) {
  expressão1 
} else { 
  expressão2 
}
```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
<font color="#996600">condição</font> ? <font color="#996600">expressão1</font> : <font color="#996600">expressão2</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
condição
qualquer expressão que possa ser avaliada como verdadeira ou falsa
expressão1
qualquer expressão válida
expressão2
qualquer expressão válida
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno
Variável, dependendo do tipo de dados das expressões
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[if()](if_)[else](else)
