
#### Nome
### pointLight()

#### Exemplos
<img border="0" height="100" src="media/pointLight_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
pointLight(51, 102, 126, 35, 40, 36); 
translate(80, 50, 0); 
sphere(30); 
 

```

#### Descrição
Adiciona um luz pontual.  Luzes precisam
ser incluidas em**draw()** para se manterem persistentes em programas em laço. A sua colocação no**setup()**
de um programa em laço causará efeito apenas
 durante a primeira passagem pelo laço. Os efeitos dos parâmetros**v1**,**v2**, e**v3** parameters são determinados pelo atual modo de cor. Os par6ametros**x**,**y**, e**z **especificam a posição da luz.

#### Sintaxe
```pde
pointLight(v1, v2, v3, x, y, z)

```
Parâmetros
v1
int ou float: valor de vermelho ou de matiz
v2
int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho
x
int ou float: coordenada x da luz pontual
y
int ou float: coordenada y da luz pontual
z
int ou float: coordenada z da luz pontual

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[lights()](lights_)[directionalLight()](directionalLight_)[ambientLight()](ambientLight_)[spotLight()](spotLight_)
