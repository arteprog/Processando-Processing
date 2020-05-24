<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### framerate
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  framerate(30); 
} 
 
void draw() { 
  line(0, 0, width, height); 
  println(framerate); 
} 

```

#### Descrição
A variável**framerate**
contém o número aproximado de quadros por segundo que o
software consegue executar. O valor inicial é 10 fps (n.t.*frames per second*
ou quadros por segundo) e é atualizado a cada quadro. O valor
 é a média (integrativa) de vários quadros.
Como tal, este valor não será válido ante de 5 ou
10 quadros.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
framerate

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[framerate()](framerate_)
