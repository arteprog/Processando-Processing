
#### Nome
### colorMode()

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

#### Descrição
Modifica a maneira com que o Processing interpreta dados relativos a cores. Como  as cores de **fill()**, **stroke()** e ** ** **background()**
são especificadas como valores entre 0 e 255 no modelo RGB de
cor. É possível modificar o intervalo de cor
 utilizado para especificar cores e se mudar de sistema de cor.
Por exemplo, ao chamar ( `coloMode(RGB, 1.0)`,
será especificado que os valoreses serão especificados
entre 0 e 1. Os limites para as definições de cores
são alterados ao ajustar os parâmetros intervalo1,
intervalo2, e intervalo3.

#### Sintaxe
```pde
colorMode(mode);
colorMode(mode, intervalo);
colorMode(mode, intervalo1, intervalo2, intervalo3);

```
Parâmetros
mode
ou RGB ou HSB, o que corresponde a Vermelho/Verde/Azul (n.t.   *Red/Green/Blue* ) e Matiz/Saturação/Brilho (n.t. * Hue/Saturation/Brightness* )


intervalo
int ou float: intervalo de todos os elemtos de cor elements


intervalo1
int ou float: intervalo para o vermelho ou para o matiz, dependendo do atual modo de cor


intervalo2
int ou float: intervalo para o verde ou para a saturação, dependendo do atual modo de cor


intervalo3
int ou float: intervalo para o azul ou para o brilho, dependendo do atual modo de cor



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[background()](background_
)
[fill()](fill_
)
[stroke()](stroke_
)

