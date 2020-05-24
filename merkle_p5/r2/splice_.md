
#### Nome
### splice()

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

#### Sintaxe
```pde
splice(array, value, index)
splice(array, array2, index)

```
Parâmetros
array
booleans[], bytes[], chars[], ints[], floats[], or Strings[]: base array
value
booleans, bytes, chars, ints, floats, or Strings: value to be spliced in
array2
booleans[], bytes[], chars[], ints[], floats[], Strings[]: array to be spliced in
index
int: position in the array from which to insert data

#### Retorno

	
Array (the same datatype as the input)

#### Utilização

	
Web & Applicações

#### Relacionado

[contract()](contract_)
[subset()](subset_)
