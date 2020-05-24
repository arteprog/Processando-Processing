
#### Nome
### PImage

#### Exemplos
<img border="0" height="100" src="media/PImage.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 

```

#### Descrição


Tipo de dados para se armazenar imagens. Processing oferece suporte para se visualizar imagens do tipo `.gif` e `.jpg`.
 Imagems podem ser visualisadas no espaço 2D e 3D. Antes d
euma imagem ser utilizada, é necessário carregá-la
através da função `loadImage()`. O objeto `PImage  `contém tanto propriedaddes de largura ( `width`) e altura ( `height`) da imagem,   como um array chamado `pixels[]`
que contem cada valor de píxel da imagem. Um grupo de
métodos, descritos abaixo, permite o acesso fácil aos
pixels e ao canal alpha da imagem, e simplificam o processo de
composição.
Campos
[width](PImage_width
)

largura da imagem


[height](PImage_height
)

altura da imagem


[pixels[]](PImage_pixels
)

array que conteém a cor de cada píxel da imagem


Métodos
[get()](PImage_get_
)

Lê a cor de qualquer pixel ou pega um retângulo de pixels


[set()](PImage_set_
)

Escreve uma cor em qualquer píxel ou escreve uma imagem em outra


[copy()](PImage_copy_
)

Copia uma imagem inteira


[mask()](PImage_mask_
)

Mascara parde de uma imagem de visualizar


[blend()](PImage_blend_
)

Copia um píxel ou um retângulo de pixels atravé de diferentes modos de mistura (n.t.<span style="font-style: italic;">blending<span style="font-weight: bold;"></span></span>)


[filter()](PImage_filter_
)

Converte a imagem em tom de cinza ou em preto e branco


Construtores
```pde
PImage()
PImage(largura, altura)
PImage(pixels[], largura, altura, formato)
PImage(img)

```
Parâmetros
largura
int: largura da imagem


altura
int: altura da imagem


pixels[]
int[] or color[]: array de inteiros ou de colors; deve ser do mesmo tamanho de largura*altura


formato
Qualquer um entre RGB, RGBA, ALPHA(canal alfa) (n.t.  *grayscale alpha channel* )


img
java.awt.Image: assume que a MediaTracker foi utilizada para se carregar os dados que que a img é válida



#### Utilização

	
Web & Applicações

#### Relacionado
[loadImage()](loadImage_
)
[imageMode()](imageMode_
)

