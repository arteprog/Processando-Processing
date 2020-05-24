<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### pixels[]
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/pixels.gif" width="100"/>

```pde
color pink = color(255, 102, 204); 
loadPixels(); 
for (int i=0; i<(width*height/2)-width/2; i++) { 
  pixels[i] = pink; 
} 
updatePixels(); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Array que contém os valores de todos os
pixels da janela de visualização.  Este array
é do tamanha da janela de visualização. Por
exemplo, se a imagem é 100x100, haverão 10000 valores, e
se a janela for 200x300, haverão 60000 valores. O valor de**index **define a posição de um valor neste array. Por exemplo, o comando**color b = pixels[230] ** atribuirá à variável**b **valor
igual ao valor daquela localização no array. Ante de
acessar  este aeeay, seus dados precisam ser carregados
através da função**loadPixels()**. Após o array ser modificado, a função**updatePixels()** precisa ser chamdada para atualizar as mudanças.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
pixels[<font color="#996600">index</font>]

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
index
int: não deve exceder o tamanho do array
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadPixels()](loadPixels_)[updatePixels()](updatePixels_)[get()](get_)[set()](set_)[PImage](PImage)
