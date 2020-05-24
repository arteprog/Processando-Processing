<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### tint()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/tint_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 
// Tint blue 
tint(0, 153, 204); 
image(b, 50, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/tint_2.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 
// tinge de azul e ajusta transparência 
tint(0, 153, 204, 126); 
image(b, 50, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Configura o valor de preenchiemtno para se
visualizar imagems. Imagens pode ser tingidas com cores
específicas ou tornadas transparentes ao se ajustar o
alpha.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
tint(<font color="#996600">cinza</font>)
tint(<font color="#996600">cinza</font>, <font color="#996600">alpha</font>)
tint(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>)
tint(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>, <font color="#996600">alpha</font>)
tint(<font color="#996600">color</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
cinza
int ou float: qualquer número válido
alpha
int ou float: opacidade da imagem
valor1
int ou float: valor de vermelho ou de matiz
valor2
int ou float: valor de verde ou de saturação
valor3
int ou float: valor de azul ou de brilho
color
color: qualquer valor do tipo de dados color
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noTint()](noTint_)[image()](image_)
