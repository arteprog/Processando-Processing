
#### Nome
### textSize()

#### Exemplos
<img border="0" height="100" src="media/textSize_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 50); 
textSize(14); 
text("word", 15, 70); 

```

#### Descrição

	
Sets the current font size. This size will be used in all subsequent calls to the **text()** function. Font size is measured in units of pixels.

#### Sintaxe
```pde
textSize(size)

```
Parâmetros
size
int or float: the size of the letters in units of pixels



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado

[loadFont() ](loadFont_
)
[PFont ](PFont
)
[text()](text_
)
[textFont() ](textFont_
)

