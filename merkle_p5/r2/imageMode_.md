<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### imageMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/imageMode_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense_crop.jpg"); 
imageMode(CORNERS); 
image(b, 10, 10, 60, 60); 
imageMode(CORNER); 
image(b, 35, 35, 50, 50); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Modifica a localização da qual uma imagem é desenhada.  O modo padrão é**imageMode(CORNER)**
o qual especifica a localização como sendo o canto
superior esquerdo, e utiliza o quarto e quinto parâmetos de**image()** como a largura e a altura da imagem. A sintaxe**imageMode(CORNERS)**
utiliza o segundo e terceiro parâmetros para se especificar um
canto da imagem, e o quarto e quinto parâmetros para especificar
o canto oposto. O parâmentre de**imageMode()** deve ser escrito "TODO EM MAIÚSCULAS**"** pelo fato de Processing ser sensitiva a caixa das letras (n.t.*case sensitive language*).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
imageMode(MODO)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODO
Qualquer um entre CORNER ou CORNERS
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadImage() ](loadImage_)[PImage ](PImage)[image() ](image_)[imageMode() ](imageMode_)[background() ](background_)
