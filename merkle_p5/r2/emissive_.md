
#### Nome
### emissive()

#### Exemplos
<img border="0" height="100" src="media/emissive_.jpg" width="100"/>

```pde
size(100, 100, P3D); 
background(0); 
noStroke(); 
background(0); 
directionalLight(204, 204, 204, .5, 0, -1); 
emissive(0, 26, 51); 
translate(70, 50, 0); 
sphere(30); 
 

```

#### Descrição
Acusta a cor emissividade de materiais utilizados
para se desenhar formas geométricas na tela.  É
utilizada em combinação com**ambient()**,**specular()**, e**shininess()**para se configurar as propriedades materiais de formas geométricas.

#### Sintaxe
```pde
emissive(cinza)
emissive(cor)
emissive(v1, v2, v3)

```
Parâmetros
cinza
int ou float: número que especifica valor entre preto e branco
cor
color: qualquer valor do tipo de dados color
v1
int ou float: valor de vermelho ou de matiz
v2


                  int ou float: valor de verde ou de saturação
v3
int ou float: valor de azul ou de brilho

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[ambient()](ambient_)[specular()](specular_)[shininess()](shininess_)
