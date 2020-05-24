
#### Nome
### image()

#### Exemplos
<img border="0" height="100" src="media/image_.jpg" width="100"/>

```pde
PImage b; 
// Imagems precisam estar no diretório "data" para carregar corretamente
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 

```
<img border="0" height="100" src="media/image_2.jpg" width="100"/>

```pde
PImage b; 
// Imagems precisam estar no diretório "data" para carregar corretamente
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 
image(b, 0, 0, width/2, height/2); 

```

#### Descrição
Visualiza imagens na tela. A imagem precisam estar
no diretório "data" do esboço para carregar corretamente.
Selecione "Add file ..."(n.t. Adicione arquivo)  no menu "Sketch"
(n.t. Esboço, Rascunho) para adicionar a imagem. Atualmente,
Processing trabalha como imagens no formato GIF, JPEG e Targa. A cor de
duma imagem pode ser modificada através da função `tint()`, e no caso de uma imgem GIF apresentar transparência, esta será mantida. O parâmetro `img `especifica a imagem a visualizar e os parâmentros `x` e `y `definem
a localização da imagem relativa ao seu canto superior
esquerdo. A imagem é visualizada em seu tamanho original,
 exceto quando os parâmetros `largura` e `altura` especificam um tamanho diferente.  A função `imageMode() ` altera a maneira com que os parâmetros trabalham. ` `Uma chamada a `imageMode(CORNERS)` alterará os parâmetros altura e largura de modo a definir os valores x e y do canto oposto da imagem.

#### Sintaxe
```pde
image(img, x, y)
image(img, x, y, largura, altura)

```
Parâmetros
img
PImage: a imagem a visualizar


x
int ou float: coordenada-x da imagem


y
int ou float: coordenada-y da imagem


width
int ou float: largura de
visualização da imagem ou coordenada x do canto inferior
direito (dependendo do modo de visualização)


height
int ou float: altura de
visualização da imagem ou coordenada-y do canto inferior
direito (dependendo do modo de visualização)



#### Utilização

	
Web & Applicações

#### Relacionado
[loadImage() ](loadImage_
)
[PImage  ](PImage
)
[imageMode()](imageMode_
)
[tint() ](tint_
)
[background() ](background_
)
[alpha()](alpha_
)

