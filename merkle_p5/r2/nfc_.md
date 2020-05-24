
#### Nome
### nfc()

#### Exemplos

```pde
int i = 500000; 
String si = nfc(i); 
println(si);  // Imprime "500,000" 
float f = 42525.34343; 
String fi = nfc(f, 2); 
println(fi);  // Imprime "42,525.34" 
 

```



#### Descrição
Função utilitária para se
formatar números em strinds e posicionar vírgulas para
demarcar unidades de Há duas versões, uma
para formatar floats e outra para formatar ints. Os valores do
parâmentros **digitos** deve ser sempre um números inteiro positivo.



Utility function for formatting numbers into strings and placing
appropriate commas to mark units of 100. There are two versions, one
for formatting ints and one for formatting an array of ints. The value
for the **digits** parameter should always be a positive integer.

#### Sintaxe
```pde
nfc(intValor)
nfc(floatValue, direita)

```
Parâmetros
intValor
int ou int[]: o(s) número(s) a formatar


floatValor
float ou float[]: o(s) número(s) a formatar


direita
int: o número de digitos após o ponto decimal



#### Retorno

	
String ou String[]

#### Utilização

	
Web & Applicações

#### Relacionado
[nf()](nf_
)
[nfs()](nfs_
)
[nfp()](nfp_
)

