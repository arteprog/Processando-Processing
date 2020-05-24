<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### beginCamera()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/beginCamera_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
beginCamera(); 
resetMatrix(); 
lookat(0, height/2, 180, width/2, height/2, 0, 0, 1, 0); 
endCamera(); 
translate(50, 50, 0); 
rotateX(-PI/6); 
rotateY(PI/3); 
box(45); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
As funções**beginCamera() ** e** endCamera() **permitem alterar o espaço da câmera através de chamadas à transformações como**lookar()**
e outras. Esta função especifica o modo matriz à
matriz da câmera, e conseqüentemente chamadas
à applyMatrix() e resetMatrix() afetam a câmara. A
função**beginCamera() ** deve ser  sempre utilizada com conjunto com**endCamera() **e pares de**beginCamera()** e**endCamera() ** não podem  ser aninhados.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
beginCamera()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[camera()](camera_)[endCamera()](endCamera_)
