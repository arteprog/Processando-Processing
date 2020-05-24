<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### screenY()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  size(100, 100, P3D); 
} 
 
void draw() { 
  background(204); 
  
  float x = mouseX; 
  float y = mouseY; 
  float z = -100; 
  
  // Desenha "X" em z = -100 
  stroke(255); 
  line(x-10, y-10, z, x+10, y+10, z); 
  line(x+10, y-10, z, x-10, y+10, z); 
  
  // Desenha uma linha em 2D no mesmo valor y
  // Note a paralaxe
  stroke(102); 
  line(0, y, 0, width, y, 0); 
  
  // desenha uma linha 2D que se ajusta ao balor y do
  // elemento desenhado em z = -100 
  stroke(0); 
  float theY = screenY(x, y, z); 
  line(0, theY, 0, width, theY, 0);    
}  

```

#### Descrição
Recebe uma posição
tri-diemensional X,Y,Z e retorna o valor Y de onde ela iria
aparecer em uma tela (bi-dimensional).
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
screenY(<font color="#996600">x</font>, <font color="#996600">y</font>, <font color="#996600">z</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
x
int ou float: coordenada 3D x a ser mapeada
y
int ou float: coordenada 3D y a ser mapeada
z
int ou float: coordenada 3D z a ser mapeada
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[screenX()](screenX_)[screenZ()](screenZ_)
