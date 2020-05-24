<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### perspective()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/perspective_.gif" width="100"/>

```pde
// Recria a perspectiva padrão
size(100, 100, P3D); 
noFill(); 
float fov = PI/3.0; 
float cameraZ = (height/2.0) / tan(PI * fov / 360.0); 
perspective(fov, float(width)/float(height), 
            cameraZ/10.0, cameraZ*10.0); 
translate(50, 50, 0); 
rotateX(-PI/6); 
rotateY(PI/3); 
box(45); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Configura a perspecitva padrão ao aplicar encurtamento (n.t.*foreshortening*),
o que faz com que objetos mais distantes aparecem menores que os mais
próximos, Os parâmetros definem um volume de
visualização com a forma de pirâmide truncada.
Objetos próximos a câmera aparecem em seu tamanho real,
enquanto que objetos mais distantes aparecem menores.  Esta
projeção simula a perspectiva do mundo de mod mais
acurado que a perspectiva ortográfica. Sua versão sem
parâmetros configura a perspectiva padrão, e sua
versão com quatro parâmetros especifica a área
precisamente. Os valores padrão equivalem à perspective(PI/3.0, width/height, cameraZ/10.0, cameraZ*10.0) onde cameraZ é ((height/2.0) / tan(PI*60.0/360.0));
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
perspective()
perspective(<font color="#996600">fov</font>, <font color="#996600">aspecto</font>, <font color="#996600">zProx</font>, <font color="#996600">zDist</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
fov
float: ângulo do campo de visão  (em radianos) da direção vertical
aspecto
float: taxa entre largura e altura
zProx
float: posição z do plano de recorte mais próximo
zDist
float: posição z do plano de recorte mais distante
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
