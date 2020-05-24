
#### Nome
### loadPixels()

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

#### Descrição
Carrega no array `pixel[]`
dados de pixels para a janela de visualização. Esta
função deve ser chamada sempre antes de se ler ou
escrever em `pixels[].`

#### Sintaxe
```pde
loadPixels()

```

#### Utilização

	
Web & Applicações

#### Relacionado
[pixels[]](pixels
)
[updatePixels()](updatePixels_
)

