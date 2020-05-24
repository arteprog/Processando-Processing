
#### Nome
### nf()

#### Exemplos

```pde
int a=200, b=40, c=90; 
String sa = nf(a, 10); 
println(sa); // Imprime "0000000200" 
String sb = nf(b, 5); 
println(sb); // Imprime "00040" 
String sc = nf(c, 3); 
println(sc); // Imprime "090" 
 
float d = 200.94, e = 40.2, f = 9.012; 
String sd = nf(d, 10, 4); 
println(sd);  // Imprime "0000000200.9400" 
String se = nf(e, 5, 3); 
println(se);  // Imprime "00040.200" 
String sf = nf(f, 3, 5); 
println(sf);  // Imprime "009.01200" 

```

#### Descrição
Função utilitária para se
formatar números em strings. Há duas versões, uma
para formatar floats e outra para formatar ints. Os valores dos
parâmentros**digitos**,**esquerda**, e**direita **devem ser sempre números inteiros positivos.

#### Sintaxe
```pde
nf(intValor, digitos)
nf(floatValor, esquerda, direita)

```
Parâmetros
intValor
int ou int[]: os números a formatar
digitos
int: números de dígitos a preencher com zeros zeroes
floatValor
float ou float[]: os números a formatar
lesquerda
int: numero de
algarismos à esqueda do ponto decimal (n.t. em inglês se
utiliza ponto ao invés de vírgula)
direita
int: numero de
algarismos à direita do ponto decimal (n.t. em inglês se
utiliza ponto ao invés de vírgula)

#### Retorno

	
String or String[]

#### Utilização

	
Web & Applicações

#### Relacionado
[nfs()](nfs_)[nfp()](nfp_)[nfc()](nfc_)
