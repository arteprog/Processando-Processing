<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### textureMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/textureMode_.gif" width="100"/>
```pde
noStroke(); 
PImage a = loadImage("arch.jpg"); 
textureMode(IMAGE); 
beginShape(); 
texture(a); 
vertex(10, 20, 0, 0); 
vertex(80, 5, 100, 0); 
vertex(95, 90, 100, 100); 
vertex(40, 95, 0, 100); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/textureMode_2.gif" width="100"/>
```pde
noStroke(); 
PImage a = loadImage("arch.jpg"); 
textureMode(NORMALIZED); 
beginShape(); 
texture(a); 
vertex(10, 20, 0, 0); 
vertex(80, 5, 1, 0); 
vertex(95, 90, 1, 1); 
vertex(40, 95, 0, 1); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Sets the coordinate space for texture mapping. There are two options, IMAGE, which refers to the actual coordinates of the image, and NORMALIZED, which refers to a normalized space of values ranging from 0 to 1. The default mode is IMAGE. In IMAGE, if an image is 100 x 200 pixels, mapping the image onto the entire size of a quad would require the points (0,0) (0,100) (100,200) (0,200). The same mapping in NORMAL_SPACE is (0,0) (0,1) (1,1) (0,1).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
texture(<font color="#996600">MODE</font>); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODE
either IMAGE or NORMALIZED
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application & Web
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[texture()](texture_)
