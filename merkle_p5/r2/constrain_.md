
#### Nome
### constrain()

#### Exemplos

```pde
void draw() 
{ 
  background(204); 
  float mx = constrain(mouseX, 30, 70); 
  rect(mx-10, 40, 20, 20); 
} 

```

#### Descrição

Restringe um valor a um intervalo definico por um valor mínimo e um máximo.

#### Sintaxe
```pde
constrain(valor, min, max)

```
Parâmetros
valor
int ou float: o calor a ser restrito
min
int ou float: limite mínimo
max
int ou float: limite máximo

#### Retorno

	
float ou int (dependendo dos valores de entrada)

#### Utilização

	
Web & Applicações

#### Relacionado
[max()](max_)[min()](min_)
