
#### Nome
### noCursor()

#### Exemplos

```pde
// Press the mouse to hide the cursor 
void draw() 
{ 
  if(mousePressed == true) { 
    noCursor(); 
  } else { 
    cursor(HAND); 
  } 
} 

```

#### Descrição
Esconde o cursor de vista.  Não irá funcionar quando o programa for executado em um navegador web.

#### Sintaxe
```pde
noCursor()

```

#### Retorno

	
Nenhum

#### Utilização

	
Application

#### Relacionado
[cursor()](cursor_)
