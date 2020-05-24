<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### splice()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
```pde
String sa1[] = { "OH ", "NY ", "CA "}; 
sa1 = splice(sa1, "KY ", 1); 
print(sa1);  // Prints "OH KY NY CA " 
println(); 
String sa2[] = { "VA ", "CO ", "IL "  }; 
sa1 = splice(sa1, sa2, 2); 
print(sa1);  // Prints "OH KY VA CO IL NY CA " 

```

#### Descrição

	
Inserts a value or array of values into an existing array. The first two parameters must be of the same datatype. The**array** parameter defines the array which will be modified and the second parameter defines the data which will be inserted.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
splice(<font color="#996600">array</font>, <font color="#996600">value</font>, <font color="#996600">index</font>)
splice(<font color="#996600">array</font>, <font color="#996600">array2</font>, <font color="#996600">index</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
array
booleans[], bytes[], chars[], ints[], floats[], or Strings[]: base array
value
booleans, bytes, chars, ints, floats, or Strings: value to be spliced in
array2
booleans[], bytes[], chars[], ints[], floats[], Strings[]: array to be spliced in
index
int: position in the array from which to insert data
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Array (the same datatype as the input)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[contract()](contract_)
[subset()](subset_)
