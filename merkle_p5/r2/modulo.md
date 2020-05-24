<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### % (módulo ou resto)
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
int a = 20%100;         // Atribui 20  à a
int b = 20%100;         // Atribui 20 à b
float c = 75.0%100.0;   // Atribui 75.0 à c
float d = 275.0%100.0;  // Atribui 75.0 à d

```
<hr align="left" noshade="noshade" size="1" width="150"/>

```pde
float a = 0.0; 
void draw() { 
  background(204); 
  a = (a + 0.5)%width; 
  line(a, 0, a, height); 
} 

```

#### Descrição
Clacula o resto de uma divisão de um
número por outro.  É extremamente útil para
manter números dentro de um limite, como no caso de manter uma
forma na tela.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
<font color="#996600">value1</font>%<font color="#996600">valor2</font>
            
```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
valor1
int ou float
valor2
int ou float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
int ou float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[/ (divisão)](divide)
