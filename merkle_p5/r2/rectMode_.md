<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### rectMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/rectMode_.gif" width="100"/>

```pde
rectMode(CENTER); 
rect(35, 35, 50, 50); 
rectMode(CORNER); 
fill(102); 
rect(35, 35, 50, 50); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
 Modifica a localização a partir de
onde um retângulo é desenhado. A
configuração padrão é**rectMode(CORNER)**,
 a qual especifica a localizaçãocomo sendo o canto
superior esquedo da forma, e utiliza o terceiro e quarto
parâmetros de**rect() ** para especificar sua largura e altura.  O modo CORNERS especifica que os dois primeiros parâmetros de**rect()**  especificarão um canto, e que o terceiro e quarto especificarão o canto oposto. A chamada à**rectMode(CENTER)**  especifica que a forma será desenhada com refer6encia ao seu centro, e o terceiro e quarto parâmetros de**rect()** especificarão sua largura e altura.  O parâmetro MODO precisa ser todo escrito "MAIÚSCULA"
pelo fato de Processing ser uma linguagem onde letras
mínúsculas e maiúsculas são diferentes (*case sensitive*).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
rectMode(<font color="#996600">MODO</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODO
Qualquer um entre: CORNER, CORNERS, ou CENTER
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[rect()](rect_)
