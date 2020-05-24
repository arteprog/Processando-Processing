
#### Nome
### Object

#### Exemplos

```pde
// declara e constrói dois objetos, h1 e h2, de tipo definido pela classe HLine
HLine h1 = new HLine(20, 2.0); 
HLine h2 = new HLine(50, 2.5); 
 
void setup() 
{ 
  size(200, 200); 
  framerate(30); 
} 
 
void draw() { 
  background(204); 
  h1.update(); 
  h2.update();  
} 
 
class HLine { 
  float ypos, speed; 
  HLine (float y, float s) {  
    ypos = y; 
    speed = s; 
  } 
  void update() { 
    ypos += speed; 
    if (ypos > width) { 
      ypos = 0; 
    } 
    line(0, ypos, width, ypos); 
  } 
} 

```



#### Descrição
Objetos são instâncias de classes. Uma
classe é um agregado de métodos (funções)
relacionados e campos (variáveis e constantes).

#### Sintaxe
```pde
class instancia
            
```
Parâmetros
class
o tipo da classe que o objeto será instanciado ou criado


instancia
qualquer nome válido de variável



#### Utilização

	
Web & Applicações

#### Relacionado
[class](class
)

