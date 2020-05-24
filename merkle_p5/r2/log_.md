
#### Nome
### log()

#### Exemplos

```pde
void setup() { 
  int i = 12; 
  println(log(i)); 
  println(log10(i)); 
} 
 
// Calculates the base-10 logarithm of a number 
float log10 (int x) { 
  return (log(x) / log(10)); 
} 

```

#### Descrição
Calcula o logaritmo natural (logaritmo na base*e*) de um número. Esta função espera que valoressejam maiores que 0.0.

#### Sintaxe
```pde
log(valor)

```
Parâmetros
valor
int ou float: número dever ser maior que 0.0

#### Retorno

	
float

#### Utilização

	
Web & Applicações
