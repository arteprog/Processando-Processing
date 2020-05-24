
#### Nome
### frustum()

#### Exemplos
<img border="0" height="100" src="media/frustum_.gif" width="100"/>

```pde
size(100, 100, P3D); 
noFill(); 
background(204); 
frustum(-width/2, width, 0, height, -100, 200.0); 
rotateY(PI/6); 
box(45); 

```

#### Descrição
Configura a matris de perspectiva através de
seus parâmetros. Trabalha como glFrustum, excetp que reinicializa
atual matriz de perspectiva em vez de fazer a
multiplicação a esta.

#### Sintaxe
```pde
frustum(esquerda, direita, inferior, superior, proximo, distante)

```
Parâmetros
esquerda
float: coordenada esquerda do plano de recorte
direita
float:coordenada direita do plano de recorte
inferior
float: coordenada inferior do plano de recorte
superior
float: coordenada superior do plano de recorte
proximo
float: coordenada do plano de recorte mais próximo
distante
float: coordenada do plano de recorte mais distante

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[camera()](camera_)[endCamera()](endCamera_)[perspective()](perspective_)
