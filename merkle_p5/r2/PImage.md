<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### PImage
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/PImage.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

Tipo de dados para se armazenar imagens. Processing oferece suporte para se visualizar imagens do tipo**.gif** e**.jpg**.
 Imagems podem ser visualisadas no espaço 2D e 3D. Antes d
euma imagem ser utilizada, é necessário carregá-la
através da função**loadImage()**. O objeto**PImage  **contém tanto propriedaddes de largura (**width**) e altura (**height**) da imagem,   como um array chamado**pixels[]**
que contem cada valor de píxel da imagem. Um grupo de
métodos, descritos abaixo, permite o acesso fácil aos
pixels e ao canal alpha da imagem, e simplificam o processo de
composição.
<img height="25" src="../images/1pix.gif" width="1"/>
Campos
[width](PImage_width)
largura da imagem
[height](PImage_height)
altura da imagem
[pixels[]](PImage_pixels)
array que conteém a cor de cada píxel da imagem
<img height="25" src="../images/1pix.gif" width="1"/>
Métodos
[get()](PImage_get_)
Lê a cor de qualquer pixel ou pega um retângulo de pixels
[set()](PImage_set_)
Escreve uma cor em qualquer píxel ou escreve uma imagem em outra
[copy()](PImage_copy_)
Copia uma imagem inteira
[mask()](PImage_mask_)
Mascara parde de uma imagem de visualizar
[blend()](PImage_blend_)
Copia um píxel ou um retângulo de pixels atravé de diferentes modos de mistura (n.t.<span style="font-style: italic;">blending<span style="font-weight: bold;"></span></span>)
[filter()](PImage_filter_)
Converte a imagem em tom de cinza ou em preto e branco
<img height="25" src="../images/1pix.gif" width="1"/>
<img height="25" src="../images/1pix.gif" width="1"/>
Construtores
```pde
PImage()
PImage(<font color="#996600">largura</font>, <font color="#996600">altura</font>)
PImage(<font color="#996600">pixels[]</font>, <font color="#996600">largura</font>, <font color="#996600">altura</font>, <font color="#996600">formato</font>)
PImage(<font color="#996600">img</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
largura
int: largura da imagem
altura
int: altura da imagem
pixels[]
int[] or color[]: array de inteiros ou de colors; deve ser do mesmo tamanho de largura*altura
formato
Qualquer um entre RGB, RGBA, ALPHA(canal alfa) (n.t. *grayscale alpha channel*)
img
java.awt.Image: assume que a MediaTracker foi utilizada para se carregar os dados que que a img é válida
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadImage()](loadImage_)[imageMode()](imageMode_)
