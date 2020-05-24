
#### Nome
### loadFont()

#### Exemplos
<img border="0" height="100" src="media/loadFont_.gif" width="100"/>
```pde
PFont font; 
// The font must be located in the sketch's 
// "data" directory to load successfully 
font = loadFont("FFScala-32.vlw"); 
textFont(font, 32); 
text("word", 15, 50); 

```

#### Descrição

	
Loads a font into a variable of type **PFont**. To load correctly, fonts must be located in the data directory of the current sketch.

#### Sintaxe
```pde
loadFont(fontname)

```
Parâmetros
fontname
string: name of the font to load



#### Retorno

	
PFont

#### Utilização

	
Web & Applicações

#### Relacionado

[PFont ](PFont
)
[textFont() ](textFont_
)
[text() ](text_
)

