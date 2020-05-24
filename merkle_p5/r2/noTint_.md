
#### Nome
### noTint()

#### Exemplos
<img border="0" height="100" src="media/noTint_.jpg" width="100"/>

```pde
PImage b; 
b = loadImage("laDefense.jpg"); 
tint(0, 153, 204); // Tingimento azul
image(b, 0, 0); 
noTint(); // Desabilita tingimento
image(b, 50, 0); 

```

#### Descrição
Retira o atual valor de tingimento para se visualizar imagems, de modo a visualizá-las coms seus matizes originais.

#### Sintaxe
```pde
noTint()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[tint()](tint_)[image()](image_)
