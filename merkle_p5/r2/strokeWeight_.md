
#### Nome
### strokeWeight()

#### Exemplos
<img border="0" height="100" src="media/strokeWeight_.gif" width="100"/>

```pde
smooth(); 
strokeWeight(1);   // Padrão 
line(20, 20, 80, 20); 
strokeWeight(4);   // mais espessa
line(20, 40, 80, 40); 
strokeWeight(10);  // muito mais espessa
line(20, 70, 80, 70); 

```

#### Descrição
Configura a espessura utilizada para se desenhar
linhas, pontos, e o contorno das formas. Todas as espessuras são
especificadas em unidades de píxel.
Esta função
não funciona com os renderizadores P2D, P3D, OR
OPENGL (favor ver a referência de size() para mais
informações)

#### Sintaxe
```pde
strokeWeight(espessura)

```
Parâmetros
espessura
int ou float: a espessura (em pixeis)  do traço

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[stroke()](stroke_)[strokeJoin()](strokeJoin_)[strokeCap()](strokeCap_)
