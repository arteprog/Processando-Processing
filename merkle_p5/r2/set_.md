
#### Nome
### set()

#### Exemplos
<img border="0" height="100" src="media/set_.gif" width="100"/>

```pde
color black = color(0); 
set(30, 20, black); 
set(85, 20, black); 
set(85, 75, black); 
set(30, 75, black); 

```
<img border="0" height="100" src="media/set_2.jpg" width="100"/>

```pde
for (int i=30; i<(width-15); i++) { 
  for(int j=20; j<(height-25); j++) { 
    color c = color(204-j, 153-i, 0); 
    set(i, j, c); 
  } 
} 

```
<img border="0" height="100" src="media/set_3.jpg" width="100"/>

```pde
size(100, 100, P3D); 
PImage myImage = loadImage("topanga.jpg"); 
set(0, 0, myImage); 
line(0, 0, width, height); 
line(0, height, width, 0); 

```

#### Descrição

Modifica a cor de qualquer
píxel ou escreve uma imagem diretamente na janela de
visualização. Os parâmetros x e y
especificam o píxel a modificar, e o parâmetro cor 
especificam sua cor. O parâmetro cor é afetato
pelo atual modo de cor (o valor padrão é o RGB com
valores entre 0 e 255). Ao especificar uma imagem, os parâmetros
x e y definem as coordenadas do canto superior esquerdo
da imagem (o posicionamente dda imagem não é afetado
pela função imageMode()). function).<br style="font-family: Helvetica,Arial,sans-serif;"/><br style="font-family: Helvetica,Arial,sans-serif;"/>
Atribuir  a cor a um único
píxel com set(x,y) é fácil, mas não tão
rápido como atribuir dados diretamente em pixels[]. Ao
se usar pixels[], o comando equivalente a "set(x,y,
#000000)" é "pixels[y*largura+x] = #000000. A versão BETA de Processing requer que se chame `loadPixels() `para se carregar a janela de visualização no array `pixels[]` antes que se pegue os valores. ow data into the **pixels[]** array before getting the values.

#### Sintaxe
```pde
set(x, y, cor)
set(x, y, imagem)

```
Parâmetros
x
int: coordenada-x do píxel


y
int: coordenada-y do píxel


cor
color: qualquer valor de tipo de dados color


imagem
PImage: qualquer variável válida do tipo PImage



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[get()](get_
)
[pixels[]](pixels
)

