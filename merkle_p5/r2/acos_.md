
#### Nome
### acos()

#### Exemplos

```pde
float a = PI; 
float c = cos(a); 
float ac = acos(c); 
// Imprime "3.1415927 : -1.0 : 3.1415927" 
println(a + " : " + c + " : " +  ac); 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
float a = PI + PI/4.0; 
float c = cos(a); 
float ac = acos(c); 
// Imprime "3.926991 : -0.70710665 : 2.3561943" 
println(a + " : " + c + " : " +  ac); 

```

#### Descrição
A oposta a**cos()**, retorna o arco
cosseno de um valor. Esta função espera valores no
intervalo entre -1.0 e 1.0 e  retona valores no intervalo entre**0** e**PI (3.1415927)**.

#### Sintaxe
```pde
acos(valor)

```
Parâmetros
valor
float: números entre -1.0 e 1.0

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[cos()](cos_)[asin()](asin_)[atan()](atan_)
