<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### size()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  size(320, 240); 
  background(153); 
} 
 
void draw() { 
  line(0, 0, width, height); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
void setup() { 
  size(320, 240, P3D); 
  background(153); 
} 
 
void draw() { 
  line(0, 0, 0, width, height, -200); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
import processing.opengl.*; 
 
void setup() { 
  size(screen.width, screen.height, OPENGL); 
  background(153); 
} 
 
void draw() { 
  line(0, 0, 0, width, height, -200); 
} 

```

#### Descrição
Define a dismensão da janela de visualização em unidades de pixeils. A função**size() **deve ser a primeira linha em**setup()**. Caso**size() **não seja chamada, o tamanho padrão assumido (*default*)  para a janela é de 100x100 pixels. Às variáveis de sistema**width **(n.t largura) e**height **(n.t. altura), são atribuídos os valores passados pelos parâmetros da função<span style="font-weight: bold;">size(). ** **</span> A tulilização de variáveis como parâmetros em**size() ** é desencorajada e pode causar problemas. Utilize as variáveis**width** e** height**
se é preciso conhever as dimensões horizontal e vertical,
respectivamente,  da janela de visualização em um
programa.
O parâmetro MODE seleciona qual o mecanismo de
renderização a ser utilizado. Por exemplo, no desenho de
formas 3D para uso na Web utiliza-se**P3D**; na exportação de um programa com aceleração gráfica OpenGl utiliza-se**OPENGL. **Segue uma  descrição breve dos quatro mecanismos de renderização:
P2D (Processing 2D) - Renderizador 2D com suporte para  Java 1.1 export (NÃO ESTÁ ATUALMENTE IMPLEMENTADO)
P3D (Processing 3D) - Rrenderizador 3D rápido para a web
JAVA2D - O renderizador padrão assumido. Possui excelente qualidade em geral, mas é mais lendo que o P2D.
OPENGL - Interface com hardware que possui suporte para
aceleração OpenGL, de modo a aumentar a velocidade de
placas gráficas OpenGl instaladas.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
size(<font color="#996600">width</font>, <font color="#996600">height</font>)
size(<font color="#996600">width</font>, <font color="#996600">height</font>, <font color="#996600">MODE</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
width
int: largura da janela de visualização em pixels
height
int: altura da janela de visualização em píxels
MODE
Qualquer entre P2D, P3D, JAVA2D, ou OPENGL
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
