
#### Nome
### sort()

#### Exemplos

```pde
float a[] = { 3.4, 3.6, 2, 0, 7.1 }; 
a = sort(a); 
for (int i = 0; i < a.length; i++) { 
  println(a[i]); 
} 
 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
String s[] = { "deer", "elephant", "bear", "aardvark", "cat" }; 
s = sort(s); 
print(s);  // Imprime "aardvark bear cat deer elephant" 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
String s[] = { "deer", "elephant", "bear", "aardvark", "cat" }; 
s = sort(s, 3); 
print(s);  // Imprime "bear dear elephant" 
 

```

#### Descrição
Ordena um array de números do menor ao
maior, ou colococa um array de palavras em ordem alfabética.
 O array original não é modificado, e um array
reordenado é retornado. O parâmetro**count** fornece o número de elementos a ordenar. Por exemplo, caso haja 12 elementos em um array e o valor de**count **dor 5,  apenas os primeiros cinco elementos serão ordenados.

#### Sintaxe
```pde
sort(dataArray)
sort(dataArray, count)

```
Parâmetros
dataArray
String[], int[], ou float[]
count
int: número dos elementos iniciais do array a ordenart

#### Retorno

	
Array (do mesmo tipo de dados da entrada)

#### Utilização

	
Web & Applicações

#### Relacionado
[reverse()](reverse_)
