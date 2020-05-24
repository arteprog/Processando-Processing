
#### Nome
### nfs()

#### Exemplos

```pde
int a=200, b=-40, c=90; 
String sa = nfs(a, 10); 
println(sa); // Imprime " 0000000200" 
String sb = nfs(b, 5); 
println(sb); // Imprime "-00040" 
String sc = nfs(c, 3); 
println(sc); // Imprime " 090" 
 
float d = -200.94, e = 40.2, f = -9.012; 
String sd = nfs(d, 10, 4); 
println(sd);  // Imprime "-0000000200.9400" 
String se = nfs(e, 5, 3); 
println(se);  // Imprime " 00040.200" 
String sf = nfs(f, 3, 5); 
println(sf);  // Imprime "-009.01200" 

```



#### Descrição
Função utilitária para se
formatar números em strings.É similar a `nf() `mas
coloca um espaço ("+""em frente dos números positivos e
um "-"em frente dos números negativos.  Há duas
versões, uma
para formatar floats e outra para formatar ints. Os valores dos
parâmentros **digitos**, **esquerda**, e **direita **devem ser sempre números inteiros positivos.

#### Sintaxe
```pde
nfs(intValor, digitos)
nfs(floatValor, esquerda, direita)

```
Parâmetros
intValor
int ou int[]: os números a formatar


digitos
int: números de dígitos a preencher com zeros

floatValor


                  float ou float[]: os números a formatar


esquerda


                  int: numero de
algarismos à esqueda do ponto decimal (n.t. em inglês se
utiliza ponto ao invés de vírgula)


direita


                  int: numero de
algarismos à direita do ponto decimal (n.t. em inglês se
utiliza ponto ao invés de vírgula)



#### Retorno

	
String ou String[]

#### Utilização

	
Web & Applicações

#### Relacionado
[nf()](nf_
)
[nfp()](nfp_
)
[nfc()](nfc_
)

