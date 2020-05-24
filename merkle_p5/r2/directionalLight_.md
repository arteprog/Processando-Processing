
#### Nome
### directionalLight()

#### Exemplos
<img border="0" height="100" src="media/directionalLight_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
directionalLight(51, 102, 126, -1, 0, 0); 
translate(20, 50, 0); 
sphere(30); 

```
<img border="0" height="100" src="media/directionalLight_2.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
directionalLight(51, 102, 126, 0, -1, 0); 
translate(80, 50, 0); 
sphere(30); 
 

```

#### Descrição
Adiciona uma luz direta. A luz direta vem apenas de
uma direção e é mais forte quando atinge uma
superfície ortogonalmente,e mais fraca quando a atingem em um
pequeno ângulo. Após atingir uma superfície, a luz
direta se espalha em todas as direções. Luzes precisam
ser incluidas em**draw()** para se manterem persistentes em programas em laço. A sua colocação no**setup()**
de um programa em laço causará edeito apenas
 durante a primeira passagem pelo laço. O efeito dos
parâmetros**v1**,**v2**, e**v3 **é determinado pelo atual modo de cor.  Os parâmetros**nx**,**ny**, e**nz **especificam a direção que a luz está iluminando. Por exemplo, ao especificar**ny** como -1 determina que a geometria será iluminada de baixo (a luz está iluminando diretamente para cima).

#### Sintaxe
```pde
directionalLight(v1, v2, v3, nx, ny, nz)

```
Parâmetros
v1
int ou float: valor de vermelho ou de matiz
v2


                  int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho
nx
int ou float: direção ao longo do eixo x
ny
int ou float: direção ao longo do eixo y
nz
int ou float: direção ao longo do eixo z

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[lights()](lights_)[ambientLight()](ambientLight_)[pointLight()](pointLight_)[spotLight()](spotLight_)
