<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### link()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void draw() { 
  rect(20, 20, 60, 60); 
} 
 
void mousePressed() { 
  link("http://processing.org"); 
} 

```
<hr align="left" noshade="noshade" size="1" width="150"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
link(<font color="#996600">url</font>)
link(<font color="#996600">url</font>, <font color="#996600">alvo</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
url
String: complete url as a String in quotes
alvo
String: nome da janela a carregar a url como uma string entre aspas
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>
