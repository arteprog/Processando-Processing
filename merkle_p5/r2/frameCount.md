<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### frameCount
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  framerate(30); 
} 
 
void draw() { 
  line(0, 0, width, height); 
  println(frameCount); 
} 

```

#### Descrição
A variável de sistema**frameCaount  **contém o número de quadros visualisado desde que o program iniciou.  Em**setup() ** seu
valor é 0, após a primeira iteração de
draw() é 1,  após a segunda 2, e assim
consecutivamente.
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
[frameRate()](framerate_)
