<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadImage()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/loadImage_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Carrega uma imagem em uma variável do tipo**PImage**. Três tipos de imagems (**.gif**,**.jpg**,**.tga**)
podem ser carregadas. Para se carregar corretamente, as imagem precisam
estar no diretório "data" do esboço corrente.** ** Na maioria dos casos, carregam-se todas as imagems dentro do**setup()** para pré-carregá-las no início do programa. Carregar as imagems em** draw() **reduz
dramaticamente a valocidade do programa. Para se carregar corretamente
imagens .tga, estas devem ser de 32 bits e sem compressão (*n.t. 32-bit uncompressed*)*. *
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadImage(<font color="#996600">nomearquivo</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
nomearquivo
string: nome do arquivo a carregar. deve ser do tipo .gif, .jpg, ou .tga
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
PImage
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[PImage ](PImage)[image() ](image_)[imageMode() ](imageMode_)[background() ](background_)
