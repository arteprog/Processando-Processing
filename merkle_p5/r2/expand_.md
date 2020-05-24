
#### Nome
### expand()

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

#### Sintaxe
```pde
expand(array)
expand(array, novoTam)

```
Parâmetros
array
boolean[], byte[], char[], int[], float[], ou String[]
novoTam
int positivo: novo tamanho do array

#### Retorno

	
Array (do mesmo tipo de dados da entrada)

#### Utilização

	
Web & Applicações

#### Relacionado
[contract()](contract_)
