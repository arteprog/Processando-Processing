
#### Nome
### strokeJoin()

#### Exemplos
<img border="0" height="100" src="media/strokeJoin_.gif" width="100"/>

```pde
smooth(); 
strokeWeight(10.0); 
strokeJoin(MITER); 
beginShape(LINE_STRIP); 
vertex(35, 20); 
vertex(65, 50); 
vertex(35, 80); 
endShape(); 

```
<img border="0" height="100" src="media/strokeJoin_2.gif" width="100"/>

```pde
smooth(); 
strokeWeight(10.0); 
strokeJoin(BEVEL); 
beginShape(LINE_STRIP); 
vertex(35, 20); 
vertex(65, 50); 
vertex(35, 80); 
endShape(); 

```
<img border="0" height="100" src="media/strokeJoin_3.gif" width="100"/>

```pde
smooth(); 
strokeWeight(10.0); 
strokeJoin(ROUND); 
beginShape(LINE_STRIP); 
vertex(35, 20); 
vertex(65, 50); 
vertex(35, 80); 
endShape(); 

```

#### Descrição
Configura o estilo de juntas que conectam segmentos
de linha. Estas juntas podem ser em meia-esquadria,  chanfradas ou
arredondas, e são especificadas respectivamente através
do parâmetros  MITER, BEVEL, e ROUND. A junta padrão corresponde à meia-esquadria; MITER. Esta
função não funciona com os
renderizadores P2D, P3D, OR OPENGL (favor ver a
referência de size() para mais informações)

#### Sintaxe
```pde
strokeJoin(MODO)

```
Parâmetros
MODO
Qualquer um entre: MITER, BEVEL, ou ROUND



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[stroke()](stroke_
)
[strokeWeight()](strokeWeight_
)
[strokeCap()](strokeCap_
)

