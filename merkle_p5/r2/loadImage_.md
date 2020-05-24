
#### Nome
### loadImage()

#### Exemplos
<img border="0" height="100" src="media/loadImage_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 

```
<img border="0" height="100" src="media/loadImage_.jpg" width="100"/>

```pde
PImage b; 
 
void setup() { 
  b = loadImage("laDefense.jpg"); 
  noLoop(); 
} 
 
void draw() { 
  image(b, 0, 0); 
} 

```

#### Descrição
Carrega uma imagem em uma variável do tipo `PImage`. Três tipos de imagems ( **.gif**, **.jpg**, **.tga**)
podem ser carregadas. Para se carregar corretamente, as imagem precisam
estar no diretório "data" do esboço corrente. ` ` Na maioria dos casos, carregam-se todas as imagems dentro do `setup()` para pré-carregá-las no início do programa. Carregar as imagems em ` draw() `reduz
dramaticamente a valocidade do programa. Para se carregar corretamente
imagens .tga, estas devem ser de 32 bits e sem compressão ( *n.t. 32-bit uncompressed*) *. *

#### Sintaxe
```pde
loadImage(nomearquivo)

```
Parâmetros
nomearquivo
string: nome do arquivo a carregar. deve ser do tipo .gif, .jpg, ou .tga



#### Retorno

	
PImage

#### Utilização

	
Web & Applicações

#### Relacionado
[PImage ](PImage
)
[image() ](image_
)
[imageMode() ](imageMode_
)
[background() ](background_
)

