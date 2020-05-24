
#### Nome
### background()

#### Exemplos
<img border="0" height="100" src="media/background_.gif" width="100"/>

```pde
background(51); 

```
<img border="0" height="100" src="media/background_2.gif" width="100"/>

```pde
background(255, 204, 0); 

```
<img border="0" height="100" src="media/background_3.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
background(b); 

```

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

#### Sintaxe
```pde
background(valor1)
background(valor1, valor2, valor3)
background(image)

```
Parâmetros
valor1
int ou float: vermelho ou velor do matiz (dependendo do modo de cor corrente)
valor2
int ou float: verde ou valor da saturação (dependendo do modo de cor corrente)
valor3
int or float: azul ou valor do brilho (dependendo do modo de cor corrente)
image
PImage: nome da PImage de mesmo tamanho da janela de visualização

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[colorMode()](colorMode_)
