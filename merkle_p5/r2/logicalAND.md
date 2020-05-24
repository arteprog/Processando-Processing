<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### && (logical AND)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/logicalAND.gif" width="100"/>

```pde
for(int i=5; i<=95; i+=5) { 
  if((i > 35) && (i < 60)) { 
    stroke(0);    //Atribui a variável color a cor preta
  } else { 
    stroke(255);  //Atribui a variável color a cor branca
  } 
  line(30, i, 80, i); 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Compara duas expressões e retorna verdadeiro (**true**) se ambas forem avaliadas como verdadeiras (**true**). Retorna false (**false**) se uma ou ambas forem avaliadas como falsas (**false**). A seguinte linstas mostra todas as possíveis combinações<tt>true &amp;&amp; false    // É avaliada como falsa porquê a segunda é falsa

false &amp;&amp; true    // É avaliada como falsa porquê a primeira é falsa

true &amp;&amp; true   // É avaliada como verdadeira porquê ambas são verdadeiras

false &amp;&amp; false  // É avaliada como falsa porquê ambas são falsas</tt>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
<font color="#996600">expressão1</font> && <font color="#996600">expressão2</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
expressão1
qualquer expressão válida
expressão2
qualquer expressão válida
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[|| (lógico OU)](logicalOR)[! (lógico NÃO)](logicalNOT)[if()](if_)
