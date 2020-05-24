<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### draw()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
float yPos = 0.0; 
 
void setup() { 
  size(200, 200); 
  framerate(30); 
} 
 
void draw() { 
  background(204); 
  yPos = yPos - 1.0; 
  if(yPos < 0) { 
    yPos = height; 
  } 
  line(0, yPos, width, yPos); 
} 
 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
void setup() { 
  size(200, 200); 
} 
 
void draw() { } 
 
void mousePressed() { 
  line(mouseX, 10, mouseX, 90); 
} 
 

```

#### Descrição
A função**draw()** é chamada imediatamente após a execução de**setup() ** e tem executadas suas linhas de código continuamente até que o programa seja parado, ou que**noLoop()** seja chamada.**draw() **é
chamada  automaticamente e jamais deve ser chamada explicitamente.
 deve ser sempre controlado através de**noLoop()**,** redraw()**, e** loop(). **Depois que**noLoop() **para o código de executar em**draw(), redraw() ** faz com que o código em**draw() **execute uma única vez,  e**loop()** faz com que este mesmo código seja executado de novo  continuamante. O número de vezes por segundo que**draw() **é executada pode ser cotrolada pelas funções**delay() **e por**framerate(). **Pode haver apenas uma função**draw()** em cada  esboço e**draw() ** deve existir caso se queira que o código execute continuamente,  ou para processar eventos como**mousePressed(). ** Ocasionalmente,há a possibilidade de se ter uma chamada vazia a**draw() **em um programa, como  mostrado no segundo  exemplo acima.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
draw() {
  <font color="#996600">comandos</font>
}
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
comandos
Uma sequëncia qualquer de comandos
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[setup()](setup_)[loop()](loop_)[noLoop()](noLoop_)[redraw()](http://www.processing.org/reference/redraw_)[framerate()](http://www.processing.org/reference/framerate_)
