<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### copy()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Copia uma região de pixels da janela de
visualização em outra região da janela de
visualização, ou copia uma região de pixels de uma
imagem definida pelo parâmetro**srcImg**
na janela de visualização.  Se as regiões
fonte e destino não forem do mesmo tamanho, ela irá
automaticamente redimensionar os pixels fonte ao tamenho da
região alvo. Neste processo não é utilizado
informação alfa, mas caso ca imagem fonte tenha um canal
alpha, esta também será copiado.  A
função**imageMode() ** altera a maneira com que os parâmetros trabalham.** **Uma chamada a**imageMode(CORNERS)** alterará os parâmetros altura e largura de modo a definir os valores x e y do canto oposto da imagem.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
copy(<font color="#996600">fx</font>, <font color="#996600">sy</font>, <font color="#996600">flargura</font>, <font color="#996600">faltura</font>, <font color="#996600">dx</font>, <font color="#996600">dy</font>, <font color="#996600">dlargura</font>, <font color="#996600">daltura</font>)
copy(<font color="#996600">fntImg</font>, <font color="#996600">fx</font>, <font color="#996600">sy</font>, <font color="#996600">fwidth</font>, <font color="#996600">faltura</font>, <font color="#996600">dx</font>, <font color="#996600">dy</font>, <font color="#996600">dlargura</font>, <font color="#996600">daltura</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[imageMode()](imageMode_)[blend()](blend_)[get()](get_)
