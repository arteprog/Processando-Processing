<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### lights()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/lights_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
// Especifica as luzes ambiente
// e direcionada 
lights(); 
translate(20, 50, 0); 
sphere(30); 
translate(60, 0, 0); 
sphere(30); 

```
<img height="25" src="../images/1pix.gif" width="1"/>
<img border="0" height="100" src="media/lights_2.jpg" width="100"/>

```pde
void setup() { 
  size(100, 100, P3D); 
  background(0); 
  noStroke(); 
} 
 
void draw() { 
  // Adiciona um luz ao início de 
  // draw() para torná-la persistente 
  lights(); 
  translate(20, 50, 0); 
  sphere(30); 
  translate(60, 0, 0); 
  sphere(30); 
} 
 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Especifica o valor padrão de luz ambiente, direcionada,*falloff *(n.t.
decaimento), e especular. Os valores padrão são
ambientLight(128, 128, 128), directionalLight(128, 128, 128, 0, 0, -1),
falloff(1, 0, 0), e specular(0, 0, 0). Luzes são
incluídas na função draw() para permanecerem
persistentes em programas em laço. Sua chamda em setup() em um
programa em laço terá efeito apenas na primeira vez que
se percorrer este.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
lights()

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[ambientLight()](ambientLight_)[directionalLight()](directionalLight_)[pointLight()](pointLight_)[spotLight()](spotLight_)
