<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### expand()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int[] ia = {0, 1, 3, 4}; 
println(ia.length);  // Prints "4" 
ia = expand(ia); 
println(ia.length);  // Prints "8" 
ia = expand(ia, 512); 
println(ia.length);  // Prints "512" 

```

#### Descrição
Incrementa o tamanho de um array. Como
padrão, esta função duplica o tamanho do array,
mas através do parâmetro opcional**novoTam** tem-se controle preciso sobre este incremento em tamanho.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
expand(<font color="#996600">array</font>)
expand(<font color="#996600">array</font>, <font color="#996600">novoTam</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
array
boolean[], byte[], char[], int[], float[], ou String[]
novoTam
int positivo: novo tamanho do array
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Array (do mesmo tipo de dados da entrada)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[contract()](contract_)
