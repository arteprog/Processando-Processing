<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### contract()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
```pde
int[] ia = {0, 1, 2, 3, 4, 5, 6, 7}; 
println(ia.length);  // Prints "8" 
ia = contract(ia, 5); 
println(ia.length);  // Prints "5" 

```

#### Descrição

	
Decreases the size of an array. The required**newSize** parameter provides precise control over the decrease in size.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
contract(<font color="#996600">array</font>, <font color="#996600">newSize</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
array
booleans[], bytes[], chars[], ints[], floats[], or Strings[]
newSize
positive int: new size for the array
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Array (the same datatype as the input)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[expand()](expand_)
