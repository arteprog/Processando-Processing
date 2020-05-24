
#### Nome
### class

#### Exemplos

```pde
// Declara e constrói dois objetos (h1 e h2) da classe Hline
HLine h1 = new HLine(20, 2.0); 
HLine h2 = new HLine(50, 2.5); 
 
void setup() 
{ 
  size(200, 200); 
  framerate(30); 
} 
 
void draw() { 
  background(204); 
  h1.update(); 
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
Palavra chave utilizada para indicar a
declaração de uma classe. Uma classe é um
compósito de dados e métodos (funções), que
pode ser instanciada em objetos. Usualmente, a primeira letra do nome
de uma classe é escolhida maiúscula, de modo a
diferenciá-la de outros tipos de variáveis.  Um
tutorial em[Programação Orientada a Objetos](http://java.sun.com/docs/books/tutorial/java/concepts/index), em inglês, pode ser encontrado no sítio da Sun.

#### Sintaxe
```pde
class NomeClasse {
  comandos
}
            
```
Parâmetros
NomeClasse
Qualquer nome válido de variáveis
comandos
Qualquer comando válido

#### Utilização

	
Web & Applicações

#### Relacionado
[Object](Object)
