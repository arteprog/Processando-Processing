
#### Nome
### spotLight()

#### Exemplos
<img border="0" height="100" src="media/spotLight_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
spotLight(51, 102, 126, 80, 20, 40, -1, 0, 0, PI/2, 2); 
translate(20, 50, 0); 
sphere(30); 

```
<img border="0" height="100" src="media/spotLight_2.jpg" width="100"/>

```pde
size(100, 100, P3D); 
int concentration = 600; // Try 1 -> 10000 
background(0); 
noStroke(); 
background(0); 
spotLight(51, 102, 126, 50, 50, 400, 
          0, 0, -1, PI/16, concentration); 
translate(80, 50, 0); 
sphere(30); 
 

```

#### Descrição
Adiciona uma luz do tipo *spot*. Luzes precisam
ser incluidas em `draw()` para se manterem persistentes em programas em laço. A sua colocação no `setup()`
de um programa em laço causará edeito apenas
 durante a primeira passagem pelo laço. O efeito dos
parâmetros **v1**, **v2**, e **v3 **é determinado pelo atual modo de cor.  Os parâmetros **x**, **y**, e **z **especifiicam a posição da luz e **nx**, **ny**, e **nz **especificam a direção que a luz está iluminando.  O parâmetro `angulo` especifica o o cone de luz da fonte.

#### Sintaxe
```pde
spotLight(v1, v2, v3, x, y, z, nx, ny, nz, angulo, concentracao)

```
Parâmetros
v1
int ou float: valor de vermelho ou de matiz

v2
int ou float: valor de verde ou de saturação


v3
int ou float: valor de azul ou de brilho

x
int ou float: coordenada x da luz pontual

y
int ou float: coordenada y da luz pontual


z
int ou float: coordenada z da luz pontual


nx
int ou float: direção ao longo do eixo x

ny
int ou float: direção ao longo do eixo y


nz
int ou float: direção ao longo do eixo z


angulo
float: ângulo do cone de luz


concentracao
float: expoente que determina a distribição de luz em relação ao eixo do cone



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[lights()](lights_
)
[directionalLight()](directionalLight_
)
[ambientLight()](ambientLight_
)
[pointLight()](pointLight_
)

