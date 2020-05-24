
#### Nome
### subset()

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
Extrai um array de elementos de uma array existente. O parâmetro `array` define o array do qual os elementos serão copiandos, e os parâmetros `offset` e `lenght` determinan quais elementos a extrair. Caso `length  ` nao seja dado, os elementos extraídos irão de `offset` ao final do array. Ao se especificar o `offset`, lembrar que o primeiro elemento do array é o 0. Esta função não modifica o array fonte.

#### Sintaxe
```pde
subset(array, offset)
subset(array, offset, length)

```
Parâmetros
array
boolean[], byte[], char[], int[], float[], or String[]: array base


offset
int: posição para iniciar cópia


length
int: número de elementos as extrair



#### Retorno

	
Array (do mesmo tipo do array de entrada)

#### Utilização

	
Web & Applicações

#### Relacionado
[splice()](splice_
)

