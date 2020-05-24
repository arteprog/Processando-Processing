<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### mag()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/mag_.gif" width="100"/>

```pde
float x1 = 20; 
float x2 = 80; 
float y1 = 30; 
float y2 = 70; 
 
line(0, 0, x1, y1); 
println(mag(x1, y1));  // Imprime 36.05551 
line(0, 0, x2, y1); 
println(mag(x2, y1));  // Imprime 85.44004 
line(0, 0, x1, y2); 
println(mag(x1, y2));  // Imprime 72.8011 
line(0, 0, x2, y2); 
println(mag(x2, y2));  // Imprime 106.30146 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula a magnitude  (ou comprimento) de um
vetor. Um vetor é uma direção no espaço
comumente utilizada em computação gráfica e
algebra linear. Como não tem
posição "inicial", a magnitude de um vetor pode ser
compreendica como a distância entre a coordenada (0,0) e seu
 valor (x,y). Portanto, mag() é uma maneira abreviada de se
escrever "dist(0,0,x,y)".
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
mag(<font color="#996600">a</font>, <font color="#996600">b</font>)
mag(<font color="#996600">a</font>, <font color="#996600">b</font>, <font color="#996600">c</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
a
float ou int: primeiro valor<description>
</description>
b
float ou int: segundo valor<description>
</description>
c
float ou int: terceiro valor<description>
</description>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[dist()](dist_)
