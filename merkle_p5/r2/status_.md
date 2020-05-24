
#### Nome
### status()

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
esqurdo do navegador. A função `status()` só funcionará quando um programa Processing estiver executando em um navegador web.


#### Sintaxe
```pde
status(texto)

```
Parâmetros
texto
String: qualquer String válida



#### Retorno

	
Nenhum

#### Utilização

	
Web
