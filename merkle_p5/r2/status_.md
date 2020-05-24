<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### status()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// mova o mouse à direita e à esquerda para ver o texto
// mudar no canto inferior esquerdos de seu navegador
void draw() { 
  if(mouseX < 50) { 
    status("esquerda"); 
  } else { 
    status("direita"); 
  } 
} 

```

#### Descrição
Visualiza uma mensagem na área de status do
navegador. Esta é a área de texto no canto inferior
esqurdo do navegador. A função**status()** só funcionará quando um programa Processing estiver executando em um navegador web.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
status(<font color="#996600">texto</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
texto
String: qualquer String válida
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web
<img height="25" src="../images/1pix.gif" width="1"/>
