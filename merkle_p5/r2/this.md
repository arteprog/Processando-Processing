
#### Nome
### this

#### Exemplos

```pde
float ypos = 50; 
 
void setup() { 
  size(100, 100); 
  noLoop(); 
} 
 
void draw() { 
  line(0, 0, 100, ypos); 
  this.ypos = 100; 
  line(0, 0, 100, ypos); 
} 
 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
import processing.video.*; 
Movie myMovie; 
 
void setup() { 
  size(200, 200); 
  background(0); 
  myMovie = new Movie(this, "totoro.mov"); 
  myMovie.loop(); 
} 
 
void draw() { 
  if(myMovie.available()) { 
    myMovie.read(); 
  } 
  image(myMovie, 0, 0); 
} 
 

```

#### Descrição
Se refere ao objeto atual ou corrente (ex. "this object"). Em Processing é muito comum o uso de**this ** para se passar a referência de um objeto corrente a umas das bibliotacas. A palavra chace**this ** também
pode ser utilizada da outro modo, mas nem sempre é
necessário. Por exemplo, ao se chamar o método**filter() **de um objeto**PImage**  chamado**tree**, se escreve**tree.filter()**. Para se chamar este método dentro da própria**PImage** é possível escrever simplesmente**filter()**, ou se pode explicitamente escrever**this.filter(). **  Não é errado escrever**this.filter()** mas n não é necessários, pois isto está sempre implícito.

#### Sintaxe
```pde
this

```

#### Utilização

	
Web & Applicações
