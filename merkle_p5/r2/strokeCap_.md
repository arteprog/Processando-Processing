
#### Nome
### strokeCap()

#### Exemplos
<img border="0" height="100" src="media/strokeCap_.gif" width="100"/>

```pde
smooth(); 
strokeWeight(12.0); 
strokeCap(ROUND); 
line(20, 30, 80, 30); 
strokeCap(SQUARE); 
line(20, 50, 80, 50); 
strokeCap(PROJECT); 
line(20, 70, 80, 70); 

```

#### Descrição
Estabelece o estilo de renderização
do começo efinal das linhas.  Estas
terminações são quadradas, estendidas ou
arredondadas, e são especidicadas respectivamente através
dos parâmetrosSQUARE, PROJECT, ou ROUND. A capa (*cap*) padrão é ROUND. Esta função
não funciona com os renderizadores P2D, P3D, OR
OPENGL (favor ver a referência de size() para mais
informações)

#### Sintaxe
```pde
strokeCap(MODO)

```
Parâmetros
MODO
qualquer um entre: SQUARE, PROJECT, ou ROUND

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[stroke()](stroke_)[strokeWeight()](strokeWeight_)[strokeJoin()](strokeJoin_)
