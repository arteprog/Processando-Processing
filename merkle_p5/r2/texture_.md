<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### texture()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/texture_.gif" width="100"/>
```pde
noStroke(); 
PImage a = loadImage("arch.jpg"); 
beginShape(); 
texture(a); 
vertex(10, 20, 0, 0); 
vertex(80, 5, 100, 0); 
vertex(95, 90, 100, 100); 
vertex(40, 95, 0, 100); 
endShape(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição

	
Sets a texture to be applied to vertex points. The**texture()** function must be called between**beginShape()** and**endShape()** and before any calls to**vertex()**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
texture(<font color="#996600">img</font>); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
img
PImage: the texture to apply
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application & Web
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado

[textureMode()](textureMode_)
[beginShape()](beginShape_)
[endShape()](endShape_)
[vertex()](vertex_)
