<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### constrain()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
constrain(<font color="#996600">valor</font>, <font color="#996600">min</font>, <font color="#996600">max</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor
int ou float: o calor a ser restrito
min
int ou float: limite mínimo
max
int ou float: limite máximo
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float ou int (dependendo dos valores de entrada)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[max()](max_)[min()](min_)
