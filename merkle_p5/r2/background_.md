<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### background()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/background_.gif" width="100"/>

```pde
background(51); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/background_2.gif" width="100"/>

```pde
background(255, 204, 0); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/background_3.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
background(b); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
A função**background()**
configura a cor de fundo da janela de visualização do
Processing.  O valor padrão é um cinza claro. Na
função**draw()** a
cor de fundo é utilizada para atualizar a janela de
visualização entre os quadros. É possível
carregar uma imagem JPG ou GIF como fundo ao carregar uma imagem do
mesmo tamanho que a janela de visualização. A imagem
precisa estar na diretório data do diretório de
esboços para carregar co sucesso.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
background(<font color="#996600">valor1</font>)
background(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>)
background(<font color="#996600">image</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor1
int ou float: vermelho ou velor do matiz (dependendo do modo de cor corrente)
valor2
int ou float: verde ou valor da saturação (dependendo do modo de cor corrente)
valor3
int or float: azul ou valor do brilho (dependendo do modo de cor corrente)
image
PImage: nome da PImage de mesmo tamanho da janela de visualização
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[colorMode()](colorMode_)
