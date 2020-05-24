
#### Nome
### textFont()

#### Exemplos
<img border="0" height="100" src="media/textFont_.gif" width="100"/>
```pde
PFont metaBold; 
// The font "Meta-Bold.vlw.gz" must be located in the 
// current sketch's "data" directory to load successfully 
metaBold = loadFont("Meta-Bold.vlw.gz"); 
textFont(metaBold, 44); 
text("word", 15, 50); 

```

#### Descrição

	
Sets the current font. The font must be loaded with**loadFont()** before it can be used. This font will be used in all subsequent calls to the**text()** function. If no**size** parameter is input, the font will appear at its original size (the size it was created at with the "Create Font..." tool) until it is changed with**textSize()**.

#### Sintaxe
```pde
textFont(font)
textFont(font, size)

```
Parâmetros
font
PFont: any variable of the type PFont
size
int or float: the size of the letters in units of pixels

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado

[loadFont() ](loadFont_)
[PFont ](PFont)
[text() ](text_)
