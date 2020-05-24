
#### Nome
### pow()

#### Exemplos

```pde
float a = pow( 1, 3);  // Atribui 1*1*1 = 1  à "a"
float b = pow( 3, 5);  // Atribui 3*3*3*3*3 = 243 à "b"
float c = pow( 3,-5);  // Atribui 1 / 3*3*3*3*3 = 1 / 243 = .0041 à "c" 
float d = pow(-3, 5);  // Atribui -3*-3*-3*-3*-3 = -243  à "d"

```



#### Descrição
Facilita  expressões exponenciais. A função `pow()`
é uma forma eficeitne de semultiplicar números por eleas
mesmos ( ou seus inversos) em grandes quantidades. Por exemplo , `pow(3,5)` é equivalente a expressão 3*3*3*3*3, e **pow(3, -5)** é equivalente à  1 / 3*3*3*3*3.

#### Sintaxe
```pde
pow(base, exponente)

```
Parâmetros
base
int ou float: base da expressão exponencial


exponente
int ou float: potência a ser elevada a base



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[sqrt()](sqrt_
)

