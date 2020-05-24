<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### loadPixels()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/loadPixels_.jpg" width="100"/>

```pde
int halfImage = width*height/2; 
PImage myImage = loadImage("topanga.jpg"); 
image(myImage, 0, 0); 
 
loadPixels(); 
for(int i=0; i<halfImage; i++) { 
  pixels[i+halfImage] = pixels[i]; 
} 
updatePixels(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Carrega no array**pixel[]**
dados de pixels para a janela de visualização. Esta
função deve ser chamada sempre antes de se ler ou
escrever em**pixels[].**
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
loadPixels()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[pixels[]](pixels)[updatePixels()](updatePixels_)
