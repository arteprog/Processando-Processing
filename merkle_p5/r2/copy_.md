
#### Nome
### copy()

#### Exemplos
<img border="0" height="100" src="media/copy_.jpg" width="100"/>

```pde
PImage img = loadImage("eames.jpg"); 
image(img, 0, 0); 
copy(15, 25, 10, 10, 35, 25, 50, 50); 
noFill(); 
// O retângulo mostra a áreas sendo copiada
rect(15, 25, 10, 10); 

```

#### Descrição
Copia uma região de pixels da janela de
visualização em outra região da janela de
visualização, ou copia uma região de pixels de uma
imagem definida pelo parâmetro `srcImg`
na janela de visualização.  Se as regiões
fonte e destino não forem do mesmo tamanho, ela irá
automaticamente redimensionar os pixels fonte ao tamenho da
região alvo. Neste processo não é utilizado
informação alfa, mas caso ca imagem fonte tenha um canal
alpha, esta também será copiado.  A
função `imageMode() ` altera a maneira com que os parâmetros trabalham. ` `Uma chamada a `imageMode(CORNERS)` alterará os parâmetros altura e largura de modo a definir os valores x e y do canto oposto da imagem.

#### Sintaxe
```pde
copy(fx, sy, flargura, faltura, dx, dy, dlargura, daltura)
copy(fntImg, fx, sy, fwidth, faltura, dx, dy, dlargura, daltura)

```
Parâmetros
fx
int: coordenada x do canto superior esquerdo da imagem fonte


sy
int: coordenada y do canto superior esquerdo da imagem fonte


flargura
int: largura da imagem fonte


faltura
int: altura da imagem fonte


dx
int: coordenada x do canto superior esquerdo da imagem destino


dy
int: coordenada y do canto superior esquerdo da imagem destino

dlargura


                  int: largura da imagem destino


daltura


                  int: altura da imagem destino


fntImg
PImage: a variável de imagem que se refere à imagem fonte



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[imageMode()](imageMode_
)
[blend()](blend_
)
[get()](get_
)

