<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### stroke()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/stroke_.gif" width="100"/>

```pde
stroke(153); 
rect(30, 20, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/stroke_2.gif" width="100"/>

```pde
stroke(204, 102, 0); 
rect(30, 20, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
 Sets the color used to draw lines and borders
around shapes. This color is either specified in terms of the RGB ou
HSB color depending on the current**colorMode()** (the default color space is RGB, with each valor in the range from 0 to 255).<i>Note: the valor for the parameter "ciza" must be less than ou equal to the current maximum valor as specified by **colorMode()**. The default maximum valor is 255.



</i>Atribui cor ao traço utilizado em linhas e contornos de formas Esta cor pode ser
especificada nos termos dos modelos RGB ou HSB, dependendo do modo
corrente especificado através de**colorMode() **( o espaço de cor padrão é o RGB, como cada valor variando de 0 a 255).<span style="font-style: italic;">Nota: o valor do parâmetro "cinza"deve ser menor ou igual ao máximo valor corrente especificado por **colorMode()**. O valor padrão máximo é 255. </span>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
stroke(<font color="#996600">ciza</font>)
stroke(<font color="#996600">ciza</font>, <font color="#996600">alpha</font>)
stroke(<font color="#996600">color</font>)
stroke(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>)
stroke(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>, <font color="#996600">alpha</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noStroke()](noStroke_)[colorMode()](colorMode_)
