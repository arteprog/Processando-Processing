
#### Nome
### asin()

#### Exemplos

```pde
float a = PI/3; 
float s = sin(a); 
float as = asin(s); 
// Imprime "1.0471976 : 0.86602545 : 1.0471976" 
println(a + " : " + s + " : " +  as); 

```



```pde
float a = PI + PI/3.0; 
float s = sin(a); 
float as = asin(s); 
// Imprime "4.1887903 : -0.86602545 : -1.0471976" 
println(a + " : " + s + " : " +  as); 

```



#### Descrição
A oposta de `sin()`; retorna  o arco seno de um valor. Esta função espera valores no
intervalo entre -1.0 e 1.0 e retona valores no intervalo entre **0** e **PI (3.1415927)**.

#### Sintaxe
```pde
asin(valor)

```
Parâmetros
valor
float: números entre -1.0 e 1.0



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[sin()](sin_
)
[acos()](acos_
)
[atan()](atan_
)

