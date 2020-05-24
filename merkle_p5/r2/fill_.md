<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### fill()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/fill_.gif" width="100"/>

```pde
fill(153); 
rect(30, 20, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/fill_2.gif" width="100"/>

```pde
fill(204, 102, 0); 
rect(30, 20, 55, 55); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Atribui cor para ser usada no preenchimento de formas. Por exemplo, ao chamar**fill(204,102,0) ** e
desenhar um ret6angulo, este e todas as fomras subsequentes,
serão preenchidas com um tom de laranja. Esta cor pode ser
especificada nos termos dos modelos RGB ou HSB, dependendo do modo
corrente especificado através de**colorMode() **( o espaço de cor padrão é o RGB, como cada valor variando de 0 a 255).<span style="font-style: italic;">Nota: o valor do parâmetro "cinza"deve ser menor ou igual ao máximo valor corrente especificado por **colorMode()**. O valor padrão máximo é 255. </span><i></i>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
fill(<font color="#996600">cinza</font>)
fill(<font color="#996600">cinza</font>, <font color="#996600">alpha</font>)
fill(<font color="#996600">cor</font>)
fill(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>)
fill(<font color="#996600">valor1</font>, <font color="#996600">valor2</font>, <font color="#996600">valor3</font>, <font color="#996600">alpha</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
cinza
int ou float: número que especifica valor entre preto e branco
alpha
int ou float: opacidade do preenchimento
cor
color: qualquer valor do tipo de dados color
valor1
int ou float: valor de vermelho ou de matiz  (dependendo do atual modo de cor)
valor2
int ou float: valor de verde ou de saturação  (dependendo do atual modo de cor)
valor3
int ou float: valor de azul o de brilho  (dependendo do atual modo de cor)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[noFill()](noFill_)[colorMode()](colorMode_)
