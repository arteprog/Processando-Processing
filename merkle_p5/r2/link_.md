
#### Nome
### link()

#### Exemplos

```pde
void draw() { 
  rect(20, 20, 60, 60); 
} 
 
void mousePressed() { 
  link("http://processing.org"); 
} 

```



```pde
void draw() { 
  rect(20, 20, 60, 60); 
} 
 
void mousePressed() { 
  link("http://processing.org", "_new"); 
} 
 

```



#### Descrição
Faz um link a uma página web na mesma janela ou em uma nova janele. A URL completa deve ser especificada.

#### Sintaxe
```pde
link(url)
link(url, alvo)

```
Parâmetros
url
String: complete url as a String in quotes


alvo
String: nome da janela a carregar a url como uma string entre aspas



#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações
