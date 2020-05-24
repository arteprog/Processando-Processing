
#### Nome
### lightSpecular()

#### Exemplos
<img border="0" height="100" src="media/lightSpecular_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
directionalLight(102, 102, 102, 0, 0, -1); 
lightSpecular(204, 204, 204); 
directionalLight(102, 102, 102, 0, 1, -1); 
lightSpecular(102, 102, 102); 
translate(20, 50, 0); 
specular(51, 51, 51); 
sphere(30); 
translate(60, 0, 0); 
specular(102, 102, 102); 
sphere(30); 
 

```

#### Descrição
Especifica a cor especular para luzes. 

Como com a função `fill(), ` a função **lightFalloff()**afeta
apenas os elementos que forem criados após sua chamada no
código.  Especular se refere à luz que é
refletita por uma superfície em uma determinada
direção (em contraste a ser refletida em todas as
direções como luz difusa), e é utilizada em
realces. A qualidade especulara de uma luz interage com as qualidades
especulares de materiais especificados attravés das
funções **specular()** e **shininess()**.

#### Sintaxe
```pde
lightSpecular(v1, v2, v3)

```
Parâmetros
v1
int ou float: valor de vermelho red ou de matiz


v2
int ou float: valor de verde ou de saturação (n.t. hue value?)


v3
int ou float: valor de azul ou de brilho (n.t. hue value?)



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[lights()](lights_
)
[ambientLight()](ambientLight_
)
[pointLight()](pointLight_
)
[spotLight()](spotLight_
)

