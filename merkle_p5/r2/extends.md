
#### Nome
### extends

#### Exemplos

```pde
DrawDot dd1 = new DrawDot(50, 80); 
 
void setup() { 
  size(200, 200); 
} 
 
void draw() { 
  dd1.display(); 
} 
 
// Classe de base
class Dot { 
  int xpos, ypos; 
} 
 
// A classe DrawBot estende a classe Dot
// ao herdar seus métodos e campos e adicionar 
// dois novos métodos

class DrawDot extends Dot { 
  DrawDot(int x, int y) { 
    xpos = x; 
    ypos = y; 
  } 
  void display() { 
    ellipse(xpos, ypos, 200, 200); 
  } 
} 
 

```



#### Descrição
permite a uma nova classe *herdar*
os métodos e campos(dados membro) de uma classe existente.
 Ao escrever o código, se coloca o nome da nova classe,,
seguido da palavra chave `extends`, e do nome da *classe de base.* O conceito de herança é um do princípios fundamentais a programação orientada a objetos.

#### Sintaxe
```pde
extends

```

#### Utilização

	
Web & Applicações
