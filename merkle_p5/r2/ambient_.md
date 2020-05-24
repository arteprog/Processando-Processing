<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ambient()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/ambient_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
directionalLight(153, 153, 153, .5, 0, -1); 
ambientLight(153, 102, 0); 
ambient(51, 26, 0); 
translate(70, 50, 0); 
sphere(30); 
 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Ajusta a reflectância ambiente para formas a
desenhar na tela. Isto é combinado com a componente de luz
ambiente do cenário. O ajiste das componentes das cores
através dos parâmetros definem a reflect6ancia. Por
exemplo, no modo de cor padrão, atribuir v1=255, v2=126, v3=0,
faria que toda luz vermelha, e metade da verde, fossem
 refletidas. É utilizada em combinação com**emissive**,**specular()**, e**shininess() **para se configurar as propriedades materiais de formas geométricas.**ness()** in setting the materal properties of shapes.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
ambient(<font color="#996600">cinza</font>)
ambient(<font color="#996600">cor</font>)
ambient(<font color="#996600">v1</font>, <font color="#996600">v2</font>, <font color="#996600">v3</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
cinza
int ou float: número que especifica valor entre preto e branco
cor
color: qualquer valor do tipo de dados color
v1
int ou float: valor de vermelho ou de matiz
v2
int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[emissive()](emissive_)[specular()](specular_)[shininess()](shininess_)
