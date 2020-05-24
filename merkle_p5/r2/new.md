<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### new
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
HLine h1 = new HLine(); 
float[] speeds = new float[3]; 
float ypos; 
 
void setup() { 
  size(200, 200); 
  speeds[0] = 0.1; 
  speeds[1] = 2.0; 
  speeds[2] = 0.5; 
} 
 
void draw() { 
  ypos += speeds[int(random(3))]; 
  if (ypos > width) { 
    ypos = 0; 
  } 
  h1.update(ypos); 
} 
 
class HLine { 
  void update(float y) { 
    line(0, y, width, y); 
  } 
} 
 

```

#### Descrição
Cira um "novo" objeto. A palavra chave**new**
é tipicamente usada de modo similar à suas
aplicações no exemplo acima. Neste exemplo, um novo
objeto "h1"do tipo "HLine"é criado. Na linha seguinte,  um
novo vetor de velocidades do tipo float, chamado "speeds", é
criado.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
new 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
