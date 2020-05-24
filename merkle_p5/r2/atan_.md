
#### Nome
### atan()

#### Exemplos

```pde
float a = PI/3; 
float t = tan(a); 
float at = atan(t); 
// Imprime "1.0471976 : 1.7320509 : 1.0471976" 
println(a + " : " + t + " : " +  at); 

```



```pde
float a = PI + PI/3.0; 
float t = tan(a); 
float at = atan(t); 
// Imprime "4.1887903 : 1.7320513 : 1.0471977" 
println(a + " : " + t + " : " +  at); 

```



#### Descrição
A oposta a **tan()**; retorna o arco tangente de um valor.<b></b> This function expects the valors in the range of -Infinity to Infinity (exclusive) and valors are returned in the range **-PI/2** to **PI/2 **.

#### Sintaxe
```pde
atan(valor)

```
Parâmetros
valor
float: -Infinito a +Infinito (exclusivo)



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[tan()](tan_
)
[asin()](asin_
)
[acos()](acos_
)

