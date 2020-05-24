
#### Nome
### rectMode()

#### Exemplos
<img border="0" height="100" src="media/rectMode_.gif" width="100"/>

```pde
rectMode(CENTER); 
rect(35, 35, 50, 50); 
rectMode(CORNER); 
fill(102); 
rect(35, 35, 50, 50); 

```

#### Descrição
 Modifica a localização a partir de
onde um retângulo é desenhado. A
configuração padrão é **rectMode(CORNER)**,
 a qual especifica a localizaçãocomo sendo o canto
superior esquedo da forma, e utiliza o terceiro e quarto
parâmetros de `rect() ` para especificar sua largura e altura.  O modo CORNERS especifica que os dois primeiros parâmetros de `rect()`  especificarão um canto, e que o terceiro e quarto especificarão o canto oposto. A chamada à `rectMode(CENTER)`  especifica que a forma será desenhada com refer6encia ao seu centro, e o terceiro e quarto parâmetros de `rect()` especificarão sua largura e altura.  O parâmetro MODO precisa ser todo escrito "MAIÚSCULA"
pelo fato de Processing ser uma linguagem onde letras
mínúsculas e maiúsculas são diferentes ( *case sensitive*).

#### Sintaxe
```pde
rectMode(MODO)

```
Parâmetros
MODO
Qualquer um entre: CORNER, CORNERS, ou CENTER



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[rect()](rect_
)

