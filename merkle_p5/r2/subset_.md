<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### subset()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
String sa1[] = { "OH ", "NY ", "CA ", "VA ", "CO ", "IL "}; 
String sa2[] = subset(sa1, 1); 
print(sa2);  // Prints "NY CA VA CO IL " 
println(); 
String sa3[] = subset(sa1, 2, 3); 
print(sa3);  // Prints "CA VA CO " 

```

#### Descrição
Extrai um array de elementos de uma array existente. O parâmetro**array** define o array do qual os elementos serão copiandos, e os parâmetros**offset** e**lenght** determinan quais elementos a extrair. Caso**length  ** nao seja dado, os elementos extraídos irão de**offset** ao final do array. Ao se especificar o**offset**, lembrar que o primeiro elemento do array é o 0. Esta função não modifica o array fonte.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
subset(<font color="#996600">array</font>, <font color="#996600">offset</font>)
subset(<font color="#996600">array</font>, <font color="#996600">offset</font>, <font color="#996600">length</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
array
boolean[], byte[], char[], int[], float[], or String[]: array base
offset
int: posição para iniciar cópia
length
int: número de elementos as extrair
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Array (do mesmo tipo do array de entrada)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[splice()](splice_)
