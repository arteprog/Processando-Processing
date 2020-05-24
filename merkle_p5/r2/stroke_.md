
#### Nome
### stroke()

#### Exemplos
<img border="0" height="100" src="media/stroke_.gif" width="100"/>

```pde
stroke(153); 
rect(30, 20, 55, 55); 

```
<img border="0" height="100" src="media/stroke_2.gif" width="100"/>

```pde
stroke(204, 102, 0); 
rect(30, 20, 55, 55); 

```

#### Descrição
 Sets the color used to draw lines and borders
around shapes. This color is either specified in terms of the RGB ou
HSB color depending on the current **colorMode()** (the default color space is RGB, with each valor in the range from 0 to 255).<i>Note: the valor for the parameter "ciza" must be less than ou equal to the current maximum valor as specified by  **colorMode()** . The default maximum valor is 255.



</i>Atribui cor ao traço utilizado em linhas e contornos de formas Esta cor pode ser
especificada nos termos dos modelos RGB ou HSB, dependendo do modo
corrente especificado através de `colorMode() `( o espaço de cor padrão é o RGB, como cada valor variando de 0 a 255).<span style="font-style: italic;">Nota: o valor do parâmetro "cinza"deve ser menor ou igual ao máximo valor corrente especificado por  `colorMode()` . O valor padrão máximo é 255. </span>

#### Sintaxe
```pde
stroke(ciza)
stroke(ciza, alpha)
stroke(color)
stroke(valor1, valor2, valor3)
stroke(valor1, valor2, valor3, alpha)

```
Parâmetros
ciza
int ou float: número que especifica valor entre preto e branco


alpha
int ou float: opacidade do preenchimento


color
color: qualquer valor do tipo de dados color


valor1
int ou float: valor de vermelho ou de matiz  (dependendo do atual modo de cor)

valor2
int ou float: alor de verde ou de saturação (dependendo do atual modo de cor)


valor3
iint ou float: valor de azul o de brilho  (dependendo do atual modo de cor)



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[noStroke()](noStroke_
)
[colorMode()](colorMode_
)

