<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### cursor()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// Mova o cursor à direita e à esquerda sobre a imagem
// para ver o cursor mudar de uma cruz para uma mão
 
void draw() 
{ 
  if(mouseX < 50) { 
    cursor(CROSS); 
  } else { 
    cursor(HAND); 
  } 
} 

```

#### Descrição
Atribui ao cursor do mouse um ícone
pré-definido, uma imagem, ou o faz aparecer se anteriormente
escondido.  Nos casos em que se queira atribuir uma imagem ao
cursor é recomendado faz6e-lo com imagens de tamanho 16x16 ou
32x32 pixels. Não é possível carregar uma imagem
como cursor nos casos em que se esteja exportando o programa para a
Web. Os valores dos parâmetros**x **e**y** devem ser menores do que as dimensões da imagem.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
cursor()
cursor(<font color="#996600">MODO</font>)
cursor(<font color="#996600">imagem</font>, <font color="#996600">x</font>, <font color="#996600">y</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODO
escolher entre  ARROW, CROSS, HAND, MOVE, TEXT, WAIT

                 n.t. (flecha, cruz, mão, movimento, texto, e espera)
imagem
PImage: qualquer variável do tipo PImage
x
int: o ponto horizontal ativo do cursor
y
int: o ponto vertical ativo do cursor
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noCursor()](noCursor_)
