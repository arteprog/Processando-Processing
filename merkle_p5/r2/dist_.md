
#### Nome
### dist()

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

#### Sintaxe
```pde
dist(x1, y1, x2, y2);
dist(x1, y1, z1, x2, y2, z2);

```
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



#### Retorno

	
float

#### Utilização

	
Web & Applicações
