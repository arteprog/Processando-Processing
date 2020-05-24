<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### nf()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
nf(<font color="#996600">intValor</font>, <font color="#996600">digitos</font>)
nf(<font color="#996600">floatValor</font>, <font color="#996600">esquerda</font>, <font color="#996600">direita</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
String or String[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[nfs()](nfs_)[nfp()](nfp_)[nfc()](nfc_)
