<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### colorMode()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/colorMode_.jpg" width="100"/>

```pde
noStroke(); 
colorMode(RGB, 100); 
for(int i=0; i<100; i++) { 
  for(int j=0; j<100; j++) { 
    stroke(i, j, 0); 
    point(i, j); 
  } 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/colorMode_2.jpg" width="100"/>

```pde
noStroke(); 
colorMode(HSB, 100); 
for(int i=0; i<100; i++) { 
  for(int j=0; j<100; j++) { 
    stroke(i, j, 100); 
    point(i, j); 
  } 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Modifica a maneira com que o Processing interpreta dados relativos a cores. Como  as cores de**fill()**,**stroke()** e** ****background()**
são especificadas como valores entre 0 e 255 no modelo RGB de
cor. É possível modificar o intervalo de cor
 utilizado para especificar cores e se mudar de sistema de cor.
Por exemplo, ao chamar (**coloMode(RGB, 1.0)**,
será especificado que os valoreses serão especificados
entre 0 e 1. Os limites para as definições de cores
são alterados ao ajustar os parâmetros intervalo1,
intervalo2, e intervalo3.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
colorMode(<font color="#996600">mode</font>);
colorMode(<font color="#996600">mode</font>, <font color="#996600">intervalo</font>);
colorMode(<font color="#996600">mode</font>, <font color="#996600">intervalo1</font>, <font color="#996600">intervalo2</font>, <font color="#996600">intervalo3</font>);

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
mode
ou RGB ou HSB, o que corresponde a Vermelho/Verde/Azul (n.t.  *Red/Green/Blue*) e Matiz/Saturação/Brilho (n.t.* Hue/Saturation/Brightness*)
intervalo
int ou float: intervalo de todos os elemtos de cor elements
intervalo1
int ou float: intervalo para o vermelho ou para o matiz, dependendo do atual modo de cor
intervalo2
int ou float: intervalo para o verde ou para a saturação, dependendo do atual modo de cor
intervalo3
int ou float: intervalo para o azul ou para o brilho, dependendo do atual modo de cor
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[background()](background_)[fill()](fill_)[stroke()](stroke_)
