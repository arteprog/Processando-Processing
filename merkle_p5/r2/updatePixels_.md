
#### Nome
### updatePixels()

#### Exemplos
<img border="0" height="100" src="media/updatePixels_.jpg" width="100"/>

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
<img border="0" height="100" src="media/updatePixels_2.jpg" width="100"/>

```pde
int halfImage = width*height/2; 
PImage myImage = loadImage("towerFlip.jpg"); 
image(myImage, 0, 0); 
 
loadPixels(); 
for(int i=0; i<halfImage; i++) { 
  pixels[i+halfImage] = pixels[i]; 
} 
 
updatePixels(50, 0, 50, 100); 

```

#### Descrição
Atualiza
a janela de visualização com os dados correntes
armazenados em pixels[]. É possível atualizar
apenas uma porção da janela de visualização,
o que se faz ao expecificar um retângulo menor através
dos parâmetros x1, y1, largura, e altura.
A função imageMode() altera o modo de trabalho
destes parâmetros.  Por exemplo, imageMode(CENTER)
assumirá x e y como sendo o centro da
imagem. Uma chamada à imageMode(CORNERS) assumirá
que os parâmetros largura e altura estarão
definindo as coordeadas opostas da imagem.

#### Sintaxe
```pde
updatePixels()
updatePixels(x1, y1, largura, altura)

```
Parâmetros
x1
int: coordenada-x do canto superior esquerdo


y1
int: coordenada-y do canto superior esquerdo


largura
largura
ou coordenadax do canto oposto, dependendo do atual modo configurado por  imageMode()


altura
altura
ou coordenada-y do canto oposto, dependendo do atual modo configurado por imageMode()



#### Utilização

	
Web & Applicações

#### Relacionado
[pixels[]](pixels
)
[loadPixels()](loadPixels_
)

