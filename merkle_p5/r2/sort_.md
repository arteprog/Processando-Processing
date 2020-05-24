<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### sort()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
sort(<font color="#996600">dataArray</font>)
sort(<font color="#996600">dataArray</font>, <font color="#996600">count</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
dataArray
String[], int[], ou float[]
count
int: número dos elementos iniciais do array a ordenart
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Array (do mesmo tipo de dados da entrada)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[reverse()](reverse_)
