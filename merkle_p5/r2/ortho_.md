<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### ortho()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/ortho_.gif" width="100"/>

```pde
noFill(); 
ortho(0, width, 0, height, -10, 10); 
translate(100, 100, 0); 
rotateX(-PI/6); 
rotateY(PI/3); 
box(45); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Configura a projeção ortográfica e define o volume de recorte paralelo (n.t.* clipping volume*).
Todos os objetos com a mesma dimensão aparecem com o mesmo
tamanho, independentemente se estão próximos ou distantes
da câmera.  Os parâmetros desta função
especificam o volume de recorte, onde**esquerdo** e**direito** são os valores mínimo e máximo de x,**superior** em**inferior**** **os valores mínimo e máximo de x, e**proximo** e**distante**
os valores mínimo e máximo de z. Na ausência de
parâmetros, os valores padrão equivalem àortho(0, width, 0, height, -10, 10).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
ortho()
ortho(<font color="#996600">esquerdo</font>, <font color="#996600">direito</font>, <font color="#996600">inferior</font>, <font color="#996600">superior</font>, <font color="#996600">proximo</font>, <font color="#996600">distante</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
esquerdo
float: plano esquerdo do volume de recorte
direito
float: plano direito do volume de recorte
botton
float: plano inferior do volume de recorte
superior
float: plano superior do volume de recorte
proximo
float: distância mínima da origem ao observador
distante
float: distância máxima da origem ao observador
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
