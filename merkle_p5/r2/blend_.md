
#### Nome
### blend()

#### Exemplos
<img border="0" height="100" src="media/blend_color.gif" width="100"/>

```pde
color orange = color(204, 102, 0); 
color blue = color(0, 102, 153); 
color orangeblueadd = blend(orange, blue, ADD); 
background(51); 
noStroke(); 
fill(orange); 
rect(14, 20, 20, 60); 
fill(orangeblueadd); 
rect(40, 20, 20, 60); 
fill(blue); 
rect(66, 20, 20, 60); 

```
<img border="0" height="100" src="media/blend_add.jpg" width="100"/>

```pde
background(loadImage("rockies.jpg")); 
PImage img = loadImage("degaul.jpg"); 
image(img, 0, 0); 
blend(img, 0, 0, 33, 100, 67, 0, 33, 100, ADD); 

```
<img border="0" height="100" src="media/blend_subtract.jpg" width="100"/>

```pde
background(loadImage("rockies.jpg")); 
PImage img = loadImage("degaul.jpg"); 
image(img, 0, 0); 
blend(img, 0, 0, 33, 100, 67, 0, 33, 100, SUBTRACT); 

```
<img border="0" height="100" src="media/blend_darkest.jpg" width="100"/>

```pde
background(loadImage("rockies.jpg")); 
PImage img = loadImage("degaul.jpg"); 
image(img, 0, 0); 
blend(img, 0, 0, 33, 100, 67, 0, 33, 100, DARKEST); 

```
<img border="0" height="100" src="media/blend_lightest.jpg" width="100"/>

```pde
background(loadImage("rockies.jpg")); 
PImage img = loadImage("degaul.jpg"); 
image(img, 0, 0); 
blend(img, 0, 0, 33, 100, 67, 0, 33, 100, LIGHTEST); 

```

#### Descrição
Mistura dois valores de cor ou copia um
único pixel ou região de pixels de uma imagem em outra
(ou na própria imagem) , com suporte copleto a canal alfa.
Há a escolha dos segintes modos para misturar os pixels fonte
(A) aos pixels destino (B).



BLEND - interpolação linear de cores: C = A*factor + B



ADD - mistura aditiva com recorte em branco: C = min(A*factor + B, 255)



SUBTRACT - smistura subtrativa com recorte em preto: C = max(B - A*factor, 0)



DARKEST - apenas a cor mais escura sucede: C = min(A*factor, B)



LIGHTEST - apenas a cor mais clara sucede: C = max(A*factor, B)



Todos os modos utilizam informação alfa (byte mais alto)
dos pixels da imagem fonte como fator de mistura. Se os tamanhos das
regiões da fonte e do destino são diferentes, a imagem
será automaticamente redimensionada  de mod adequado ao
tamanho do destino. Se parâmetro `srcImg` não for utilizado, a tela de visualização é utilizada como imagem fonte.



A função `imageMode() `modificará o modo de trabalho dos parâmetros. Por exemplo, uma chamada à `imageMode(CORNERS) ` modificará
 os parâmetros de definirem largura e altura para definirem
os valores dos cantos opostos a x e y.

#### Sintaxe
```pde
blend(c1, c2, mode);
blend(fx, fy, dx, dy, mode);
blend(fntImg, fx, fy, dx, dy, mode);
blend(fx1, fy1, flargura, faltura, dx1, dy1, dlargura, daltura, mode);
blend(fntImg, fx1, fy1, flargura, faltura, dx1, dy1, dlargura, daltura, mode);

```
Parâmetros
c1
color: a primeira cor a misturar


c2
color: a segunda cor a misturar


mode
Qualquer um entre: BLEND, ADD, SUBTRACT, LIGHTEST, ou DARKEST


fx
int: coordenada-x do píxel da imagem fonte


fy
int: coordenada-y do píxel na imagem fonte


dx
int: coordenada-x do píxel da imagem destino


dy
int: coordenada-y do píxel da imagem destino


fntImg
PImage: a variável de imagem que se refere à imagem fonte<description>



</description>
fx1
int: coordenada x do canto superior esquerdo da imagem fonte


fy1
int: coordenada y do canto superior esquerdo da imagem fonte


flargura
int: largura da imagem fonte


faltura
int: altura da imagem fonte


dx1
int: coordenada x do canto superior esquerdo da imagem destino


dy1
int: coordenada y do canto superior esquerdo da imagem destino


dlargura
int: largura da imagem destino


daltura
int: altura da imagem destino



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[filter()](filter_
)

