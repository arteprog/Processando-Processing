<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### . (ponto)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// Declara e constrói dois objetos (h1, h2) da classe HLine
HLine h1 = new HLine(20, 1.0); 
HLine h2 = new HLine(50, 5.0); 
 
void setup() { 
  size(200, 200); 
} 
 
void draw() { 
  if(h2.speed > 1.0) {  // speed se traduz como velocidade
    h2.speed -= 0.01; 
  } 
  h1.update(); 		// update se traduz como atualização
  h2.update();  
} 
 
class HLine { 
  float ypos, speed; 
  HLine (float y, float s) {  
    ypos = y; 
    speed = s; 
  } 
  void update() { 
    ypos += speed; 
    if (ypos > width) { 
      ypos = 0; 
    } 
    line(0, ypos, width, ypos); 
  } 
} 

```

#### Descrição
Permite o acesso aos métodos e dados de um
objeto. Um objeto é uma instância de uma classe e
contém um grupo de métodos (funções do
objeto) e dados (constantes e variáveis do objeto). O operador
ponto direcion o programa para a informação encapsulada
dentro do objeto.
Provides access to an object's methods and data. An object is an
instance of a class and contains is a grouping of methods (object
functions) and data (object variables and constants). The dot operator
directs the program to the information encapsulated within an object.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
<font color="#996600">objecto</font>.<font color="#996600">metodo()</font>
<font color="#996600">objecto</font>.<font color="#996600">dado</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
objeto
o objeto que se quer acessar
metodo()
o método encapsulado no objeto
dada
variável ou constante encapsulada no objeto
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[Object](Object)
