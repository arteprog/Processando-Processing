
#### Nome
### imageMode()

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

#### Descrição
Modifica a localização da qual uma imagem é desenhada.  O modo padrão é**imageMode(CORNER)**
o qual especifica a localização como sendo o canto
superior esquerdo, e utiliza o quarto e quinto parâmetos de**image()** como a largura e a altura da imagem. A sintaxe**imageMode(CORNERS)**
utiliza o segundo e terceiro parâmetros para se especificar um
canto da imagem, e o quarto e quinto parâmetros para especificar
o canto oposto. O parâmentre de**imageMode()** deve ser escrito "TODO EM MAIÚSCULAS**"** pelo fato de Processing ser sensitiva a caixa das letras (n.t.*case sensitive language*).

#### Sintaxe
```pde
imageMode(MODO)

```
Parâmetros
MODO
Qualquer um entre CORNER ou CORNERS

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[loadImage() ](loadImage_)[PImage ](PImage)[image() ](image_)[imageMode() ](imageMode_)[background() ](background_)
