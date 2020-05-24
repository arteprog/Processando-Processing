
#### Nome
### cursor()

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

#### Sintaxe
```pde
cursor()
cursor(MODO)
cursor(imagem, x, y)

```
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

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noCursor()](noCursor_)
