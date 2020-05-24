
#### Nome
### screenY()

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

#### Sintaxe
```pde
screenY(x, y, z)

```
Parâmetros
x
int ou float: coordenada 3D x a ser mapeada
y
int ou float: coordenada 3D y a ser mapeada
z
int ou float: coordenada 3D z a ser mapeada

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[screenX()](screenX_)[screenZ()](screenZ_)
