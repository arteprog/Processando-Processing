
#### Nome
### texture()

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

#### Descrição

	
Sets a texture to be applied to vertex points. The **texture()** function must be called between **beginShape()** and **endShape()** and before any calls to **vertex()**.

#### Sintaxe
```pde
texture(img); 

```
Parâmetros
img
PImage: the texture to apply



#### Retorno

	
Nenhum

#### Utilização

	
Application & Web

#### Relacionado

[textureMode()](textureMode_
)
[beginShape()](beginShape_
)
[endShape()](endShape_
)
[vertex()](vertex_
)

