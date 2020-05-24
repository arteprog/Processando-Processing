<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### atan2()
<img height="25" src="../images/1pix.gif" width="1"/>

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
relação ao eixo-x. Valores são retornados como**float** e no intervalo entre**-Pi ** e**PI.** A função** atan2()**
é ferqüentemente utilizada para na orientação
de formas geométricas através da posição do
cursor. A coordenada-y do ponto é o primeiro parâmetro e a
coordenada-x o segundo, conforme a estrutura de cálculo da
tangente.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
atan2(<font color="#996600">y</font>, <font color="#996600">x</font>); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
y
int ou float: coordenada-y do ponto
x
int ou float: coordenada-x do ponto
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[tan()](tan_)
