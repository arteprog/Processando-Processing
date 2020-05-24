<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### dist()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// atribui um tom de cinza como cor de fundo baseado 
// na distância do mouse ao centrao da tela de visualização
void draw() { 
  float d = dist(50, 50, mouseX, mouseY); 
  fill(d*4); 
  rect(0, 0, 99, 99); 
} 

```

#### Descrição
Calcula a distância entre dois pontos.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
dist(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>);
dist(<font color="#996600">x1</font>, <font color="#996600">y1</font>, <font color="#996600">z1</font>, <font color="#996600">x2</font>, <font color="#996600">y2</font>, <font color="#996600">z2</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x1
int ou float: coordenada-x do primeiro ponto
y1
int ou float: coordenada-y do primeiro ponto
z1
int ou float: coordenada-z do primeiro ponto
x2
int ou float: coordenada-x do segundo ponto
y2
int ou float: coordenada-y do segundo ponto
z2
int ou float: coordenada-z do segundo ponto
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
