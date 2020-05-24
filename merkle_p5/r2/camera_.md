<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### camera()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/lookat_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
background(204); 
camera(70.0, 35.0, 120.0, 50.0, 50.0, 0.0, 
       0.0, 1.0, 0.0); 
translate(50, 50, 0); 
rotateX(-PI/6); 
rotateY(PI/3); 
box(45); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Configura a posição da câmara
ao especificar a posição do olho, o centro da cena, e
qual eixo está direcionado para cima.  O movimento da
posição do olho e para onde está apontando (centro
da cena)  permite que imagens sejam vistas de ângulos
diferentes. A versão sem nenhum parâmetro atribui a
câmera o valor padrão, que aponta para o centro da janela
com o eixo Y apontando para cima. Os valores padrão são
camera(width/2.0, height/2.0, ((height/2.0) / tan(PI*60.0 / 360.0),
width/2.0, height/2.0, 0, 0, 1, 0). Esta função é
similar a gluLookAt() em OpenGL, mas primeiro limpa a atual
configuração da câmera.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
camera()
camera(<font color="#996600">olhoX</font>, <font color="#996600">olhoY</font>, <font color="#996600">olhoZ</font>, <font color="#996600">centroX</font>, <font color="#996600">centroY</font>, <font color="#996600">centroZ</font>, <font color="#996600">upX</font>, <font color="#996600">upY</font>, <font color="#996600">upZ</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
olhoX
float: x coordenada  do olho
olhoY
float: y coordenada  do olho
olhoZ
float: z coordenada  do olho
centroX
float: coordenada x do centro da cena
centroY
float: coordenada y  do centro da cena
centroZ
float: coordenada z do centro da cena
upX
float: usualmente 0.0, 1.0, ou -1.0
upY
float: usualmente 0.0, 1.0, ou -1.0
upZ
float: usualmente 0.0, 1.0, ou -1.0
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[camera()](camera_)[endCamera()](endCamera_)[frustum()](frustum_)
