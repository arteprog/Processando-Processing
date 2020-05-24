
#### Nome
### contract()

#### Exemplos
```pde
int[] ia = {0, 1, 2, 3, 4, 5, 6, 7}; 
println(ia.length);  // Prints "8" 
ia = contract(ia, 5); 
println(ia.length);  // Prints "5" 

```



#### Descrição

	
Decreases the size of an array. The required **newSize** parameter provides precise control over the decrease in size.

#### Sintaxe
```pde
contract(array, newSize)

```
Parâmetros
array
booleans[], bytes[], chars[], ints[], floats[], or Strings[]


newSize
positive int: new size for the array



#### Retorno

	
Array (the same datatype as the input)

#### Utilização

	
Web & Applicações

#### Relacionado

[expand()](expand_
)

