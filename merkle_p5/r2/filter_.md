
#### Nome
### filter()

#### Exemplos
<img border="0" height="100" src="media/filter_threshold.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("topanga.jpg"); 
image(b, 0, 0); 
filter(THRESHOLD); 

```
<img border="0" height="100" src="media/filter_gray.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("topanga.jpg"); 
image(b, 0, 0); 
filter(GRAY); 

```
<img border="0" height="100" src="media/filter_invert.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("topanga.jpg"); 
image(b, 0, 0); 
filter(INVERT); 
save("filter_invert.tif"); 

```
<img border="0" height="100" src="media/filter_posterize.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("topanga.jpg"); 
image(b, 0, 0); 
filter(GRAY); 
filter(POSTERIZE, 4); 

```
<img border="0" height="100" src="media/filter_blur.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("topanga.jpg"); 
image(b, 0, 0); 
filter(BLUR, 6); 

```

#### Descrição
Filtra a imagem de visualização como definido em um dos seguintes modos:


THRESHOLD  - converte a imagem para preto e branco dependendo se
os pixels estão acima ou abaixo de um limiar definido pelo
parâmetro ` nivel`. Este nível deve estar entre 0.0 (preto) e 1.0 (branco). Nos casos onde `nivel ` não é especificado, 0.5 é utilizado.


GRAY - converte quaisquer cores na imagem em seus equivalentes tons de cinza


INVERT - atribui a cada píxel seu valor inverso


POSTERIZE - limita cada canal da imagem a um número de cores especificada pelo parâmetro `nivel. `


BLUR - executa um borramento Gaussiano (n.t. *Guassian blur*), sendo que o parâmetro `level` especifica a extensão do borramento. Nos casos em que o parâmetro `level` não é utilizado, o borramento equivalente a um borramento gaussiano de raio 1.


OPAQUE - atribui ao canal alfa para ser inteiramente opaco

#### Sintaxe
```pde
filter(MODO)
ilter(MODO, nivel)

```
Parâmetros
MODO
Qualquer um entre: THRESHOLD, GRAY, INVERT, POSTERIZE, BLUR, ou OPAQUE


nivel
int ou float: define a qualidade do filtro



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[blend()](blend_
)

