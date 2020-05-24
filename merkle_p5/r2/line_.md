
#### Nome
### line()

#### Exemplos
<img border="0" height="100" src="media/line_.gif" width="100"/>

```pde
line(30, 20, 85, 75); 

```
<img border="0" height="100" src="media/line_2.gif" width="100"/>

```pde
line(30, 20, 85, 20); 
stroke(126); 
line(85, 20, 85, 75); 
stroke(255); 
line(85, 75, 30, 75); 

```
<img border="0" height="100" src="media/line_3.gif" width="100"/>

```pde
// O desenho de linhas em 3D requer P3D
// ou OPENGL como parâmetro de sizze()
size(100, 100, P3D); 
line(30, 20, 0, 85, 20, 15); 
stroke(126); 
line(85, 20, 15, 85, 75, 0); 
stroke(255); 
line(85, 75, 0, 30, 75, -50); 

```

#### Descrição
Desenha uma linha (um caminho direto entre dois pontos) na janela de visualização. A versão de `line()` com quatro parâmetros desenha uma linha em 2D. Para se utilizar cor em uma linha, utilize a função `stroke()`. Uma linha não pode ser preenchida, e conseqüentemente o método `fill`
não afetará a cor de uma linha. Linhas em 2D são
desenhadas com espessura padrão de um píxel, mas isto
pode ser modificado através da funcção **strokeWeight(). **A
versão com seis parâmetros permite que uma linha seja
posicionada em qualquer lugar do espaço XYZ. O desenho desta
forma em 3D  faz uso do parâmetro `z ` e deve ser combinado com o uso do parâmerto P3D ou OPENGL em size() , como no exemplo acima.

#### Sintaxe
```pde
line(x1, y1, x2, y2); 
line(x1, y1, z1, x2, y2, z2); 

```
Parâmetros
x1
int ou float: coordenada-x do primeiro ponto


y1
int ou float: coordenada-y do primeiro ponto


z1
int ou float: coordenada-z do primeiro ponto


x2
int ou float: coordenada-x do segundo ponto


y2
int ou float: coordenada-y do segundo ponto


z2
int ou float: coordenada-z do segundo ponto



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[strokeWeight()](strokeWeight_
)
[strokeJoin()](strokeJoin_
)
[strokeCap()](strokeCap_
)
[beginShape()](beginShape_
)

