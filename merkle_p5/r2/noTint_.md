<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### noTint()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/noTint_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
tint(0, 153, 204); // Tingimento azul
image(b, 0, 0); 
noTint(); // Desabilita tingimento
image(b, 50, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Retira o atual valor de tingimento para se visualizar imagems, de modo a visualizá-las coms seus matizes originais.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
noTint()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[tint()](tint_)[image()](image_)
