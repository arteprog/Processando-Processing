
#### Nome
### arraycopy()

#### Exemplos

```pde
String north[] = { "OH", "IN", "MI"}; 
String south[] = { "GA", "FL", "NC"}; 
arraycopy(north, south); 
print(south);  // Imprime "OH IN MI" 
 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
String north[] = { "OH", "IN", "MI"}; 
String south[] = { "GA", "FL", "NC"}; 
arraycopy(north, 1, south, 0, 2); 
print(south);  // Imprime "IN MI NC" 
 

```

#### Descrição
Copia um array (ou parte dele) em outro array. O array**src** é copiado ao array**dst, **começando a cópia pela posição especificada por**srcPos** com destino na posição especificada por**dstPos.** O número de elementos copiado é especificado por**tamanho.**
A varsão simplificada com dois argumentos copia um array inteiro
em outro de mesmo tamanho. É equivalente à
"arraycopy(src, 0, dst, 0, src.length)".  Esta
função é muito mais eficiente do que copiar os
dados de um array mediante a iteração em um laço**for()** onde se copia cada um dos elementos.

#### Sintaxe
```pde
arraycopy(src, dest)
arraycopy(src, srcPos, dest, destPos, tamanho)

```
Parâmetros
src
booleans[], bytes[], chars[], ints[], floats[], or Strings[]: o array fonte
dest
booleans[], bytes[], chars[], ints[], floats[], or Strings[]: o array destino
srcPos
int: posição de início no array fonte
destPos
int: posição de início no array destino
tamabho
int: número de elementos a ser copiado

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações
