
#### Nome
### frameCount

#### Exemplos

```pde
void setup() { 
  framerate(30); 
} 
 
void draw() { 
  line(0, 0, width, height); 
  println(frameCount); 
} 

```



#### Descrição
A variável de sistema `frameCaount  `contém o número de quadros visualisado desde que o program iniciou.  Em `setup() ` seu
valor é 0, após a primeira iteração de
draw() é 1,  após a segunda 2, e assim
consecutivamente.

#### Sintaxe
```pde
framerate

```

#### Utilização

	
Web & Applicações

#### Relacionado
[frameRate()](framerate_
)

