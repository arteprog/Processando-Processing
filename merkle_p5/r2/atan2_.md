
#### Nome
### atan2()

#### Exemplos

```pde
void draw() { 
  background(204); 
  translate(width/2, height/2); 
  float a = atan2(mouseY-height/2, mouseX-width/2); 
  rotate(a); 
  rect(-12, -5, 24, 10); 
} 

```



#### Descrição
Calcula o ângulo (em radianos) de um ponto
especificado em relação à origem e medido em
relação ao eixo-x. Valores são retornados como `float` e no intervalo entre `-Pi ` e `PI.` A função ` atan2()`
é ferqüentemente utilizada para na orientação
de formas geométricas através da posição do
cursor. A coordenada-y do ponto é o primeiro parâmetro e a
coordenada-x o segundo, conforme a estrutura de cálculo da
tangente.

#### Sintaxe
```pde
atan2(y, x); 

```
Parâmetros
y
int ou float: coordenada-y do ponto


x
int ou float: coordenada-x do ponto



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[tan()](tan_
)

