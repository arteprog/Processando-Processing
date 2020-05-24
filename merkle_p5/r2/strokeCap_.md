<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### strokeCap()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Estabelece o estilo de renderização
do começo efinal das linhas.  Estas
terminações são quadradas, estendidas ou
arredondadas, e são especidicadas respectivamente através
dos parâmetrosSQUARE, PROJECT, ou ROUND. A capa (*cap*) padrão é ROUND. Esta função
não funciona com os renderizadores P2D, P3D, OR
OPENGL (favor ver a referência de size() para mais
informações)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
strokeCap(<font color="#996600">MODO</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
MODO
qualquer um entre: SQUARE, PROJECT, ou ROUND
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[stroke()](stroke_)[strokeWeight()](strokeWeight_)[strokeJoin()](strokeJoin_)
