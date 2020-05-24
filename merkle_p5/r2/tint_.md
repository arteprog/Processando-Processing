
#### Nome
### tint()

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
<img border="0" height="100" src="media/tint_2.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
image(b, 0, 0); 
// tinge de azul e ajusta transparência 
tint(0, 153, 204, 126); 
image(b, 50, 0); 

```

#### Descrição
Configura o valor de preenchiemtno para se
visualizar imagems. Imagens pode ser tingidas com cores
específicas ou tornadas transparentes ao se ajustar o
alpha.

#### Sintaxe
```pde
tint(cinza)
tint(cinza, alpha)
tint(valor1, valor2, valor3)
tint(valor1, valor2, valor3, alpha)
tint(color)

```
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



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noTint()](noTint_
)
[image()](image_
)

