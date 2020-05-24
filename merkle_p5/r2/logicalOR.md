
#### Nome
### || (logical OR)

#### Exemplos
<img border="0" height="100" src="media/logicalOR.gif" width="100"/>

```pde
for(int i=5 ; i<=95; i+=5) { 
  if((i < 35) || (i > 60)) { 
    line(30, i, 80, i); 
  } 
} 

```

#### Descrição
Compara duas expressões e retorna verdadeiro ( `true`) se uma ou ambas forem avaliadas como verdadeiras ( `true`). Retorna false ( `false`) se ambas forem avaliadas como falsas ( `false`). A seguinte linstas mostra todas as possíveis combinações

<tt>true &amp;&amp; false    // É avaliada como verdedeira porquê a primeira é verdadeira

false &amp;&amp; true    // É avaliada como verdadeira porquê a segunda é verdadeira

true &amp;&amp; true   // É avaliada como verdadeira porquê ambas são verdadeiras

false &amp;&amp; false  // É avaliada como falsa porquê ambas são falsas</tt>
<tt></tt>

#### Sintaxe
```pde
expressão1 || expressão
            
```
Parâmetros
expressão1
qualquer expressão válida


expressão2
qualquer expressão válida



#### Utilização

	
Web & Applicações

#### Relacionado
[&& (lógoco E)](
)
[! (lógico OU)](logicalNOT
)
[if()](if_
)

